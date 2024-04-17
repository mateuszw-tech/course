import json
import requests
from datetime import date
import os
from tkinter import messagebox
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfilename
import customtkinter as ctk


class ManagerGUI:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root = ctk.CTk()
        self.root.title("responseGUI 1.0")
        self.root.iconbitmap("images/nerd.ico")
        self.root.geometry("1080x720")
        self.websites_frame = ctk.CTkFrame(master=self.root)
        self.websites_button_frame = ctk.CTkFrame(master=self.websites_frame)
        self.response_frame = ctk.CTkFrame(master=self.root)
        self.response_button_frame = ctk.CTkFrame(master=self.response_frame)
        self.websites_path = ""
        self.response_index = 0

    def initialize_ui(self):

        WebContentUtils.ensure_settings_saved_to_file()
        self.websites_frame.pack(pady=25, padx=60, fill="both", side=TOP, expand=True)
        self.websites_button_frame.pack(fill="x", expand=False, side=TOP)

        button_left = ctk.CTkButton(
            master=self.websites_button_frame,
            text="load",
            command=lambda: self.load_filename(websites_label),
        )
        button_left.pack(padx=0, side=LEFT)
        button_right = ctk.CTkButton(
            master=self.websites_button_frame,
            text="save to file",
            command=lambda: WebContentUtils.pull_websites_content_to_archive_file(self.websites_path),
        )
        button_right.pack(padx=0, side=RIGHT)
        button_right = ctk.CTkButton(
            master=self.websites_button_frame,
            text="delete",
            command=lambda: self.delete_website_from_file(websites_label),
        )
        button_right.pack(padx=10, side=RIGHT)
        button_middle = ctk.CTkButton(
            master=self.websites_button_frame,
            text="add",
            command=lambda: self.add_website_url(websites_label),
        )
        button_middle.pack(padx=0, side=RIGHT)

        websites_label = ctk.CTkLabel(
            master=self.websites_frame,
            width=300,
            text="No websites file",
            justify="center",
        )
        websites_label.pack(expand=True)

        self.response_frame.pack(pady=25, padx=60, fill="both", side=BOTTOM, expand=True)

        self.response_button_frame.pack(fill="x", expand=False, side=TOP)
        button_left = ctk.CTkButton(
            master=self.response_button_frame,
            text="<-",
            command=lambda: self.change_response_index(TRUE, response_label, file_name_label),
        )

        file_name_label = ctk.CTkLabel(
            master=self.response_button_frame,
            text=WebContentUtils.load_current_file_name(self.response_index),
            justify="center",
        )

        button_right = ctk.CTkButton(
            master=self.response_button_frame,
            text="->",
            command=lambda: self.change_response_index(FALSE, response_label, file_name_label),
        )
        button_left.pack(side=LEFT)
        button_right.pack(side=RIGHT)
        file_name_label.pack()

        response_label = ctk.CTkLabel(
            master=self.response_frame,
            width=300,
            text=WebContentUtils.load_responses_from_archive_files(self.response_index),
            justify="center",
        )
        response_label.pack(expand=True)

        self.root.mainloop()

    def add_website_url(self, website_file_label: ctk.CTkLabel) -> None:
        try:
            WebContentUtils.add_website_entry_to_chosen_file(self.websites_path,
                                                             WebContentUtils.get_website_entry_url()),
            WebContentUtils.configure_path(self.websites_path, website_file_label)
        except FileNotFoundError as e:
            messagebox.showinfo("Opps!", f"It looks like file websites is missing \n {e}")

    def delete_website_from_file(self, website_file_label: ctk.CTkLabel) -> None:
        try:
            WebContentUtils.delete_website_entry_from_file(self.websites_path),
            WebContentUtils.configure_path(self.websites_path, website_file_label)
        except FileNotFoundError as e:
            messagebox.showinfo("Opps!", f"{e}")

    def load_filename(self, website_file_label: ctk.CTkLabel) -> None:
        self.websites_path = WebContentUtils.return_websites_entries_filename()
        WebContentUtils.configure_path(self.websites_path, website_file_label)

    def change_response_index(
            self, left_direction: bool, content_label: ctk.CTkLabel, file_name_label: ctk.CTkLabel
    ) -> None:
        if left_direction:
            if self.response_index >= 0:
                self.response_index -= 1
            else:
                self.response_index = len(WebContentUtils.get_response_files_from_archive_folder()) - 1
        else:
            if self.response_index < (len(WebContentUtils.get_response_files_from_archive_folder()) - 1):
                self.response_index += 1
            else:
                self.response_index = 0

        content_label.configure(text=WebContentUtils.load_responses_from_archive_files(self.response_index))
        file_name_label.configure(text=WebContentUtils.load_current_file_name(self.response_index))


