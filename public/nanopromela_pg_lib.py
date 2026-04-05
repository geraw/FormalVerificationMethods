"""
Adapted from the NanoPromela-to-program-graph notebook code in FVM-Python/HW4.ipynb.
This helper parses a NanoPromela statement and returns Slidev-friendly graph data.
"""

from collections import defaultdict, deque
from itertools import chain

from lark import Lark, Transformer, Tree


EXIT_LOCATION = "EXIT"

NANO_PROMELA_GRAMMAR = r"""
    ?start: statement

    ?statement: assign_stmt
              | skip_stmt
              | comm_stmt
              | if_stmt
              | do_stmt
              | atomic_stmt
              | sequence_stmt

    sequence_stmt: statement ";" statement

    skip_stmt: "skip"                -> skip

    assign_stmt: NAME ":=" expr
    comm_stmt: channel "!" expr      -> send
             | channel "?" NAME      -> recv

    if_stmt: "if" guarded_command+ "fi"  -> if_stmt
    do_stmt: "do" guarded_command+ "od"  -> do_stmt

    guarded_command: "::" condition ("->" | "=>") statement

    atomic_stmt: "atomic" "{" assign_stmt (";" assign_stmt)* "}"

    ?condition: or_expr

    ?or_expr: and_expr
            | or_expr "||" and_expr      -> or_op

    ?and_expr: not_expr
             | and_expr "&&" not_expr    -> and_op

    ?not_expr: "!" not_expr              -> not_op
             | atom_condition

    ?atom_condition: "(" condition ")"
                   | comparison
                   | "true"              -> true
                   | "false"             -> false

    ?comparison: expr "==" expr          -> eq
               | expr "!=" expr          -> neq
               | expr ">" expr           -> gt
               | expr ">=" expr          -> gte
               | expr "<" expr           -> lt
               | expr "<=" expr          -> lte
               | expr                    -> expr_condition

    ?expr: term
         | expr "+" term                 -> add
         | expr "-" term                 -> sub

    ?term: factor
         | term "*" factor               -> mul
         | term "/" factor               -> div

    ?factor: NUMBER                      -> number
           | NAME                        -> var
           | "-" factor                  -> neg
           | "(" expr ")"                -> paren_expr

    channel: CNAME
    CNAME: /[A-Z][a-zA-Z0-9_]*/
    NAME: /[a-z][a-zA-Z0-9_]*/
    NUMBER: /[0-9]+/

    %import common.WS
    %ignore WS
"""


class TreeToCode(Transformer):
    def start(self, items):
        return items[0]

    def sequence_stmt(self, items):
        return f"{items[0]}; {items[1]}"

    def skip(self, _items):
        return "skip"

    def assign_stmt(self, items):
        return f"{items[0]} := {items[1]}"

    def send(self, items):
        return f"{items[0]}!{items[1]}"

    def recv(self, items):
        return f"{items[0]}?{items[1]}"

    def if_stmt(self, items):
        commands = " ".join(items)
        return f"if {commands} fi"

    def do_stmt(self, items):
        commands = " ".join(items)
        return f"do {commands} od"

    def guarded_command(self, items):
        return f":: {items[0]} -> {items[1]}"

    def atomic_stmt(self, items):
        return f"atomic {{ {'; '.join(items)} }}"

    def or_op(self, items):
        return f"({items[0]} || {items[1]})"

    def and_op(self, items):
        return f"({items[0]} && {items[1]})"

    def not_op(self, items):
        return f"!{items[0]}"

    def eq(self, items):
        return f"{items[0]} == {items[1]}"

    def neq(self, items):
        return f"{items[0]} != {items[1]}"

    def gt(self, items):
        return f"{items[0]} > {items[1]}"

    def gte(self, items):
        return f"{items[0]} >= {items[1]}"

    def lt(self, items):
        return f"{items[0]} < {items[1]}"

    def lte(self, items):
        return f"{items[0]} <= {items[1]}"

    def expr_condition(self, items):
        return str(items[0])

    def add(self, items):
        return f"{items[0]} + {items[1]}"

    def sub(self, items):
        return f"{items[0]} - {items[1]}"

    def mul(self, items):
        return f"{items[0]} * {items[1]}"

    def div(self, items):
        return f"{items[0]} / {items[1]}"

    def number(self, items):
        return str(items[0])

    def var(self, items):
        return str(items[0])

    def neg(self, items):
        return f"-{items[0]}"

    def paren_expr(self, items):
        return f"({items[0]})"

    def true(self, _items):
        return "true"

    def false(self, _items):
        return "false"

    def channel(self, items):
        return str(items[0])


