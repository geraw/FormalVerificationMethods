"""
Generate matching question images for transition systems and program graphs.
Visual style matches the TransitionSystemD3.vue component used in course slides:
  - Rectangular nodes with rounded corners
  - AP labels shown outside nodes (bottom-right)
  - Initial states receive an incoming arrow
  - Curved arrows for bidirectional edges
  - Self-loops drawn as arcs
"""

import os
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
from typing import Set, Dict, Tuple, Union, Optional, List

State = Union[str, Tuple]
Action = str
Transition = Tuple[State, Action, State]
LabelingMap = Dict[State, Set[str]]

# ── Style constants matching the course slides ──────────────────────────
NODE_W = 0.17         # default node half-width
NODE_H = 0.14         # node half-height
NODE_FILL = '#f9f9f9'
NODE_EDGE = '#222222'
NODE_LW   = 1.8
ARROW_KW  = dict(arrowstyle='->', lw=1.8, color='#222222',
                 mutation_scale=16)
FONT_NODE  = dict(ha='center', va='center', fontsize=11, fontweight='bold',
                  color='#222222', fontfamily='DejaVu Sans')
FONT_LABEL = dict(ha='left', va='top', fontsize=8.5, color='#555555',
                  fontfamily='DejaVu Sans')
FONT_ACTION = dict(ha='center', va='center', fontsize=9, color='#222222',
                   fontfamily='DejaVu Sans',
                   bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.85))


def _draw_node(ax, x, y, text, label=None, is_initial=False,
               w=None, h=None, initial_dir='left'):
    """Draw one rectangular state node in the course-slides style."""
    w = w if w is not None else NODE_W
    h = h if h is not None else NODE_H
    lw = 2.8 if is_initial else NODE_LW
    rect = FancyBboxPatch((x - w, y - h), 2 * w, 2 * h,
                          boxstyle='round,pad=0.08',
                          facecolor=NODE_FILL, edgecolor=NODE_EDGE,
                          linewidth=lw, zorder=3)
    ax.add_patch(rect)
    ax.text(x, y, text, zorder=4, **FONT_NODE)

    if label:
        # AP label: small text outside bottom-right corner
        ax.text(x + w + 0.06, y - h - 0.05, f'{{{label}}}', zorder=4,
                **FONT_LABEL)

    if is_initial:
        pad = 0.08   # must match FancyBboxPatch pad
        gap = 0.20
        vw = w + pad   # visual half-width
        vh = h + pad   # visual half-height
        if initial_dir == 'left':
            ax.annotate('', xy=(x - vw, y),
                        xytext=(x - vw - gap, y),
                        arrowprops=dict(**ARROW_KW, connectionstyle='arc3,rad=0',
                                        shrinkA=0, shrinkB=0),
                        zorder=5)
        elif initial_dir == 'top':
            ax.annotate('', xy=(x, y + vh),
                        xytext=(x, y + vh + gap),
                        arrowprops=dict(**ARROW_KW, connectionstyle='arc3,rad=0',
                                        shrinkA=0, shrinkB=0),
                        zorder=5)
        elif initial_dir == 'right':
            ax.annotate('', xy=(x + vw, y),
                        xytext=(x + vw + gap, y),
                        arrowprops=dict(**ARROW_KW, connectionstyle='arc3,rad=0',
                                        shrinkA=0, shrinkB=0),
                        zorder=5)
        elif initial_dir == 'bottom':
            ax.annotate('', xy=(x, y - vh),
                        xytext=(x, y - vh - gap),
                        arrowprops=dict(**ARROW_KW, connectionstyle='arc3,rad=0',
                                        shrinkA=0, shrinkB=0),
                        zorder=5)


def _edge_border_pt(cx, cy, w, h, tx, ty, pad=0.08):
    """Return the point on the node rectangle border towards (tx, ty).
    pad accounts for FancyBboxPatch's boxstyle pad so arrows stop at the visual edge."""
    w = w + pad
    h = h + pad
    dx, dy = tx - cx, ty - cy
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return cx, cy
    # Intersect ray with rectangle
    if abs(dx) < 1e-9:
        # vertical
        if dy > 0:
            return cx, cy + h
        else:
            return cx, cy - h
    if abs(dy) < 1e-9:
        # horizontal
        if dx > 0:
            return cx + w, cy
        else:
            return cx - w, cy
    t_x = w / abs(dx)
    t_y = h / abs(dy)
    t = min(t_x, t_y)
    return cx + dx * t, cy + dy * t


