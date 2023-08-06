from sprocket.util.common import repo_root


class Loader:
    def __init__(self):
        self.success = False

    def __bool__(self):
        return self.success

    def load(self, filename):
        filepath = repo_root("data", "text", filename)
        try:
            self.raw = open(filepath, "r").read()
            self.success = True
        except FileNotFoundError:
            self.success = False
            print("File not found")