class HashableTree(Tree):
    def __init__(self, data, children=None, meta=None):
        super().__init__(data, children if children is not None else [], meta)

    def __hash__(self):
        return hash((self.data, tuple(self.children)))

    def __eq__(self, other):
        return (
            isinstance(other, Tree)
            and self.data == other.data
            and self.children == other.children
        )


nano_promela_parser = Lark(
    NANO_PROMELA_GRAMMAR,
    start="start",
    parser="lalr",
    propagate_positions=True,
)
tree_to_code_transformer = TreeToCode()


def freeze_tree(node):
    if isinstance(node, Tree):
        return HashableTree(
            node.data,
            [freeze_tree(child) for child in node.children],
            node.meta,
        )
    return node


def tree_to_code(tree):
    if tree == EXIT_LOCATION:
        return "exit"
    return tree_to_code_transformer.transform(tree)


def sub(tree):
    if tree.data == "start":
        return sub(tree.children[0])

    if tree.data in {"assign_stmt", "recv", "send", "atomic_stmt", "skip"}:
        return {
            HashableTree(tree.data, tree.children, tree.meta),
            EXIT_LOCATION,
        }

    if tree.data == "sequence_stmt":
        first_set = {
            HashableTree("sequence_stmt", [sub_stmt, tree.children[1]], tree.meta)
            for sub_stmt in sub(tree.children[0])
            if sub_stmt != EXIT_LOCATION
        }
        return first_set | sub(tree.children[1])

    if tree.data == "if_stmt":
        subtree_results = {
            location
            for guarded_command in tree.children
            for location in sub(guarded_command.children[1])
        }
        return {HashableTree(tree.data, tree.children)} | subtree_results

    if tree.data == "do_stmt":
        loop_location = HashableTree(tree.data, tree.children, tree.meta)
        subtree_results = {
            HashableTree(
                "sequence_stmt",
                [sub_stmt, loop_location],
                getattr(sub_stmt, "meta", tree.meta),
            )
            for guarded_command in tree.children
            for sub_stmt in sub(guarded_command.children[1])
            if sub_stmt != EXIT_LOCATION
        }
        return {loop_location, EXIT_LOCATION} | subtree_results

    raise ValueError(f"Unsupported NanoPromela node: {tree.data}")


