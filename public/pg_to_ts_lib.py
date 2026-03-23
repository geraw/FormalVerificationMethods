import itertools


SAFE_EVAL_GLOBALS = {
    '__builtins__': {},
    'abs': abs,
    'all': all,
    'any': any,
    'bool': bool,
    'dict': dict,
    'int': int,
    'len': len,
    'list': list,
    'max': max,
    'min': min,
    'set': set,
    'sum': sum,
    'tuple': tuple,
}


def identity(env):
    return dict(env)


def update(env, **changes):
    new_env = dict(env)
    new_env.update(changes)
    return new_env


def _normalize_var_domains(var_domains):
    if not isinstance(var_domains, dict):
        raise TypeError('var_domains must be a dict mapping variable names to finite domains.')

    normalized = {}
    for name, domain in var_domains.items():
        values = tuple(domain)
        if not values:
            raise ValueError(f'var_domains[{name!r}] must be non-empty.')
        normalized[name] = values
    return normalized


def _all_evaluations(var_domains):
    names = list(var_domains.keys())
    if not names:
        return [dict()]

    product = itertools.product(*(var_domains[name] for name in names))
    return [dict(zip(names, values)) for values in product]


def _expression_locals(valuation):
    scope = dict(valuation)
    scope['eta'] = dict(valuation)
    scope['update'] = update
    scope['identity'] = identity
    return scope


def _eval_expression(expr, valuation, context_name):
    try:
        return eval(expr, SAFE_EVAL_GLOBALS, _expression_locals(valuation))
    except Exception as exc:
        raise ValueError(f'Failed to evaluate {context_name} expression {expr!r}: {exc}') from exc


def _compile_guard(guard, context_name):
    if callable(guard):
        return guard

    if isinstance(guard, str):
        return lambda eta, expr=guard, name=context_name: bool(
            _eval_expression(expr, eta, name)
        )

    if isinstance(guard, bool):
        return lambda eta, value=guard: value

    raise TypeError(f'{context_name} must be callable, a Python expression string, or a bool.')


def _compile_effect(effect, action_name):
    if callable(effect):
        return effect

    if effect is None:
        return identity

    if isinstance(effect, dict):
        assignments = dict(effect)

        def apply_assignments(eta, assignments=assignments, action_name=action_name):
            base = dict(eta)
            updates = {}
            for name, value_or_expr in assignments.items():
                if isinstance(value_or_expr, str):
                    updates[name] = _eval_expression(
                        value_or_expr,
                        eta,
                        f'assignment to {name!r} in action {action_name!r}',
                    )
                else:
                    updates[name] = value_or_expr
            base.update(updates)
            return base

        return apply_assignments

    if isinstance(effect, str):
        def evaluate_effect(eta, expr=effect, action_name=action_name):
            result = _eval_expression(expr, eta, f'effect for action {action_name!r}')
            if not isinstance(result, dict):
                raise TypeError(
                    f'Effect expression for action {action_name!r} must evaluate to a dict valuation.'
                )
            return result

        return evaluate_effect

    raise TypeError(
        f'Effect for action {action_name!r} must be callable, a dict of assignments, '
        'a Python expression string, or None.'
    )


def _normalize_transition(entry):
    if isinstance(entry, dict):
        source = entry['source']
        guard = entry.get('guard', lambda eta: True)
        action = entry['action']
        effect = entry.get('effect', identity)
        target = entry['target']
    else:
        if len(entry) != 5:
            raise ValueError(
                'Each transition must be either a dict or a 5-tuple '
                '(source, guard, action, effect, target).'
            )
        source, guard, action, effect, target = entry

    action_name = str(action)

    return {
        'source': source,
        'guard': _compile_guard(guard, f'Guard for transition {source!r}->{target!r}'),
        'action': action_name,
        'effect': _compile_effect(effect, action_name),
        'target': target,
    }


def _normalize_valuation(valuation, var_domains, action_name):
    if not isinstance(valuation, dict):
        raise TypeError(
            f'Effect for action {action_name!r} must return a dict valuation, '
            f'but got {type(valuation).__name__}.'
        )

    normalized = {}
    for name, domain in var_domains.items():
        if name not in valuation:
            raise ValueError(
                f'Effect for action {action_name!r} did not assign a value to {name!r}.'
            )
        value = valuation[name]
        if value not in domain:
            raise ValueError(
                f'Effect for action {action_name!r} assigned {name}={value!r}, '
                f'which is outside its finite domain {list(domain)}.'
            )
        normalized[name] = value

    extra = set(valuation.keys()) - set(var_domains.keys())
    if extra:
        raise ValueError(
            f'Effect for action {action_name!r} returned unknown variables: {sorted(extra)}.'
        )

    return normalized


