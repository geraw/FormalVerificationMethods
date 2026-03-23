import itertools


def extract_ts(n_inputs, initial_r, delta, lam):
    k = len(initial_r)
    states = list(itertools.product([0, 1], repeat=n_inputs + k))
    transitions = []
    labels = {}

    for state in states:
        x = state[:n_inputs]
        r = state[n_inputs:]
        out = lam(x, r)

        active_props = []
        for i, value in enumerate(x):
            if value:
                active_props.append(f'x{i + 1}' if n_inputs > 1 else 'x')
        for i, value in enumerate(r):
            if value:
                active_props.append(f'r{i + 1}' if k > 1 else 'r')
        if out:
            active_props.append('y')

        labels[state] = '{' + ','.join(active_props) + '}'

        next_r = tuple(delta(x, r))
        for next_x in itertools.product([0, 1], repeat=n_inputs):
            transitions.append((state, next_x + next_r))

    init = [state for state in states if state[n_inputs:] == tuple(initial_r)]
    return states, transitions, init, labels


def show_ts(states, transitions, init, labels):
    print("States:")
    for state in states:
        marker = " (initial)" if state in init else ""
        print(f"  {state}  L={labels[state]}{marker}")

    print(f"\nTransitions ({len(transitions)}):")
    seen = set()
    for src, tgt in transitions:
        edge = (src, tgt)
        if edge in seen:
            continue
        seen.add(edge)
        print(f"  {src} --> {tgt}")


def _state_text(state):
    return '(' + ', '.join(str(value) for value in state) + ')'


def _state_width(text):
    return max(76, min(180, 18 + len(text) * 8))


def ts_to_slidev_data(ts):
    states, transitions, init, labels = ts
    state_ids = {state: f's{i}' for i, state in enumerate(states)}

    unique_transitions = []
    seen_edges = set()
    for src, tgt in transitions:
        edge = (src, tgt)
        if edge in seen_edges:
            continue
        seen_edges.add(edge)
        unique_transitions.append({
            'source': state_ids[src],
            'target': state_ids[tgt],
        })

    graph_states = []
    for state in states:
        text = _state_text(state)
        graph_states.append({
            'id': state_ids[state],
            'text': text,
            'label': labels.get(state, '{}'),
            'width': _state_width(text),
            'initial': state in init,
            'initialDirection': 'top',
        })

    return {
        'states': graph_states,
        'transitions': unique_transitions,
        'summary': {
            'states': len(graph_states),
            'transitions': len(unique_transitions),
            'initial': len(init),
        },
    }
