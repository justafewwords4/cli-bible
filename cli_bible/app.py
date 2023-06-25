from textual.app import App

from .screens import Main


class ReadTheBible(App[None]):
    """La aplicación de la biblia"""

    SCREENS = {
        "main": Main,
    }

    TITLE = "Read the Bible"
    CSS_PATH = "biblia.css"

    def on_mount(self) -> None:
        """Montar la pantalla principal"""
        self.push_screen(Main())


def run():
    """Ejecutar la app"""
    app = ReadTheBible()
    app.run()
