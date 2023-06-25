import os


class FilesToWalk:
    """devuelve los archivos a recorrer"""

    files = []

    def __init__(self, directory: str) -> None:
        for root, dirs, files in os.walk(directory):
            for name in files:
                self.files.append(files)

        self.files = self.files[0]

    def clean_files(self):
        """limpia la lista de archivos"""
        self.files = []
