from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from ..widgets import MARKDOWN_EXAMPLE, MenuTree, MyContent


class Main(Screen):
    """Pantalla principal"""

    BINDINGS = [
        ("q", "app.quit", "Quit"),
        ("t", "toggle_table_of_contents", "TOC"),
        ("b", "back", "Back"),
        ("f", "forward", "Forward"),
    ]

    def compose(self) -> ComposeResult:
        yield Header("Read the Bible")
        yield Footer()
        menu_tree: MenuTree[dict] = MenuTree("Leer la Biblia")
        menu_tree.root.expand()
        plan_activo = menu_tree.root.add("Plan Activo", expand=True)
        planes_disponibles = menu_tree.root.add("Planes Disponibles", expand=True)
        planes_disponibles.add_leaf("Secuencial")
        planes_disponibles.add_leaf("Antiguo y Nuevo Testamento")
        with Horizontal():
            yield menu_tree
            yield MyContent(MARKDOWN_EXAMPLE, id="viewer", show_table_of_contents=False)

    @property
    def markdown_viewer(self) -> MyContent:
        return self.query_one(MyContent)

    def action_toggle_table_of_contents(self) -> None:
        self.markdown_viewer.show_table_of_contents = (
            not self.markdown_viewer.show_table_of_contents
        )

    def action_back(self) -> None:
        self.markdown_viewer.action_page_up()

    def action_forward(self) -> None:
        self.markdown_viewer.action_page_down()
