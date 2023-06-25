import sys

from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Header

from ..modules import Config, FilesToWalk
from ..widgets import MARKDOWN_CONTENT, MenuTree, MyContent


class Main(Screen):
    """Pantalla principal"""

    BINDINGS = [
        ("q", "app.quit", "Quit"),
        ("t", "toggle_table_of_contents", "TOC"),
        ("b", "back", "Back"),
        ("f", "forward", "Forward"),
        ("n", "load_next", "Next Chapter"),
        ("p", "load_previous", "Previous Chapter"),
    ]

    config = Config()
    work_directory = "/home/felipe/dev/cli-bible/files/rv1960"
    actual_file = 1
    list_files = FilesToWalk(work_directory)
    total_files = len(list_files.files)

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
            yield MyContent(
                self.list_files.files[self.actual_file],
                id="viewer",
                show_table_of_contents=False,
            )

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

    async def load_chapter(self) -> None:
        """load self.actual_file"""
        file_to_load = str(
            f"{self.work_directory}/{self.list_files.files[self.actual_file]}"
        )
        if not await self.markdown_viewer.go(file_to_load):
            sys.exit(1)

    async def action_load_next(self) -> None:
        """Cargar el siguiente capítulo"""

        if self.actual_file < self.total_files - 1:
            self.actual_file += 1
        else:
            self.actual_file = 0

        await self.load_chapter()

    async def action_load_previous(self) -> None:
        """Cargar el archivo previo"""

        if self.actual_file > 1:
            self.actual_file -= 1
        else:
            self.actual_file = self.total_files

        await self.load_chapter()
