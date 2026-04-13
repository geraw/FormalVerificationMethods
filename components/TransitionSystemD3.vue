<template>
  <div ref="containerRef" class="transition-system-container flex justify-center items-center mt-8"
       @mousedown.stop @touchstart.stop @pointerdown.stop @wheel.stop>
    <div v-if="zoomable && showZoomControls" class="zoom-controls">
      <button type="button" class="zoom-button" @click.stop="zoomOut">-</button>
      <button type="button" class="zoom-button" @click.stop="resetZoom">Reset</button>
      <button type="button" class="zoom-button" @click.stop="zoomIn">+</button>
    </div>
    <svg ref="svgRef" :width="width" :height="height" class="overflow-visible">
      <defs>
        <marker v-for="color in uniqueColors" :key="color"
          :id="getMarkerId(color)" markerWidth="7" markerHeight="5" 
          refX="6" refY="2.5" orient="auto">
          <polygon points="0 0, 7 2.5, 0 5" :fill="color" />
        </marker>
      </defs>
      <g ref="zoomLayer">
        <g class="links"></g>
        <g class="nodes"></g>
      </g>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch, computed } from 'vue';
import * as d3 from 'd3';
import katex from 'katex';
import 'katex/dist/katex.min.css';

// Interfaces
interface State {
  id: string;
  x?: number;
  y?: number;
  label?: string; // Atomic Propositions (below right)
  name?: string;  // Inside the rectangle
  text?: string;  // Alias for name
  width?: number; // Custom width override
  initial?: boolean;
  initialDirection?: 'left' | 'right' | 'top' | 'bottom';
  initialStroke?: string;
  initialStrokeWidth?: number;
  labelX?: number; // Offset for label
  labelY?: number;
  initialText?: string;
  initialTextWidth?: number;
  initialTextHeight?: number;
  stroke?: string;
  strokeWidth?: number;
  color?: string;
  rx?: number;
}

interface Transition {
  source: string;
  target: string;
  action?: string;
  actionFontSize?: number;
  loopDirection?: string; // e.g., '0deg', '90deg'
  loopRadius?: number;
  loopLabelRadius?: number;
  loopSpread?: number;
  actionWidth?: number;
  actionHeight?: number;
  actionX?: number; // Offset from default center
  actionY?: number; // Offset from default center
  curve?: number;
  midPoints?: { x: number; y: number }[];
  stroke?: string;
  strokeWidth?: number;
}

interface Props {
  states: State[];
  transitions: Transition[];
  width?: number;
  height?: number;
  auto?: boolean;
  zoomable?: boolean;
  showZoomControls?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  width: 600,
  height: 400,
  auto: true,
  zoomable: false,
  showZoomControls: false,
});

const svgRef = ref<SVGSVGElement | null>(null);
const zoomLayer = ref<SVGGElement | null>(null);
const containerRef = ref<HTMLDivElement | null>(null);

const markerIdBase = `arrowhead-ts-d3-${Math.random().toString(36).slice(2, 11)}`;
const getMarkerId = (color: string) => `${markerIdBase}-${color.replace('#', '')}`;
const zoomable = computed(() => props.zoomable);
const showZoomControls = computed(() => props.showZoomControls);

const uniqueColors = computed(() => {
    const set = new Set<string>();
    set.add('#333'); // Default
    props.transitions.forEach(t => {
        if (t.stroke) set.add(t.stroke);
    });
    props.states.forEach(s => {
        if (s.initialStroke) set.add(s.initialStroke);
    });
    return Array.from(set);
});

function getInitialArrowColor(state: State) {
    if (state.initialStroke) return state.initialStroke;
    return '#333';
}

function getInitialArrowStrokeWidth(state: State) {
    if (state.initialStrokeWidth !== undefined) return state.initialStrokeWidth;

    const outgoingWidths = new Set(
        props.transitions
            .filter(t => t.source === state.id)
            .map(t => t.strokeWidth !== undefined ? t.strokeWidth : 2)
    );
    if (outgoingWidths.size === 1) return Array.from(outgoingWidths)[0];

    const allTransitionWidths = new Set(
        props.transitions.map(t => t.strokeWidth !== undefined ? t.strokeWidth : 2)
    );
    if (allTransitionWidths.size === 1) return Array.from(allTransitionWidths)[0];

    return 2;
}

