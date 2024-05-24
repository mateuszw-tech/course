import json
import os


class ReadFile:
    def __init__(self):
        self.file_name = "archive"
        self.number = 0

    def read_json_file(self):
        file_path = f"archive/{self.file_name}.txt"
        print("_______" * 20)
        while os.path.exists(file_path):
            f = open(file_path)
            data = json.load(f)
            for element in data:
                print(
                    f"| {self.file_name}{self.number}.txt - {element['Date']} - {element['Address']} - {element['Content']}"
                )
            print("_______" * 20)
            self.number += 1
            file_path = f"archive/{self.file_name}{self.number}.txt"