def _draw_edge(ax, sx, sy, tx, ty, sw, sh, tw, th, action='',
               curve=0.0, action_offset=(0, 0)):
    """Draw a directed edge between two nodes with an optional action label."""
    # Border points
    bsx, bsy = _edge_border_pt(sx, sy, sw, sh, tx, ty)
    btx, bty = _edge_border_pt(tx, ty, tw, th, sx, sy)

    rad = f'arc3,rad={curve}'
    ax.annotate('', xy=(btx, bty), xytext=(bsx, bsy),
                arrowprops=dict(**ARROW_KW, connectionstyle=rad,
                                shrinkA=0, shrinkB=0),
                zorder=5)

    if action:
        # Midpoint for label, adjusted by offset
        if abs(curve) > 0.01:
            mx = (bsx + btx) / 2 - curve * (bty - bsy) * 0.5
            my = (bsy + bty) / 2 + curve * (btx - bsx) * 0.5
        else:
            mx = (bsx + btx) / 2
            my = (bsy + bty) / 2
        ax.text(mx + action_offset[0], my + action_offset[1], action,
                zorder=3, **FONT_ACTION)


def _draw_self_loop(ax, cx, cy, w, h, action='', direction='top'):
    """Draw a self-loop arc on a node using a cubic Bezier for a round appearance."""
    pad = 0.08          # must match FancyBboxPatch pad
    vw = w + pad        # visual half-width
    vh = h + pad        # visual half-height
    spread = 0.30       # half-distance between loop attachment points
    bulge  = 0.65       # how far the control points stick out

    if direction == 'top':
        p1  = (cx - spread, cy + vh)
        c1  = (cx - spread, cy + vh + bulge)
        c2  = (cx + spread, cy + vh + bulge)
        p2  = (cx + spread, cy + vh)
        lx, ly = cx, cy + vh + bulge + 0.14
        # arrowhead tangent direction: c2→p2
        arr_dx, arr_dy = p2[0] - c2[0], p2[1] - c2[1]
    elif direction == 'bottom':
        p1  = (cx + spread, cy - vh)
        c1  = (cx + spread, cy - vh - bulge)
        c2  = (cx - spread, cy - vh - bulge)
        p2  = (cx - spread, cy - vh)
        lx, ly = cx, cy - vh - bulge - 0.14
        arr_dx, arr_dy = p2[0] - c2[0], p2[1] - c2[1]
    elif direction == 'left':
        p1  = (cx - vw, cy + spread)
        c1  = (cx - vw - bulge, cy + spread)
        c2  = (cx - vw - bulge, cy - spread)
        p2  = (cx - vw, cy - spread)
        lx, ly = cx - vw - bulge - 0.14, cy
        arr_dx, arr_dy = p2[0] - c2[0], p2[1] - c2[1]
    else:  # right
        p1  = (cx + vw, cy - spread)
        c1  = (cx + vw + bulge, cy - spread)
        c2  = (cx + vw + bulge, cy + spread)
        p2  = (cx + vw, cy + spread)
        lx, ly = cx + vw + bulge + 0.14, cy
        arr_dx, arr_dy = p2[0] - c2[0], p2[1] - c2[1]

    import matplotlib.path as mpath
    import matplotlib.patches as mpatches
    verts = [p1, c1, c2, p2]
    codes = [mpath.Path.MOVETO, mpath.Path.CURVE4,
             mpath.Path.CURVE4, mpath.Path.CURVE4]
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor='none', edgecolor='#222222',
                               lw=1.8, zorder=4)
    ax.add_patch(patch)

    # Arrowhead tangent along c2→p2
    norm = math.sqrt(arr_dx**2 + arr_dy**2) or 1e-6
    step = 0.04
    ax.annotate('', xy=p2,
                xytext=(p2[0] - arr_dx / norm * step,
                        p2[1] - arr_dy / norm * step),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#222222',
                                mutation_scale=16,
                                connectionstyle='arc3,rad=0'),
                zorder=5)
    if action:
        ax.text(lx, ly, action, zorder=5, **FONT_ACTION)


