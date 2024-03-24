import json
import requests
from datetime import date
import os
from tkinter import *
import customtkinter as ctk


class WebContentManager:
    def __init__(
            self,
            path_to_archive_directory: str = None,
            websites_list_file_path: str = None,
    ):
        self.path_to_archive_directory: str = path_to_archive_directory
        self.websites_list_file_path: str = websites_list_file_path

    def _load_websites_data_from_file(self, file_path: str = None) -> list:
        f = open(f"{self.path_to_archive_directory}/{file_path}")
        return json.load(f)

    # return []

    def _save_websites_data_to_file(
            self,
            data: list = None,
    ) -> None:
        number: int = 0
        file_path = f"{self.path_to_archive_directory}/archive.txt"
        while os.path.exists(file_path):
            number += 1
            file_path = f"{self.path_to_archive_directory}/archive{number}.txt"
        with open(file_path, "w") as f:
            json.dump(
                data,
                f,
                indent=1,
            )

    def print_websites_data(
            self,
    ) -> None:
        for file in os.listdir(self.path_to_archive_directory):
            if file.endswith(".txt"):
                for element in self._load_websites_data_from_file(file):
                    print(
                        f"| {file} - {element['Date']} - {element['Address']} - {element['Content']}"
                    )

    def pull_websites_content(
            self,
    ) -> None:
        data: list = []
        websites_list = open(self.websites_list_file_path, "r").read().split("\n")
        for website in websites_list:
            response = requests.get(website)
            data.append(
                {
                    "Date": str(date.today()),
                    "Address": website,
                    "Content": str(response),
                }
            )
        self._save_websites_data_to_file(data)


class ManagerGUI:
    def __init__(self):
        pass

    def display_menu(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        root = ctk.CTk()

        root.title("test")
        root.iconbitmap("images/nerd.ico")
        root.geometry("1080x720")

        websites_frame = ctk.CTkFrame(master=root)
        websites_frame.pack(pady=0, padx=60, fill="x", side=TOP, expand=True)

        response_frame = ctk.CTkFrame(master=root)
        response_frame.pack(pady=25, padx=60, fill="both", side=BOTTOM, expand=True)

        button_frame = ctk.CTkFrame(master=response_frame)
        button_frame.pack(fill="x", expand=False, side=TOP)
        button_left = ctk.CTkButton(master=button_frame, text="<-")
        button_left.pack(side=LEFT)
        button_right = ctk.CTkButton(master=button_frame, text="->")
        button_right.pack(side=RIGHT)

        root.mainloop()
