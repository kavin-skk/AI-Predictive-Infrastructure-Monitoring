import json
import os


class CacheService:

    def __init__(self):

        self.file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "cache",
            "summary.json"
        )

    def save(self, data):

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):

        with open(self.file_path, "r") as f:
            return json.load(f)