import os
import sys
from pathlib import Path

import yaml
from rich import print


class Config:
    """Maneja la configuración de la app"""

    home_user = Path.home()
    config_file = home_user.joinpath(".clibib.yaml")
    default_config = {"work_directory": str(home_user.joinpath("clibib"))}
    work_directory = ""

    def __init__(self) -> None:
        """llamar read_yaml"""
        self.load_config_file()
        if self.work_directory.endswith("/"):
            self.work_directory = self.__replace_last(self.work_directory, "/", "")

    def __str__(self):
        """imprimir la configuración"""
        return f"\tDirectorio del usuario: {self.home_user}\n\tArchivo de configuración: {self.config_file}\n\tWork Directory: {self.work_directory}"

    def __replace_last(self, string, old, new):
        return new.join(string.rsplit(old, 1))

    def load_config_file(self) -> dict:
        """leer archivo de configuración"""
        try:
            with open(self.config_file, "r") as ff:
                documents = yaml.safe_load(ff)
            if "work_directory" in documents:
                self.work_directory = documents["work_directory"]
            else:
                print(
                    "No existe un directorio de trabajo en el archivo de configuración"
                )
                print(f"Modifique {self.config_file} y corrija el error")
                sys.exit(1)
        except FileNotFoundError:
            print("Archivo no encontrado")
            print("Creando archivo de configuración")
            self.create_config_file()

        # DONE: Comprobar si existe el directorio de trabajo
        if not os.path.exists(self.work_directory):
            try:
                os.makedirs(self.work_directory)
            except PermissionError:
                print("Error de permisos al crear directorio de trabajo")
                sys.exit()

    def create_config_file(self) -> dict:
        """crear el archivo de configuración"""
        try:
            with open(self.config_file, "w") as ff:
                documents = yaml.dump(self.default_config, ff)
                self.work_directory = self.default_config["work_directory"]
            return documents
        except PermissionError:
            print("Error de permisos")
            sys.exit(1)

    def is_work_directory_ok(self) -> None:
        """Verifica si existe el directorio de trabajo"""
        pass
