import os


class Loader:
    def __init__(self):
        self.success = False

    def __bool__(self):
        return self.success

    def load(self, filename):
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            self.raw = open(filepath, "r").read()
            self.success = True
        except FileNotFoundError:
            self.success = False
            print("File not found")