# ─────────────────────────────────────────────────────────────────────────────
# Public drawing functions
# ─────────────────────────────────────────────────────────────────────────────

def draw_transition_system(
        title: str,
        node_positions: Dict,   # {state: (x, y)}
        node_labels: Dict,      # {state: ap_label_str}  e.g. {'s0': 'p'}
        initial_states: Set,
        transitions: List[Tuple],   # (src, tgt, action, curve, action_offset)
        self_loops: List[Tuple],    # (state, action, direction)
        filename: str,
        figsize=(8, 5),
        node_widths: Dict = None,
        initial_directions: Dict = None,
):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=13, fontweight='bold', pad=10)

    nw = node_widths or {}
    nd = initial_directions or {}

    # Edges first (behind nodes)
    for (src, tgt, action, curve, aoff) in transitions:
        sx, sy = node_positions[src]
        tx, ty = node_positions[tgt]
        sw = nw.get(src, NODE_W)
        tw = nw.get(tgt, NODE_W)
        _draw_edge(ax, sx, sy, tx, ty, sw, NODE_H, tw, NODE_H,
                   action=action, curve=curve, action_offset=aoff)

    for (state, action, direction) in self_loops:
        cx, cy = node_positions[state]
        w = nw.get(state, NODE_W)
        _draw_self_loop(ax, cx, cy, w, NODE_H, action=action, direction=direction)

    # Nodes on top
    for state, (x, y) in node_positions.items():
        _draw_node(ax, x, y, str(state),
                   label=node_labels.get(state, ''),
                   is_initial=(state in initial_states),
                   w=nw.get(state, NODE_W),
                   initial_dir=nd.get(state, 'left'))

    # Auto-fit
    all_x = [p[0] for p in node_positions.values()]
    all_y = [p[1] for p in node_positions.values()]
    pad = 0.7
    ax.set_xlim(min(all_x) - pad, max(all_x) + pad)
    ax.set_ylim(min(all_y) - pad, max(all_y) + pad)

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filename}")
    plt.close()


def draw_program_graph(
        title: str,
        node_positions: Dict,
        initial_states: Set,
        transitions: List[Tuple],
        self_loops: List[Tuple],
        filename: str,
        figsize=(8, 5),
        node_widths: Dict = None,
        initial_directions: Dict = None,
):
    """Same as draw_transition_system but no AP labels (program graphs don't have L)."""
    draw_transition_system(
        title=title,
        node_positions=node_positions,
        node_labels={},
        initial_states=initial_states,
        transitions=transitions,
        self_loops=self_loops,
        filename=filename,
        figsize=figsize,
        node_widths=node_widths,
        initial_directions=initial_directions,
    )


def generate_ts_images(output_dir: str = '.'):
    """Generate TS1, TS2, TS3 in course-slide style."""

    # ── TS1: s0 ⇄ s1 (cycle), s0 initial ──────────────────────────────────
    draw_transition_system(
        title='Transition System 1 (TS1)',
        node_positions={'s0': (0.0, 0.0), 's1': (3.0, 0.0)},
        node_labels={'s0': 'p', 's1': 'q'},
        initial_states={'s0'},
        transitions=[
            ('s0', 's1', 'a', 0.20, (0, 0.08)),   # s0 → s1 upper
            ('s1', 's0', 'b', 0.20, (0, -0.12)),   # s1 → s0 lower
        ],
        self_loops=[],
        filename=os.path.join(output_dir, 'ts1.png'),
        figsize=(7, 4),
        initial_directions={'s0': 'top'},
    )

    # ── TS2: q0 → q1 → q2 → q0, also q1 → q0 ─────────────────────────────
    draw_transition_system(
        title='Transition System 2 (TS2)',
        node_positions={'q0': (0.0, 0.0), 'q1': (3.0, 0.0), 'q2': (1.5, 2.0)},
        node_labels={'q0': 'r', 'q1': 'r,s', 'q2': 's'},
        initial_states={'q0'},
        transitions=[
            ('q0', 'q1', 'x',  0.0,  (0,  0.12)),
            ('q1', 'q2', 'y',  0.0,  (0.12, 0)),
            ('q2', 'q0', 'γ',  0.0,  (-0.14, 0)),
            ('q1', 'q0', 'x',  0.22, (0, -0.14)),  # curved back arc
        ],
        self_loops=[],
        filename=os.path.join(output_dir, 'ts2.png'),
        figsize=(7, 5),
        initial_directions={'q0': 'left'},
    )

    # ── TS3: t0 self-loop c; t0 → t1 → t0 ─────────────────────────────────
    draw_transition_system(
        title='Transition System 3 (TS3)',
        node_positions={'t0': (0.0, 0.0), 't1': (3.0, 0.0)},
        node_labels={'t0': 'u', 't1': 'v'},
        initial_states={'t0'},
        transitions=[
            ('t0', 't1', 'd', 0.20, (0,  0.10)),
            ('t1', 't0', 'c', 0.20, (0, -0.14)),
        ],
        self_loops=[('t0', 'c', 'top')],
        filename=os.path.join(output_dir, 'ts3.png'),
        figsize=(7, 4),
        initial_directions={'t0': 'left'},
    )


