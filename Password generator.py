import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(tk.END, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

window = tk.Tk()
window.title("Password Generator")

label_length = tk.Label(window, text="Enter password length:")
label_length.pack(pady=5)

entry_length = tk.Entry(window)
entry_length.pack(pady=5)

button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

label_password = tk.Label(window, text="Generated Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(window, width=30)
entry_password.pack(pady=5)

button_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=10)

window.mainloop()