let simulation: d3.Simulation<d3.SimulationNodeDatum, undefined> | null = null;
let zoomBehavior: d3.ZoomBehavior<SVGSVGElement, unknown> | null = null;
let currentZoomTransform = d3.zoomIdentity;

const zoomMin = 0.12;
const zoomMax = 3;

function applyZoomTransform(transform: d3.ZoomTransform) {
    currentZoomTransform = transform;
    if (!zoomLayer.value) return;
    d3.select(zoomLayer.value).attr("transform", transform.toString());
}

function setupZoom() {
    if (!svgRef.value) return;

    const svg = d3.select(svgRef.value);

    if (!props.zoomable) {
        svg.on(".zoom", null);
        zoomBehavior = null;
        applyZoomTransform(d3.zoomIdentity);
        return;
    }

    zoomBehavior = d3.zoom<SVGSVGElement, unknown>()
        .scaleExtent([zoomMin, zoomMax])
        .extent([[0, 0], [props.width, props.height]])
        .translateExtent([
            [-props.width * 2, -props.height * 2],
            [props.width * 3, props.height * 3],
        ])
        .filter((event: any) => {
            const target = event.target as Element | null;
            if (event.type === 'wheel') return true;
            if (event.type === 'mousedown') {
                return event.button === 0 && !target?.closest?.('.node-group');
            }
            if (event.type === 'touchstart') {
                return !target?.closest?.('.node-group');
            }
            return false;
        })
        .on("zoom", (event) => {
            applyZoomTransform(event.transform);
            event.sourceEvent?.stopPropagation?.();
        });

    svg.call(zoomBehavior);
    svg.on("dblclick.zoom", null);
    svg.call(zoomBehavior.transform, currentZoomTransform);
}

function zoomIn() {
    if (!svgRef.value || !zoomBehavior) return;
    d3.select(svgRef.value)
        .transition()
        .duration(180)
        .call(zoomBehavior.scaleBy, 1.2);
}

function zoomOut() {
    if (!svgRef.value || !zoomBehavior) return;
    d3.select(svgRef.value)
        .transition()
        .duration(180)
        .call(zoomBehavior.scaleBy, 1 / 1.2);
}

function resetZoom() {
    if (!svgRef.value || !zoomBehavior) return;
    d3.select(svgRef.value)
        .transition()
        .duration(180)
        .call(zoomBehavior.transform, d3.zoomIdentity);
}

const escapeHtml = (str: string): string =>
    str
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');

// Render inline math while escaping plain text, so labels like <l0, {...}>
// stay visible instead of being interpreted as HTML.
const renderMath = (str: string, preserveLineBreaks = false): string => {
    if (!str) return '';

    const renderSegment = (segment: string) => {
        const parts = segment.split('$');
        return parts.map((part, index) => {
            if (index % 2 === 1) {
                try {
                    return katex.renderToString(part, { throwOnError: false });
                } catch (e) {
                    return escapeHtml(part);
                }
            }
            return escapeHtml(part);
        }).join('');
    };

    if (!preserveLineBreaks) {
        return renderSegment(str);
    }

    return str
        .split('<br>')
        .map(segment => renderSegment(segment))
        .join('<br>');
};

