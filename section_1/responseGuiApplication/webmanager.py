import json
import webbrowser

import requests
from datetime import date
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
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


class WebContentUtils:

    @staticmethod
    def _save_websites_data_to_file(
            data: list = None,
    ) -> None:
        number = 0
        file_path = "archive/archive.txt"
        while os.path.exists(file_path):
            number += 1
            file_path = f"archive/archive{number}.txt"
        with open(file_path, "w") as f:
            json.dump(
                data,
                f,
                indent=1,
            )

    @staticmethod
    def return_website_list_as_string(path) -> str:
        websites_list = open(path, "r").read().split("\n")
        return "\n".join(websites_list)

    @staticmethod
    def return_filename() -> str:
        filename = askopenfilename(
            initialdir="C:\\Users\\learn_python()\\PycharmProjects\\course\\section_1\\responseGuiApplication",
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")),
        )
        return filename

    @staticmethod
    def configure_path(filename, label) -> None:
        label.configure(text=WebContentUtils.return_website_list_as_string(filename))

    @staticmethod
    def pull_websites_content(
            filename: str
    ) -> None:
        data: list = []
        for website in open(filename, "r").read().split("\n"):
            response = requests.get(website)
            data.append(
                {
                    "Date": str(date.today()),
                    "Address": website,
                    "Content": str(response),
                }
            )
        WebContentUtils._save_websites_data_to_file(data)


class ManagerGUI:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title("responseGUI")
        self.root.iconbitmap("images/nerd.ico")
        self.root.geometry("1080x720")
        self.websites_frame = ctk.CTkFrame(master=self.root)
        self.websites_button_frame = ctk.CTkFrame(master=self.websites_frame)
        self.response_frame = ctk.CTkFrame(master=self.root)
        self.response_button_frame = ctk.CTkFrame(master=self.response_frame)
        self.filename = ""

    def display_menu(self):
        self.websites_frame.pack(pady=25, padx=60, fill="both", side=TOP, expand=True)

        self.websites_button_frame.pack(fill="x", expand=False, side=TOP)
        button_left = ctk.CTkButton(
            master=self.websites_button_frame, text="load",
            command=lambda: WebContentUtils().configure_path(WebContentUtils.return_filename(), websites_label)
        )
        button_left.pack(padx=0, side=LEFT)
        button_right = ctk.CTkButton(master=self.websites_button_frame, text="save to file",
                                     command=lambda: WebContentUtils.pull_websites_content(
                                         WebContentUtils.return_filename()))
        button_right.pack(padx=0, side=RIGHT)
        button_right = ctk.CTkButton(master=self.websites_button_frame, text="delete")
        button_right.pack(padx=10, side=RIGHT)
        button_middle = ctk.CTkButton(master=self.websites_button_frame, text="add")
        button_middle.pack(padx=0, side=RIGHT)

        websites_label = ctk.CTkLabel(
            master=self.websites_frame,
            width=300,
            text="No websites file",
            justify="center"
        )
        websites_label.pack(expand=False, fill="x", side=TOP)

        self.response_frame.pack(
            pady=25, padx=60, fill="both", side=BOTTOM, expand=True
        )

        self.response_button_frame.pack(fill="x", expand=False, side=TOP)
        button_left = ctk.CTkButton(master=self.response_button_frame, text="<-")
        button_left.pack(side=LEFT)
        button_right = ctk.CTkButton(master=self.response_button_frame, text="->")
        button_right.pack(side=RIGHT)

        self.root.mainloop()
