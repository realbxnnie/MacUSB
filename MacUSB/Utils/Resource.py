from os import path

class Resource():
    def __init__(self, file):
        Path = None
        try:
            Path = __import__("sys")._MEIPASS
        except Exception:
            Path = path.join(".")

        self.content = path.join(Path, file)
