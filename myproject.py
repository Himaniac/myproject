import tkinter as tk
from tkinter import messagebox
import unicodedata
import string

def normalize(text):
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    remove = string.punctuation + string.whitespace
    return ''.join(ch for ch in text if ch not in remove)

def check():
    text = entry.get()
    cleaned = normalize(text)

    if cleaned == cleaned[::-1] and cleaned != "":
        messagebox.showinfo("Result", f"'{text}' → PALINDROME ✔")
    else:
        messagebox.showinfo("Result", f"'{text}' → NOT a palindrome ✖")

# GUI
gui = tk.Tk()
gui.title("All-Case Palindrome Checker")
gui.geometry("360x160")

tk.Label(gui, text="Enter text:", font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(gui, width=35, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(gui, text="Check", command=check, font=("Arial", 12)).pack(pady=10)


gui.mainloop()
