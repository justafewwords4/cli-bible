from .modules import Config


def run():
    """Ejecutar la app"""
    print("Estamos en la app")
    config = Config()
    print(config)
