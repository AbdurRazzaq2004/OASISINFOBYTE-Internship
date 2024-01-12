import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()

    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    chars = ""

    if use_lowercase_var.get():
        chars += lowercase_chars

    if use_uppercase_var.get():
        chars += uppercase_chars

    if use_digits_var.get():
        chars += digits

    if use_special_chars_var.get():
        chars += special_chars

    if include_similar_chars_var.get():
        chars = chars.replace("i", "").replace("l", "").replace("1", "").replace("L", "").replace("o", "").replace("0", "").replace("O", "")

    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    generated_password_entry.configure(state="normal")
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(tk.END, password)
    generated_password_entry.configure(state="readonly")

def copy_to_clipboard():
    password = generated_password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard.")

window = tk.Tk()
window.title("Password Generator")

length_var = tk.IntVar()
use_lowercase_var = tk.BooleanVar()
use_uppercase_var = tk.BooleanVar()
use_digits_var = tk.BooleanVar()
use_special_chars_var = tk.BooleanVar()
include_similar_chars_var = tk.BooleanVar()

# Password Length
length_frame = tk.LabelFrame(window, text="Password Length")
length_frame.pack(padx=10, pady=10, fill="both", expand=True)

length_slider = tk.Scale(length_frame, from_=8, to=20, orient="horizontal", variable=length_var)
length_slider.pack(padx=10, pady=10)

# Character Types
types_frame = tk.LabelFrame(window, text="Character Types")
types_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Checkbutton(types_frame, text="Lowercase Letters", variable=use_lowercase_var).pack(anchor="w")
tk.Checkbutton(types_frame, text="Uppercase Letters", variable=use_uppercase_var).pack(anchor="w")
tk.Checkbutton(types_frame, text="Digits", variable=use_digits_var).pack(anchor="w")
tk.Checkbutton(types_frame, text="Special Characters", variable=use_special_chars_var).pack(anchor="w")

# Additional Options
options_frame = tk.LabelFrame(window, text="Additional Options")
options_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Checkbutton(options_frame, text="Exclude Similar Characters (i, l, 1, L, o, 0, O)", variable=include_similar_chars_var).pack(anchor="w")

# Generate Password Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Generated Password Entry
generated_password_entry = tk.Entry(window, state="readonly")
generated_password_entry.pack(padx=10, pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

window.mainloop()