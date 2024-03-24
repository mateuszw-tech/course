import tkinter
from calculator import CalculatorApp

window: tkinter.Tk = tkinter.Tk()
app: CalculatorApp = CalculatorApp(window, "Simple Calculator")
app.display_app()
