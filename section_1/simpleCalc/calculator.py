import tkinter


class CalculatorUtils:
    @staticmethod
    def calculate(operator: str, first, second):
        if operator == "+":
            return first + second
        elif operator == "-":
            return first - second
        elif operator == "*":
            return first * second
        elif operator == "/":
            return first / second
        elif operator == "^":
            return first**second


class CalculatorApp:
    def __init__(self, window, title: str):
        self.window = window
        self.window.title(title)
        self.window.geometry("500x600")
        self.window.configure(bg="#0D1B2A")
        self.frame = tkinter.Frame(self.window, bg="#0D1B2A")

    def display_app(self):
        def result(operator: str):
            result_label.config(
                text=CalculatorUtils.calculate(operator, int(first_number.get()), int(second_number.get()))
            )

        name_label = tkinter.Label(
            self.frame,
            text="Simple Calculator by Matthew",
            bg="#0D1B2A",
            fg="#415A77",
            font=("Arial", 20),
        )
        first_number = tkinter.Entry(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=20,
            justify="center",
            font=("Arial", 20),
        )
        second_number = tkinter.Entry(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=20,
            justify="center",
            font=("Arial", 20),
        )
        result_label = tkinter.Label(self.frame, text="2", bg="#0D1B2A", fg="#415A77", font=("Arial", 20))

        add_button = tkinter.Button(
            self.frame,
            text="+",
            bg="#0D1B2A",
            fg="#415A77",
            width=10,
            font=("Arial", 15),
            command=lambda: result("+"),
        )
        subtract_button = tkinter.Button(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=10,
            font=("Arial", 15),
            text="-",
            command=lambda: result("-"),
        )
        multiply_button = tkinter.Button(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=10,
            font=("Arial", 15),
            text="*",
            command=lambda: result("*"),
        )
        divide_button = tkinter.Button(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=10,
            font=("Arial", 15),
            text="/",
            command=lambda: result("/"),
        )
        power_button = tkinter.Button(
            self.frame,
            bg="#0D1B2A",
            fg="#415A77",
            width=10,
            font=("Arial", 15),
            text="^",
            command=lambda: result("^"),
        )

        name_label.pack(pady=10)
        result_label.pack(pady=10)
        first_number.pack(ipady=3, pady=10)
        second_number.pack(ipady=3, pady=10)
        for button in (
            add_button,
            subtract_button,
            multiply_button,
            divide_button,
            power_button,
        ):
            button.pack(pady=10)

        self.frame.pack()
        self.window.mainloop()
