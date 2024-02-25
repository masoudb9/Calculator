
from tkinter import *
equation = ""


def clear():
    global equation
    equation = ""
    l1.config(text=equation)


def show(value):
    global equation
    equation += value
    l1.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error!"
    l1.config(text=result)


window = Tk()
window.title("|^_^| Calculator")
window.minsize(360, 450)
window.maxsize(360, 450)
window.resizable(False, False)
l1 = Label(window, border=2, width=32, font=("", 15, "bold"), justify='right', height=5)
l1.grid(padx=5, pady=5)
b1 = Button(window, text="1", width=5, height=3, border=4, command=lambda: show("1"), background="lightgrey",
            font=("Arial", 14, "bold"))
b1.place(x=3, y=90)
b2 = Button(window, text="2", width=5, height=3, border=4, command=lambda: show("2"), background="lightgrey",
            font=("Arial", 14, "bold"))
b2.place(x=78, y=90)
b3 = Button(window, text="3", width=5, height=3, border=4, command=lambda: show("3"), background="lightgrey",
            font=("Arial", 14, "bold"))
b3.place(x=153, y=90)
b4 = Button(window, text="4", width=5, height=3, border=4, command=lambda: show("4"), background="lightgrey",
            font=("Arial", 14, "bold"))
b4.place(x=3, y=181)
b5 = Button(window, text="5", width=5, height=3, border=4, command=lambda: show("5"), background="lightgrey",
            font=("Arial", 14, "bold"))
b5.place(x=78, y=181)
b6 = Button(window, text="6", width=5, height=3, border=4, command=lambda: show("6"), background="lightgrey",
            font=("Arial", 14, "bold"))
b6.place(x=153, y=181)
b7 = Button(window, text="7", width=5, height=3, border=4, command=lambda: show("7"), background="lightgrey",
            font=("Arial", 14, "bold"))
b7.place(x=3, y=270)
b8 = Button(window, text="8", width=5, height=3, border=4, command=lambda: show("8"), background="lightgrey",
            font=("Arial", 14, "bold"))
b8.place(x=78, y=270)
b9 = Button(window, text="9", width=5, height=3, border=4, command=lambda: show("9"), background="lightgrey",
            font=("Arial", 14, "bold"))
b9.place(x=153, y=270)
b10 = Button(window, text="0", width=5, height=3, border=4, command=lambda: show("0"), background="lightgrey",
             font=("Arial", 14, "bold"))
b10.place(x=78, y=359)
s1 = Button(window, text="*", width=4, height=3, border=4, command=lambda: show("*"), background="skyblue",
            font=("Arial", 14, "bold"))
s1.place(x=230, y=90)
s2 = Button(window, text="/", width=4, height=3, border=4, command=lambda: show("/"), background="skyblue",
            font=("Arial", 14, "bold"))
s2.place(x=295, y=90)
s3 = Button(window, text="+", width=4, height=3, border=4, command=lambda: show("+"), background="skyblue",
            font=("Arial", 14, "bold"))
s3.place(x=230, y=181)
s4 = Button(window, text="-", width=4, height=3, border=4, command=lambda: show("-"), background="skyblue",
            font=("Arial", 14, "bold"))
s4.place(x=295, y=181)
s5 = Button(window, text="=", width=9, height=7, border=5, background="orange",  command=calculate,
            font=("Arial", 14, "bold"))
s5.place(x=231, y=270)
s6 = Button(window, text="C", width=5, height=3, border=4, foreground='black', command=clear, background="lightgrey",
            font=("Arial", 14, "bold"))
s6.place(x=3, y=359)
s7 = Button(window, text=".", width=5, height=3, border=4, command=lambda: show("."), background="lightgrey",
            font=("Arial", 14, "bold"))
s7.place(x=153, y=359)
window.mainloop()
