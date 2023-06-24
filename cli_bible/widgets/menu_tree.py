from textual.widgets import Tree


class MenuTree(Tree):
    """Opciones para leer"""

    BINDINGS = [
        ("j, down", "cursor_down", ""),
        ("k, up", "cursor_up", ""),
        ("l, h, enter", "select_cursor", ""),
        ("space", "toggle_node", ""),
    ]
