import tkinter as tk

def press(key):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + key)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=20, font=('Arial', 18), bd=8, relief='sunken')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(window, text=text, width=5, height=2, command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

btn_clear = tk.Button(window, text='C', width=5, height=2, command=clear)
btn_clear.grid(row=5, column=0, columnspan=4, sticky='nsew')

window.mainloop()