def generate_pg_images(output_dir: str = '.'):
    """Generate PG1, PG2, PG3 in course-slide style."""

    # ── PG1: ℓ₀ ⇄ ℓ₁ ─────────────────────────────────────────────────────
    draw_program_graph(
        title='Program Graph 1 (PG1)',
        node_positions={'ℓ₀': (0.0, 0.0), 'ℓ₁': (3.2, 0.0)},
        initial_states={'ℓ₀'},
        transitions=[
            ('ℓ₀', 'ℓ₁', 'x:=1',   0.22, (0,  0.10)),
            ('ℓ₁', 'ℓ₀', 'x:=x+1', 0.22, (0, -0.14)),
        ],
        self_loops=[],
        filename=os.path.join(output_dir, 'pg1.png'),
        figsize=(7, 4),
        initial_directions={'ℓ₀': 'top'},
    )

    # ── PG2: ℓ₀ → ℓ₁ → ℓ₂ → ℓ₀, self-loop on ℓ₀ ─────────────────────────
    draw_program_graph(
        title='Program Graph 2 (PG2)',
        node_positions={'ℓ₀': (0.0, 0.0), 'ℓ₁': (3.0, 1.5), 'ℓ₂': (3.0, -1.5)},
        initial_states={'ℓ₀'},
        transitions=[
            ('ℓ₀', 'ℓ₁', 'y>0 : skip',  0.0, (-0.10,  0.10)),
            ('ℓ₁', 'ℓ₂', 'y:=y-1',       0.0, ( 0.16,  0)),
            ('ℓ₂', 'ℓ₀', 'y:=0',          0.0, (-0.10, -0.10)),
        ],
        self_loops=[('ℓ₀', 'y≤0 : skip', 'top')],
        filename=os.path.join(output_dir, 'pg2.png'),
        figsize=(7, 5),
        initial_directions={'ℓ₀': 'left'},
    )

    # ── PG3: ℓ₀ ⇄ ℓ₁, self-loop on ℓ₀ ────────────────────────────────────
    draw_program_graph(
        title='Program Graph 3 (PG3)',
        node_positions={'ℓ₀': (0.0, 0.0), 'ℓ₁': (3.2, 0.0)},
        initial_states={'ℓ₀'},
        transitions=[
            ('ℓ₀', 'ℓ₁', 'z:=1', 0.22, (0,  0.10)),
            ('ℓ₁', 'ℓ₀', 'z:=0', 0.22, (0, -0.14)),
        ],
        self_loops=[('ℓ₀', 'z:=0', 'top')],
        filename=os.path.join(output_dir, 'pg3.png'),
        figsize=(7, 4),
        initial_directions={'ℓ₀': 'left'},
    )


if __name__ == '__main__':
    output_dir = r'c:\Users\geraw\courses\FormalVerificationMethods\matching_questions'

    print("Generating transition systems ...")
    generate_ts_images(output_dir)

    print("Generating program graphs ...")
    generate_pg_images(output_dir)

    print("\nAll diagrams created successfully!")
    print(f"Output directory: {output_dir}")

    files = os.listdir(output_dir)
    print("\nGenerated files:")
    for f in sorted(files):
        if f.endswith('.png'):
            print(f"  - {f}")