const render = () => {
    if (!svgRef.value || !zoomLayer.value) return;

    if (simulation) {
       simulation.stop();
       simulation = null;
    }

    const svg = d3.select(svgRef.value);
    const layer = d3.select(zoomLayer.value);
    
    // Clear existing
    layer.select(".links").selectAll("*").remove();
    layer.select(".nodes").selectAll("*").remove();

    const rectW = 60;
    const rectH = 40;

    // Prepare data
    const nodes = props.states.map(s => ({ 
        ...s, 
        x: s.x ?? undefined, 
        y: s.y ?? undefined,
        fx: s.x, 
        fy: s.y
    }));
    
    // Initial positions
    nodes.forEach(n => {
        if (n.x === undefined) n.x = props.width/2 + (Math.random()-0.5)*50;
        if (n.y === undefined) n.y = props.height/2 + (Math.random()-0.5)*50;
    });

    const links = props.transitions.map(t => ({ ...t }));

    function centeredCurveValues(count: number, step = 0.18) {
        if (count <= 1) return [0];
        const midpoint = (count - 1) / 2;
        return Array.from({ length: count }, (_, index) => (index - midpoint) * step);
    }

    function sameSideCurveValues(count: number, start = 0.16, step = 0.14) {
        return Array.from({ length: count }, (_, index) => start + index * step);
    }

    function pairKey(link: any) {
        return [String(link.source), String(link.target)].sort().join("::");
    }

    function curveValue(link: any) {
        return link.curve !== undefined ? link.curve : link.__autoCurve;
    }

    const pairGroups = new Map<string, any[]>();
    links.forEach(link => {
        if (link.source === link.target) return;
        if (link.midPoints && link.midPoints.length > 0) return;

        const key = pairKey(link);
        if (!pairGroups.has(key)) pairGroups.set(key, []);
        pairGroups.get(key)!.push(link);
    });

    pairGroups.forEach(group => {
        if (group.length <= 1) return;
        if (group.some(link => link.curve !== undefined)) return;

        const directedGroups = new Map<string, any[]>();
        group.forEach(link => {
            const key = `${link.source}->${link.target}`;
            if (!directedGroups.has(key)) directedGroups.set(key, []);
            directedGroups.get(key)!.push(link);
        });

        if (directedGroups.size > 1) {
            directedGroups.forEach(directedLinks => {
                const autoCurves = sameSideCurveValues(directedLinks.length);
                directedLinks.forEach((link, index) => {
                    link.__autoCurve = autoCurves[index];
                });
            });
            return;
        }

        const autoCurves = centeredCurveValues(group.length);
        group.forEach((link, index) => {
            link.__autoCurve = autoCurves[index];
        });
    });

    // Helper: Rectangle Intersection
    function getRectIntersection(dx: number, dy: number, w: number, h: number) {
       if (dx === 0 && dy === 0) return { x: 0, y: 0 };
       const tX = (w / 2) / Math.abs(dx);
       const tY = (h / 2) / Math.abs(dy);
       const t = Math.min(tX, tY);
       return { x: dx * t, y: dy * t };
    }
    
    // Helper: Self Loop Path
    function getSelfLoopPath(
       x: number,
       y: number,
       dirStr: string = '-45deg',
       nodeWidth: number = rectW,
       loopRadius: number = 80,
       loopSpread: number = Math.PI / 5,
    ) {
       let angle = -Math.PI * 3 / 4; 
       const degMatch = dirStr.match(/(-?[\d.]+)deg/);
       if (degMatch) {
           angle = parseFloat(degMatch[1]) * Math.PI / 180;
       } else if (!isNaN(parseFloat(dirStr))) {
           angle = parseFloat(dirStr) * Math.PI / 180;
       }

       const spread = loopSpread;
       const a1 = angle - spread;
       const a2 = angle + spread;
       
       const p1 = getRectIntersection(Math.cos(a1), Math.sin(a1), nodeWidth, rectH);
       const x1 = x + p1.x;
       const y1 = y + p1.y;
       
       const p2 = getRectIntersection(Math.cos(a2), Math.sin(a2), nodeWidth, rectH);
       const x2 = x + p2.x;
       const y2 = y + p2.y;
       
       const cpDist = loopRadius;
       const cx1 = x + Math.cos(a1) * cpDist;
       const cy1 = y + Math.sin(a1) * cpDist;
       const cx2 = x + Math.cos(a2) * cpDist;
       const cy2 = y + Math.sin(a2) * cpDist;
 
       return `M ${x1},${y1} C ${cx1},${cy1} ${cx2},${cy2} ${x2},${y2}`;
    }

    // Determine layout strategy
    const hasMissingCoords = props.states.some(s => s.x === undefined || s.y === undefined);
    const shouldSimulate = props.auto || hasMissingCoords;

    // Drag handlers (defined before use)
    function dragstarted(event: any, d: any) {
        if (!event.active && simulation) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }
    function dragged(event: any, d: any) {
        d.fx = event.x;
        d.fy = event.y;
        d.x = event.x;
        d.y = event.y;
    }
    function dragended(event: any, d: any) {
        if (!event.active && simulation) (simulation as any).alphaTarget(0);
    }
    
    // Right-click handler to print current coordinates
    function printCoordinates(event: MouseEvent) {
        event.preventDefault();
        const statesCode = nodes.map(n => {
            const parts = [`id: '${n.id}'`];
            if (n.text) parts.push(`text: '${n.text}'`);
            if (n.label) parts.push(`label: '${n.label}'`);
            if (n.initial) parts.push(`initial: true`);
            parts.push(`x: ${Math.round(n.x!)}`);
            parts.push(`y: ${Math.round(n.y!)}`);
            return `    { ${parts.join(', ')} }`;
        }).join(',\n');
        console.log(`:states="[\n${statesCode}\n]"`);
    }

    // Drag behavior
    const dragBehavior = d3.drag<SVGGElement, any>()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

    // Draw Links
    const linkGroup = layer.select(".links");
    const linkSelection = linkGroup.selectAll("g")
        .data(links)
        .enter()
        .append("g")
        .attr("class", "link-group");

        const paths = linkSelection.append("path")
        .attr("stroke", (d: any) => d.stroke || "#333")
        .attr("stroke-width", (d: any) => d.strokeWidth || 2)
        .attr("fill", "none")
        .attr("marker-end", (d: any) => `url(#${getMarkerId(d.stroke || "#333")})`);

    // Link Labels (foreignObject) - keep reference to foreignObject for positioning
    const linkLabelFOs = linkSelection.append("foreignObject")
        .attr("width", (d: any) => d.actionWidth || 100)  
        .attr("height", (d: any) => d.actionHeight || 30)
        .style("overflow", "visible");
    
    // Inner div for styling and KaTeX content
    linkLabelFOs.append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-size", (d: any) => `${d.actionFontSize || 12}px`)
        .style("padding", "0")
        .html((d: any) => d.action ? `<span style="background:white; padding:1px 3px; border-radius:2px; color: ${d.stroke || 'inherit'}">${renderMath(d.action, true)}</span>` : "");

    // Draw Nodes
    const nodeGroup = layer.select(".nodes");
    const nodeSelection = nodeGroup.selectAll("g")
        .data(nodes)
        .enter()
        .append("g")
        .attr("class", "node-group")
        .call(dragBehavior);
    

    // Node Rectangle
    nodeSelection.append("rect")
        .attr("width", (d: any) => d.width || rectW)
        .attr("height", rectH)
        .attr("x", (d: any) => -(d.width || rectW) / 2)
        .attr("y", -rectH / 2)
        .attr("rx", (d: any) => d.rx !== undefined ? d.rx : 5)
        .attr("ry", (d: any) => d.rx !== undefined ? d.rx : 5)
        .attr("fill", (d: any) => d.color || "#FFF59D")
        .attr("stroke", (d: any) => d.stroke || "#000")
        .attr("stroke-width", (d: any) => d.strokeWidth !== undefined ? d.strokeWidth : 2)
        .style("cursor", "grab")
        .on("contextmenu", printCoordinates);

    // Initial state arrow
    nodeSelection.filter(d => !!d.initial).append("path")
        .attr("d", (d: any) => {
             const dir = d.initialDirection || 'left';
             const len = 30; // Length of the arrow itself
             const gap = 5;  // Gap from node boundary
             const nw = d.width || rectW;
             const nh = rectH;
             
             if (dir === 'left') return `M -${nw/2 + gap + len},0 L -${nw/2 + gap},0`;
             if (dir === 'right') return `M ${nw/2 + gap + len},0 L ${nw/2 + gap},0`;
             if (dir === 'top') return `M 0,-${nh/2 + gap + len} L 0,-${nh/2 + gap}`;
             if (dir === 'bottom') return `M 0,${nh/2 + gap + len} L 0,${nh/2 + gap}`;
             return `M -${nw/2 + gap + len},0 L -${nw/2 + gap},0`;
        })
        .attr("stroke", (d: any) => getInitialArrowColor(d))
        .attr("stroke-width", (d: any) => getInitialArrowStrokeWidth(d))
        .attr("marker-end", (d: any) => `url(#${getMarkerId(getInitialArrowColor(d))})`);

    // Initial state label (foreignObject)
    const initialLabels = nodeSelection.filter(d => !!d.initial && !!d.initialText).append("foreignObject")
        .attr("width", (d: any) => d.initialTextWidth || 100)
        .attr("height", (d: any) => d.initialTextHeight || 30)
        .style("overflow", "visible")
        .style("pointer-events", "none");

    initialLabels.append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-size", "12px")
        .style("color", "#333")
        .html((d: any) => renderMath(d.initialText));

    // State Name (foreignObject)
    nodeSelection.append("foreignObject")
        .attr("width", (d: any) => d.width || rectW)
        .attr("height", rectH)
        .attr("x", (d: any) => -(d.width || rectW) / 2)
        .attr("y", -rectH / 2)
        .style("pointer-events", "none")
        .append("xhtml:div")
        .style("display", "flex")
        .style("justify-content", "center")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-weight", "bold")
        .style("pointer-events", "none")
        .html((d: any) => renderMath(d.text || d.name || d.id));

    // Label (Propositions - Below Right or custom)
    nodeSelection.append("foreignObject")
        .attr("width", 100)
        .attr("height", 30)
        .attr("x", (d: any) => d.labelX !== undefined ? d.labelX : ((d.width || rectW) / 2 + 5))
        .attr("y", (d: any) => d.labelY !== undefined ? d.labelY : 5)
        .style("pointer-events", "none")
        .append("xhtml:div")
        .attr("dir", "ltr")
        .style("direction", "ltr")
        .style("display", "flex")
        .style("justify-content", "flex-start")
        .style("align-items", "center")
        .style("width", "100%")
        .style("height", "100%")
        .style("font-size", "12px")
        .style("color", "#555")
        .html((d: any) => d.label ? renderMath(d.label) : "");

    // Tick function
    const tick = () => {
        // Debugging
        // console.log("Tick running. Nodes count:", nodes.length, "Links count:", links.length);

        paths.attr("d", d => {
            let source: any = d.source;
            let target: any = d.target;
            
            if (typeof source !== 'object') source = nodes.find(n => n.id === source);
            if (typeof target !== 'object') target = nodes.find(n => n.id === target);
            if (!source || !target) return "";

            if (source.id === target.id) {
               return getSelfLoopPath(
                   source.x!,
                   source.y!,
                   d.loopDirection || '-45deg',
                   source.width || rectW,
                   d.loopRadius || 80,
                   d.loopSpread || Math.PI / 5,
               );
            }
            
            const sw = source.width || rectW;
            const tw = target.width || rectW;

            if (d.midPoints && d.midPoints.length > 0) {
                const firstMid = d.midPoints[0];
                const lastMid = d.midPoints[d.midPoints.length - 1];
                
                const sInt = getRectIntersection(firstMid.x - source.x!, firstMid.y - source.y!, sw, rectH);
                const tInt = getRectIntersection(lastMid.x - target.x!, lastMid.y - target.y!, tw, rectH);
                
                const startPt = { x: source.x! + sInt.x, y: source.y! + sInt.y };
                const endPt = { x: target.x! + tInt.x, y: target.y! + tInt.y };
                
                const currentCurve = curveValue(d);
                if (currentCurve) {
                    if (d.midPoints.length === 1) {
                        return `M ${startPt.x},${startPt.y} Q ${firstMid.x},${firstMid.y} ${endPt.x},${endPt.y}`;
                    } else {
                        // Multi-point curve: simplified as polyline for now or a basic spline
                        let path = `M ${startPt.x},${startPt.y}`;
                        d.midPoints.forEach(p => { path += ` L ${p.x},${p.y}`; });
                        path += ` L ${endPt.x},${endPt.y}`;
                        return path;
                    }
                } else {
                    let path = `M ${startPt.x},${startPt.y}`;
                    d.midPoints.forEach(p => { path += ` L ${p.x},${p.y}`; });
                    path += ` L ${endPt.x},${endPt.y}`;
                    return path;
                }
            }

            const dx = target.x! - source.x!;
            const dy = target.y! - source.y!;
            const dist = Math.sqrt(dx*dx + dy*dy);
            
            const currentCurve = curveValue(d);
            if (currentCurve) {
                const nx = -dy / dist;
                const ny = dx / dist;
                const curveOffset = dist * currentCurve;
                const cx = (source.x! + target.x!) / 2 + nx * curveOffset;
                const cy = (source.y! + target.y!) / 2 + ny * curveOffset;
                
                const sInt = getRectIntersection(cx - source.x!, cy - source.y!, sw, rectH);
                const tInt = getRectIntersection(cx - target.x!, cy - target.y!, tw, rectH);
                
                return `M ${source.x! + sInt.x},${source.y! + sInt.y} Q ${cx},${cy} ${target.x! + tInt.x},${target.y! + tInt.y}`;
            }

            const sInt = getRectIntersection(dx, dy, sw, rectH);
            const tInt = getRectIntersection(-dx, -dy, tw, rectH);
            return `M ${source.x! + sInt.x},${source.y! + sInt.y} L ${target.x! + tInt.x},${target.y! + tInt.y}`;
        });

        linkLabelFOs
            .attr("x", (d: any) => {
                 let s: any = d.source;
                 let t: any = d.target;
                 if (typeof s !== 'object') s = nodes.find(n => n.id === s);
                 if (typeof t !== 'object') t = nodes.find(n => n.id === t);
                 
                 if (!s || !t) return 0;
                 if (s.x === undefined || t.x === undefined) return 0;

                 const w = d.actionWidth || 100;
                 const offsetX = d.actionX || 0;
                 if (s.id === t.id) {
                     const dirStr = d.loopDirection || '-45deg';
                     let angle = -Math.PI * 3 / 4;
                     const degMatch = dirStr.match(/(-?[\d.]+)deg/);
                     if (degMatch) angle = parseFloat(degMatch[1]) * Math.PI / 180;
                     const distLoop = d.loopLabelRadius || (d.loopRadius ? Math.max(50, d.loopRadius - 10) : 70);
                     return s.x! + Math.cos(angle) * distLoop - w/2 + offsetX;
                 }
                 
                 if (d.midPoints && d.midPoints.length > 0) {
                     const mid = d.midPoints[Math.floor(d.midPoints.length / 2)];
                     return mid.x - w/2 + offsetX;
                 }

                 const currentCurve = curveValue(d);
                 if (currentCurve) {
                     const dx = t.x! - s.x!;
                     const dy = t.y! - s.y!;
                     const dist = Math.sqrt(dx*dx + dy*dy);
                     const nx = -dy / dist;
                     const ny = dx / dist;
                     const curveOffset = dist * currentCurve;
                     return (s.x! + t.x!) / 2 + nx * (curveOffset * 0.5) - w/2 + offsetX;
                 }
                 // Center on link
                 return (s.x! + t.x!) / 2 - w/2 + offsetX;
            })
            .attr("y", (d: any) => {
                 let s: any = d.source;
                 let t: any = d.target;
                 if (typeof s !== 'object') s = nodes.find(n => n.id === s);
                 if (typeof t !== 'object') t = nodes.find(n => n.id === t);
                 if (!s || !t) return 0;
                 if (s.y === undefined || t.y === undefined) return 0;

                 const h = d.actionHeight || 30;
                 const offsetY = d.actionY || 0;
                 if (s.id === t.id) {
                     const dirStr = d.loopDirection || '-45deg';
                     let angle = -Math.PI * 3 / 4;
                     const degMatch = dirStr.match(/(-?[\d.]+)deg/);
                     if (degMatch) angle = parseFloat(degMatch[1]) * Math.PI / 180;
                     const distLoop = d.loopLabelRadius || (d.loopRadius ? Math.max(50, d.loopRadius - 10) : 70);
                     return s.y! + Math.sin(angle) * distLoop - h/2 + offsetY;
                 }
                 
                 if (d.midPoints && d.midPoints.length > 0) {
                     // Midpoint of the entire polyline/curve
                     // For now, center on the middle segment or the first midpoint
                     const mid = d.midPoints[Math.floor(d.midPoints.length / 2)];
                     return mid.y - h/2 + offsetY;
                 }

                 const currentCurve = curveValue(d);
                 if (currentCurve) {
                     const dx = t.x! - s.x!;
                     const dy = t.y! - s.y!;
                     const dist = Math.sqrt(dx*dx + dy*dy);
                     const nx = -dy / dist;
                     const ny = dx / dist;
                     const curveOffset = dist * currentCurve;
                     return (s.y! + t.y!) / 2 + ny * (curveOffset * 0.5) - h/2 + offsetY;
                 }
                 return (s.y! + t.y!) / 2 - h/2 + offsetY;
            });
        
        nodeSelection.attr("transform", d => `translate(${d.x},${d.y})`);

        // Position initial state text
        nodeSelection.filter(d => !!d.initial && !!d.initialText).select("foreignObject")
            .attr("x", (d: any) => {
                const w = d.initialTextWidth || 100;
                const dir = d.initialDirection || 'left';
                const len = 50;
                const nw = d.width || rectW;
                if (dir === 'left') return -len - w;
                if (dir === 'right') return nw/2 + 5;
                if (dir === 'top') return -w/2;
                if (dir === 'bottom') return -w/2;
                return -len - w;
            })
            .attr("y", (d: any) => {
                const h = d.initialTextHeight || 30;
                const dir = d.initialDirection || 'left';
                const len = 50;
                if (dir === 'left') return -h/2;
                if (dir === 'right') return -h/2;
                if (dir === 'top') return -len - h;
                if (dir === 'bottom') return len;
                return -h/2;
            });
    };

    if (shouldSimulate) {
        simulation = d3.forceSimulation(nodes as any)
            .force("link", d3.forceLink(links).id((d: any) => d.id).distance(150))
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter(props.width / 2, props.height / 2))
            .force("collide", d3.forceCollide((d: any) => (d.width || rectW) / 2 + 20).iterations(2));
        (simulation as any).on("tick", tick);
    } else {
        tick();
    }

    applyZoomTransform(currentZoomTransform);
    setupZoom();

};

