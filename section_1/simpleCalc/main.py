import tkinter
import calculator

window = tkinter.Tk()
window.title("Simple Calculator")
window.geometry("500x600")
window.configure(bg='#0D1B2A')

frame = tkinter.Frame(bg='#0D1B2A')


def calculate(a):
    num_one = first_number.get()
    num_two = second_number.get()
    if num_one.isdigit() and num_two.isdigit():
        calc = calculator.Calculator(int(num_one), int(num_two))
        if a == 'add_button':
            result = calc.add()
        elif a == 'sub_button':
            result = calc.subtract()
        elif a == 'mul_button':
            result = calc.multiply()
        elif a == 'div_button':
            result = calc.divide()
        elif a == 'pow_button':
            result = calc.power()
        else:
            result = 0
    else:
        result = 'Both fields should be filled by numbers'
    result_label.config(text=result)


name_label = tkinter.Label(frame, text="Simple Calculator by Matthew", bg='#0D1B2A', fg="#415A77", font=("Arial", 20))
first_number = tkinter.Entry(frame, bg='#0D1B2A', fg="#415A77", width=20, justify='center', font=("Arial", 20))
second_number = tkinter.Entry(frame, bg='#0D1B2A', fg="#415A77", width=20, justify='center', font=("Arial", 20))
result_label = tkinter.Label(frame, text='2',
                             bg='#0D1B2A', fg="#415A77",
                             font=("Arial", 20))

add_button = tkinter.Button(frame, text="+", bg='#0D1B2A', fg="#415A77", width=10, font=("Arial", 15),
                            command=lambda: calculate('add_button'))
subtract_button = tkinter.Button(frame, bg='#0D1B2A', fg="#415A77", width=10, font=("Arial", 15), text="-",
                                 command=lambda: calculate('sub_button'))
multiply_button = tkinter.Button(frame, bg='#0D1B2A', fg="#415A77", width=10, font=("Arial", 15), text="*",
                                 command=lambda: calculate('mul_button'))
divide_button = tkinter.Button(frame, bg='#0D1B2A', fg="#415A77", width=10, font=("Arial", 15), text="/",
                               command=lambda: calculate('div_button'))
square_button = tkinter.Button(frame, bg='#0D1B2A', fg="#415A77", width=10, font=("Arial", 15), text="^",
                               command=lambda: calculate('pow_button'))

calculate_button = tkinter.Button(frame, text="Calculate", command=lambda: calculate('a'))

name_label.pack(pady=10)
result_label.pack(pady=10)
first_number.pack(ipady=3, pady=10)
second_number.pack(ipady=3, pady=10)
for button in (add_button, subtract_button, multiply_button, divide_button, square_button):
    button.pack(pady=10)

frame.pack()
window.mainloop()