class TransitionBuilder:
    def get_transitions(self, location_from, location_to):
        if location_from == EXIT_LOCATION:
            return set()

        handler = getattr(
            self,
            f"handle_{location_from.data}",
            self.handle_default,
        )
        return handler(location_from, location_to)

    def handle_default(self, _location_from, _location_to):
        return set()

    def handle_assign_stmt(self, location_from, location_to):
        if location_to == EXIT_LOCATION:
            return {("true", tree_to_code(location_from))}
        return set()

    def handle_recv(self, location_from, location_to):
        return self.handle_assign_stmt(location_from, location_to)

    def handle_send(self, location_from, location_to):
        return self.handle_assign_stmt(location_from, location_to)

    def handle_atomic_stmt(self, location_from, location_to):
        return self.handle_assign_stmt(location_from, location_to)

    def handle_skip(self, location_from, location_to):
        return self.handle_assign_stmt(location_from, location_to)

    def handle_sequence_stmt(self, location_from, location_to):
        if (
            location_to != EXIT_LOCATION
            and isinstance(location_to, Tree)
            and location_to.data == "sequence_stmt"
            and location_from.children[1] == location_to.children[1]
        ):
            return self.get_transitions(location_from.children[0], location_to.children[0])

        if location_from.children[1] == location_to:
            return self.get_transitions(location_from.children[0], EXIT_LOCATION)

        return set()

    def handle_if_stmt(self, location_from, location_to):
        result = set()
        for guarded_command in location_from.children:
            guard = tree_to_code(guarded_command.children[0])
            sub_transitions = self.get_transitions(guarded_command.children[1], location_to)
            for sub_guard, action in sub_transitions:
                combined_guard = f"{sub_guard} && {guard}" if sub_guard != "true" else guard
                result.add((combined_guard, action))
        return result

    def handle_do_stmt(self, location_from, location_to):
        result = set()

        if (
            isinstance(location_to, Tree)
            and location_to.data == "sequence_stmt"
            and location_to.children[1] == location_from
        ):
            for guarded_command in location_from.children:
                guard = tree_to_code(guarded_command.children[0])
                sub_transitions = self.get_transitions(
                    guarded_command.children[1],
                    location_to.children[0],
                )
                for sub_guard, action in sub_transitions:
                    combined_guard = f"{sub_guard} && {guard}" if sub_guard != "true" else guard
                    result.add((combined_guard, action))
            return result

        if location_to == location_from:
            for guarded_command in location_from.children:
                guard = tree_to_code(guarded_command.children[0])
                sub_transitions = self.get_transitions(
                    guarded_command.children[1],
                    EXIT_LOCATION,
                )
                for sub_guard, action in sub_transitions:
                    combined_guard = f"{sub_guard} && {guard}" if sub_guard != "true" else guard
                    result.add((combined_guard, action))
            return result

        if location_to == EXIT_LOCATION:
            negated_guards = " && ".join(
                f"!({tree_to_code(guarded_command.children[0])})"
                for guarded_command in location_from.children
            )
            return {(negated_guards, "skip")}

        return result


def _location_sort_key(location):
    return (location == EXIT_LOCATION, tree_to_code(location))


def reachable_program_graph(code):
    if not isinstance(code, str) or not code.strip():
        raise ValueError("NanoPromela code must be a non-empty string.")

    root = freeze_tree(nano_promela_parser.parse(code))
    builder = TransitionBuilder()

    visited = set()
    worklist = deque([root])
    ordered_locations = []
    discovered_exit = False
    transitions = set()

    while worklist:
        location_from = worklist.popleft()
        if location_from in visited:
            continue

        visited.add(location_from)
        ordered_locations.append(location_from)

        candidate_targets = sorted(sub(location_from), key=_location_sort_key)
        for location_to in candidate_targets:
            candidate_transitions = sorted(
                builder.get_transitions(location_from, location_to),
                key=lambda item: (item[0], item[1]),
            )
            for guard, action in candidate_transitions:
                transitions.add((location_from, guard, action, location_to))

            if location_to == EXIT_LOCATION and candidate_transitions:
                discovered_exit = True
            elif (
                location_to != EXIT_LOCATION
                and candidate_transitions
                and location_to not in visited
                and location_to not in worklist
            ):
                worklist.append(location_to)

    if discovered_exit:
        ordered_locations.append(EXIT_LOCATION)

    return root, ordered_locations, sorted(
        transitions,
        key=lambda item: (
            tree_to_code(item[0]),
            tree_to_code(item[3]),
            item[1],
            item[2],
        ),
    )


def _state_width(text, short_names):
    if short_names:
        return max(68, min(108, 24 + len(text) * 9))
    return max(120, min(520, 24 + len(text) * 7))


def _anchor_position(location):
    if location == EXIT_LOCATION:
        return None, None
    if isinstance(location, Tree) and location.data == "sequence_stmt":
        return _anchor_position(location.children[0])
    meta = getattr(location, "meta", None)
    line = getattr(meta, "line", None)
    column = getattr(meta, "column", None)
    if line is not None and column is not None:
        return int(line), int(column)
    if isinstance(location, Tree) and location.children:
        for child in location.children:
            child_line, child_column = _anchor_position(child)
            if child_line is not None and child_column is not None:
                return child_line, child_column
    return None, None


