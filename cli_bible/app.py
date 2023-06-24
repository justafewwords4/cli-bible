from textual.app import App

from .modules import Config
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
        self.push_screen("main")


def run():
    """Ejecutar la app"""
    print("Estamos en la app")
    config = Config()
    print(config)
    app = ReadTheBible()
    app.run()