class WebContentUtils:
    @staticmethod
    def ensure_settings_saved_to_file() -> None:
        settings = [{"archive_dir": "path/to/archive/dir"}]
        if os.path.exists('settings.json'):
            return
        with open("settings.json", "w") as f:
            json.dump(
                settings,
                f,
                indent=1,
            )

    @staticmethod
    def _save_websites_data_to_file(
            data: list = None,  # dodać [type]
    ) -> None:
        number = 0
        file_path = "archive/archive.json"
        directory = "archive"
        is_dir_exist = os.path.exists(directory)
        if not is_dir_exist:
            os.makedirs(directory)
        while os.path.exists(file_path):
            number += 1
            file_path = f"archive/archive{number}.json"
        with open(file_path, "w") as f:
            json.dump(
                data,
                f,
                indent=1,
            )

    @staticmethod
    def return_website_list_as_string(path: str) -> str:
        websites_list = open(path, "r").read().split("\n")
        return "\n".join(websites_list)

    @staticmethod
    def return_websites_entries_filename() -> str:
        filename = askopenfilename(
            initialdir="C:\\Users\\learn_python()\\PycharmProjects\\course\\section_1\\responseGuiApplication",
            filetypes=(("Text files", "*.json"), ("all files", "*.*")),
        )
        return filename

    @staticmethod
    def configure_path(filename, label) -> None:  # Jak to zmienić?
        label.configure(text=WebContentUtils.return_website_list_as_string(filename))

    @staticmethod
    def pull_websites_content_to_archive_file(filename: str) -> None:
        try:
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
        except FileNotFoundError as e:
            messagebox.showinfo("Opps!", f"{e}")
        except ConnectionError as e:
            messagebox.showinfo("Opps!", f"{e}")

    @staticmethod
    def get_website_entry_url() -> str:
        website_string = askstring("Website URL", "Enter website URL")
        return website_string

    @staticmethod
    def add_website_entry_to_chosen_file(filepath: str, website: str) -> None:
        last_index = 0
        with open(filepath, "r") as file:
            lines = file.readlines()
        for index, element in enumerate(lines):
            last_index = index
        # Handling difficult line endings
        if last_index > 1:
            lines.append("\n" + website)
        elif last_index == 1:
            lines.append(website)
        else:
            lines.append(website + "\n")
        with open(filepath, "w") as file:
            file.writelines(lines)

    @staticmethod
    def delete_website_entry_from_file(filepath: str) -> None:
        with open(filepath, "r") as file:
            lines = file.readlines()[:-1]
        with open(filepath, "w") as file:
            last_index = 0
            for index, element in enumerate(lines):
                last_index = index
            i = 0
            for line in lines:
                if i != last_index:
                    file.write(line)
                    i += 1
                else:
                    file.write(line.strip())

    @staticmethod
    def get_response_files_from_archive_folder() -> list:
        files = []
        directory = "archive"
        is_dir_exists = os.path.exists(directory)
        if is_dir_exists:  # Skrócić if elsa
            for file in os.listdir("archive"):
                if file.endswith(".json"):
                    files.append(file)
            return files
        else:
            os.makedirs(directory)
            for file in os.listdir("archive"):
                if file.endswith(".json"):
                    files.append(file)
            return files

    @staticmethod
    def load_current_file_name(index) -> str:
        try:
            return f"{WebContentUtils.get_response_files_from_archive_folder()[index]}"
        except IndexError:
            return "No files"

    @staticmethod
    def load_responses_from_archive_files(index: int, directory="archive") -> str:
        try:
            f = open(f"{directory}/{WebContentUtils.get_response_files_from_archive_folder()[index]}", "r")
            elements = json.load(f)
            response = []
            for element in elements:
                response.append(f"{element['Date']} - {element['Address']} - {element['Content']}")
            return "\n".join(response)

        except IndexError:
            return "No files"