onMounted(() => {
   render();
   
   // Add capture-phase listeners to intercept events before Slidev
   if (containerRef.value) {
       // Bubble phase: stop propagation after children have handled it
       containerRef.value.addEventListener('mousedown', (e) => {
           e.stopPropagation();
       }, { capture: false });
       containerRef.value.addEventListener('pointerdown', (e) => {
           e.stopPropagation();
       }, { capture: false });
       containerRef.value.addEventListener('wheel', (e) => {
           e.stopPropagation();
       }, { capture: false });
   }
});

onBeforeUnmount(() => {
   if (simulation) {
       simulation.stop();
       simulation = null;
   }
   if (svgRef.value) {
       d3.select(svgRef.value).on(".zoom", null);
   }
});

watch(() => [props.states, props.transitions, props.width, props.height, props.zoomable], () => {
   render();
}, { deep: true });
</script>

<style scoped>
.transition-system-container {
  position: relative;
  z-index: 100;
  pointer-events: auto !important;
}
.zoom-controls {
  position: absolute;
  top: -30px;
  right: 65px;
  z-index: 101;
  display: flex;
  gap: 4px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #cbd5e1;
  border-radius: 999px;
  padding: 3px;
  box-shadow: 0 3px 8px rgba(15, 23, 42, 0.1);
}
.zoom-button {
  border: 1px solid #cbd5e1;
  background: #f8fafc;
  color: #0f172a;
  border-radius: 999px;
  min-width: 24px;
  height: 24px;
  padding: 0 7px;
  font-size: 10px;
  font-weight: 700;
  line-height: 1;
  cursor: pointer;
}
.zoom-button:hover {
  background: #e2e8f0;
}
.transition-system-container svg {
  pointer-events: auto !important;
}
.transition-system-container .node-group {
  pointer-events: auto !important;
  cursor: grab;
}
.transition-system-container .node-group:active {
  cursor: grabbing;
}
</style>
