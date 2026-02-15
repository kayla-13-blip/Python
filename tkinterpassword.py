import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly") 
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the length.")
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
tk.Label(root, text="Enter Password Length:", font=("Arial", 10)).pack(pady=10)
length_entry = tk.Entry(root, width=10)
length_entry.pack()
length_entry.insert(0, "12")
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=15)
tk.Label(root, text="Generated Password:", font=("Arial", 10)).pack()
password_entry = tk.Entry(root, font=("Arial", 12), width=30, state="readonly", justify="center")
password_entry.pack(pady=5)
root.mainloop()