def _action_dimensions(label_text):
    lines = label_text.split("<br>")
    longest_line = max((len(line) for line in lines), default=0)
    width = max(70, min(280, 24 + longest_line * 7))
    height = 24 + max(0, len(lines) - 1) * 14
    return width, height


def _curve_values(count, base=0.0, step=0.18):
    if count <= 1:
        return [base]
    midpoint = (count - 1) / 2
    return [round(base + (index - midpoint) * step, 2) for index in range(count)]


def _same_side_curve_values(count, start=0.16, step=0.14):
    return [round(start + index * step, 2) for index in range(count)]


def _loop_directions(count):
    defaults = ["-90deg", "-35deg", "20deg", "75deg", "130deg", "185deg"]
    if count <= len(defaults):
        return defaults[:count]
    return [f"{-90 + index * (360 / count):.0f}deg" for index in range(count)]


def nanopromela_to_pg_slidev_data(code):
    root, ordered_locations, transitions = reachable_program_graph(code)

    short_names = {}
    for index, location in enumerate(ordered_locations, start=1):
        full_text = tree_to_code(location)
        short_text = "exit" if location == EXIT_LOCATION else f"L{index}"
        if location == EXIT_LOCATION:
            short_text = "exit"
        short_names[location] = short_text

    state_ids = {location: f"loc_{index}" for index, location in enumerate(ordered_locations)}

    states = []
    for location in ordered_locations:
        full_text = tree_to_code(location)
        is_exit = location == EXIT_LOCATION
        anchor_line, anchor_column = _anchor_position(location)
        states.append({
            "id": state_ids[location],
            "shortText": short_names[location],
            "fullText": full_text,
            "shortWidth": _state_width(short_names[location], True),
            "fullWidth": _state_width(full_text, False),
            "anchorLine": anchor_line,
            "anchorColumn": anchor_column,
            "initial": location == root,
            "initialDirection": "top",
            "color": "#fef3c7" if is_exit else "#f8fafc",
            "stroke": "#b45309" if is_exit else "#334155",
            "strokeWidth": 2,
        })

    grouped_transitions = defaultdict(list)
    for source, guard, action, target in transitions:
        grouped_transitions[(state_ids[source], state_ids[target])].append({
            "source": state_ids[source],
            "target": state_ids[target],
            "guard": guard,
            "actionName": action,
            "label": f"{guard}<br>: {action}",
        })

    graph_transitions = []
    for (source_id, target_id), items in grouped_transitions.items():
        reverse_exists = (target_id, source_id) in grouped_transitions and source_id != target_id

        if source_id == target_id:
            for item, loop_direction in zip(items, _loop_directions(len(items))):
                action_width, action_height = _action_dimensions(item["label"])
                graph_transitions.append({
                    "source": item["source"],
                    "target": item["target"],
                    "action": item["label"],
                    "actionWidth": action_width,
                    "actionHeight": action_height,
                    "actionFontSize": 10,
                    "loopDirection": loop_direction,
                    "loopRadius": 96,
                    "loopLabelRadius": 84,
                    "stroke": "#334155",
                    "strokeWidth": 2,
                })
            continue

        curves = _same_side_curve_values(len(items)) if reverse_exists else _curve_values(len(items))

        for item, curve in zip(items, curves):
            action_width, action_height = _action_dimensions(item["label"])
            transition = {
                "source": item["source"],
                "target": item["target"],
                "action": item["label"],
                "actionWidth": action_width,
                "actionHeight": action_height,
                "actionFontSize": 10,
                "stroke": "#334155",
                "strokeWidth": 2,
            }
            if curve != 0:
                transition["curve"] = curve
            graph_transitions.append(transition)

    return {
        "states": states,
        "transitions": graph_transitions,
        "summary": {
            "states": len(states),
            "transitions": len(graph_transitions),
            "initial": 1,
        },
    }