def _state_key(location, valuation, var_names):
    return (location, tuple(valuation[name] for name in var_names))


def pg_to_ts(var_domains, locations, initial_locations, initial_guard, transitions):
    var_domains = _normalize_var_domains(var_domains)
    locations = list(locations)
    initial_locations = list(initial_locations)

    initial_guard = _compile_guard(initial_guard, 'initial_guard')

    location_set = set(locations)
    for location in initial_locations:
        if location not in location_set:
            raise ValueError(f'Initial location {location!r} is not in locations.')

    normalized_transitions = [_normalize_transition(entry) for entry in transitions]
    for transition in normalized_transitions:
        if transition['source'] not in location_set:
            raise ValueError(f'Source location {transition["source"]!r} is not in locations.')
        if transition['target'] not in location_set:
            raise ValueError(f'Target location {transition["target"]!r} is not in locations.')

    var_names = list(var_domains.keys())
    evaluations = _all_evaluations(var_domains)

    states = []
    state_meta = {}
    for location in locations:
        for valuation in evaluations:
            state = _state_key(location, valuation, var_names)
            states.append(state)
            state_meta[state] = {
                'location': location,
                'valuation': dict(valuation),
            }

    initial_states = []
    transitions_out = []

    for state in states:
        meta = state_meta[state]
        location = meta['location']
        valuation = dict(meta['valuation'])

        if location in initial_locations and initial_guard(dict(valuation)):
            initial_states.append(state)

        for transition in normalized_transitions:
            if transition['source'] != location:
                continue
            if not transition['guard'](dict(valuation)):
                continue

            next_valuation = transition['effect'](dict(valuation))
            next_valuation = _normalize_valuation(
                next_valuation,
                var_domains,
                transition['action'],
            )
            target_state = _state_key(transition['target'], next_valuation, var_names)
            transitions_out.append((state, target_state, transition['action']))

    return states, transitions_out, initial_states, state_meta, var_names


def _state_text(location, valuation, var_names):
    valuation_dict = {name: valuation[name] for name in var_names}
    return f"<{location}, {valuation_dict!r}>"


def _state_width(text):
    return max(110, min(320, 20 + len(text) * 7))


def _action_width(action_text):
    lines = action_text.split('<br>')
    longest = max((len(line) for line in lines), default=0)
    return max(48, min(180, 20 + longest * 7))


def pg_ts_to_slidev_data(ts):
    states, transitions, initial_states, state_meta, var_names = ts
    state_ids = {state: f's{i}' for i, state in enumerate(states)}

    edge_map = {}
    for src, tgt, action in transitions:
        key = (src, tgt)
        edge_map.setdefault(key, [])
        if action not in edge_map[key]:
            edge_map[key].append(action)

    graph_states = []
    for state in states:
        meta = state_meta[state]
        text = _state_text(meta['location'], meta['valuation'], var_names)
        graph_states.append({
            'id': state_ids[state],
            'text': text,
            'width': _state_width(text),
            'initial': state in initial_states,
            'initialDirection': 'top',
            'color': '#f8fafc',
            'stroke': '#334155',
            'strokeWidth': 2,
        })

    graph_transitions = []
    for (src, tgt), actions in edge_map.items():
        action_text = '<br>'.join(actions)
        transition = {
            'source': state_ids[src],
            'target': state_ids[tgt],
            'action': action_text,
            'actionWidth': _action_width(action_text),
            'actionFontSize': 10,
        }

        if src == tgt:
            transition['loopDirection'] = '90deg'
            transition['actionY'] = 24
        elif (tgt, src) in edge_map:
            transition['curve'] = -0.16 if state_ids[src] < state_ids[tgt] else 0.16

        graph_transitions.append(transition)

    return {
        'states': graph_states,
        'transitions': graph_transitions,
        'summary': {
            'states': len(graph_states),
            'transitions': len(graph_transitions),
            'initial': len(initial_states),
        },
    }
