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
        self.filename = ""
        self.response_index = 0

    def display_menu(self):
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
            command=lambda: WebContentUtils.pull_websites_content(self.filename),
        )
        button_right.pack(padx=0, side=RIGHT)
        button_right = ctk.CTkButton(master=self.websites_button_frame, text="delete",
                                     command=lambda: self.delete_button_action(websites_label))
        button_right.pack(padx=10, side=RIGHT)
        button_middle = ctk.CTkButton(
            master=self.websites_button_frame,
            text="add",
            command=lambda: self.add_button_action(websites_label),
        )
        button_middle.pack(padx=0, side=RIGHT)

        websites_label = ctk.CTkLabel(
            master=self.websites_frame,
            width=300,
            text="No websites file",
            justify="center",
        )
        websites_label.pack(expand=True)

        self.response_frame.pack(
            pady=25, padx=60, fill="both", side=BOTTOM, expand=True
        )

        self.response_button_frame.pack(fill="x", expand=False, side=TOP)
        button_left = ctk.CTkButton(
            master=self.response_button_frame,
            text="<-",
            command=lambda: self.change_response_index("Left", response_label, file_name_label),
        )

        file_name_label = ctk.CTkLabel(
            master=self.response_button_frame,
            text=WebContentUtils.load_file_name(self.response_index),
            justify="center",
        )

        button_right = ctk.CTkButton(
            master=self.response_button_frame,
            text="->",
            command=lambda: self.change_response_index("Right", response_label, file_name_label),
        )
        button_left.pack(side=LEFT)
        button_right.pack(side=RIGHT)
        file_name_label.pack()

        response_label = ctk.CTkLabel(
            master=self.response_frame,
            width=300,
            text=WebContentUtils.load_response(self.response_index),
            justify="center",
        )
        response_label.pack(expand=True)

        self.root.mainloop()

    def add_button_action(self, label):
        try:
            WebContentUtils.add_website(self.filename, WebContentUtils.get_website_name()),
            WebContentUtils.configure_path(self.filename, label)
        except FileNotFoundError as e:
            messagebox.showinfo("Opps!", f"{e}")

    def delete_button_action(self, label):
        try:
            WebContentUtils.delete_website(self.filename),
            WebContentUtils.configure_path(self.filename, label)
        except FileNotFoundError as e:
            messagebox.showinfo("Opps!", f"{e}")

    def load_filename(self, label):
        self.filename = WebContentUtils.return_filename()
        WebContentUtils.configure_path(self.filename, label)

    def change_response_index(self, direction: str, label, second_label):
        if direction == "Left":
            if self.response_index >= 0:
                self.response_index -= 1
            else:
                self.response_index = len(WebContentUtils.get_response_files()) - 1
        elif direction == "Right":
            if self.response_index < (len(WebContentUtils.get_response_files()) - 1):
                self.response_index += 1
            else:
                self.response_index = 0

        label.configure(text=WebContentUtils.load_response(self.response_index))
        second_label.configure(text=WebContentUtils.load_file_name(self.response_index))


class WebContentUtils:

    @staticmethod
    def _save_websites_data_to_file(
            data: list = None,  # dodać [type]
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
    def pull_websites_content(filename: str) -> None:
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
    def get_website_name() -> str:
        website_string = askstring("Website URL", "Enter website URL")
        return website_string

    @staticmethod
    def add_website(filepath: str, website: str) -> None:
        last_index = 0
        with open(filepath, "r") as file:
            lines = file.readlines()
        for index, element in enumerate(lines):
            last_index = index
        if last_index > 1:
            lines.append("\n" + website)
        elif last_index == 1:
            lines.append(website)
        else:
            lines.append(website + "\n")
        with open(filepath, "w") as file:
            file.writelines(lines)

    @staticmethod
    def delete_website(filepath: str) -> None:
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
    def get_response_files() -> list:
        files = []
        for file in os.listdir("archive"):
            if file.endswith(".txt"):
                files.append(file)
        return files

    @staticmethod
    def load_file_name(index):
        return f"{WebContentUtils.get_response_files()[index]}"

    @staticmethod
    def load_response(index):
        f = open(f"archive/{WebContentUtils.get_response_files()[index]}", "r")
        elements = json.load(f)
        test = ""
        response = []
        for element in elements:
            response.append(
                f"{element['Date']} - {element['Address']} - {element['Content']}"
            )
        return "\n".join(response)
