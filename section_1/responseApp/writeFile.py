import json
import requests
from datetime import date
import os


class WriteFile:
    def __init__(self, websites):
        self.file_name = 'archive'
        self.number = 0
        self.websites = websites

    def write_json_file(self):
        file_path = f'archive/{self.file_name}.txt'
        while os.path.exists(file_path):
            self.number += 1
            file_path = f'archive/{self.file_name}{self.number}.txt'

        data = []
        for website in self.websites:
            response = requests.get(website)
            data.append({'Date': str(date.today()),
                         'Address': website,
                         'Content': str(response)})

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=1)
