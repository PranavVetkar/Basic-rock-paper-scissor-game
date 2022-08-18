from tkinter import *

root = Tk()
root.title("Pranav's Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    num1 = e.get()
    global fn
    global math
    math = "Addition"
    fn = int(num1)
    e.delete(0, END)


def button_sub():
    num1 = e.get()
    global fn
    global math
    math = "Subtraction"
    fn = int(num1)
    e.delete(0, END)


def button_mult():
    num1 = e.get()
    global fn
    global math
    math = "Multiplication"
    fn = int(num1)
    e.delete(0, END)


def button_div():
    num1 = e.get()
    global fn
    global math
    math = "Division"
    fn = int(num1)
    e.delete(0, END)


def button_exp():
    num1 = e.get()
    global fn
    global math
    math = "Exponent"
    fn = int(num1)
    e.delete(0, END)


def button_equal():
    sn = e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, (fn, " + ", sn, " = ", fn + int(sn)))

    elif math == "Subtraction":
        e.insert(0, (fn, " - ", sn, " = ", fn - int(sn)))

    elif math == "Multiplication":
        e.insert(0, (fn, " * ", sn, " = ", fn * int(sn)))

    elif math == "Division":
        e.insert(0, (fn, " / ", sn, " = ", fn / int(sn)))

    elif math == "Exponent":
        e.insert(0, (fn, " ^ ", sn, " = ", fn ** int(sn)))


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_ad = Button(root, text="+", padx=39, pady=20, command=button_add)
button_eq = Button(root, text="=", padx=86, pady=20, command=lambda: button_equal())
button_clr = Button(root, text="Clear", padx=77, pady=20, command=lambda: button_clear())
button_sb = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_mt = Button(root, text="*", padx=39, pady=20, command=button_mult)
button_dv = Button(root, text="/", padx=39, pady=20, command=button_div)
button_ex = Button(root, text="^", padx=39, pady=20, command=button_exp)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_clr.grid(row=5, column=1, columnspan=2)
button_ad.grid(row=5, column=0)
button_eq.grid(row=4, column=1, columnspan=2)
button_sb.grid(row=6, column=0)
button_mt.grid(row=6, column=1)
button_dv.grid(row=6, column=2)
button_ex.grid(row=7, column=0)

root.mainloop()
