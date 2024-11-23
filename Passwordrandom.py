import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    try:
        length = int(length_input.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        # Characters to use in the password
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        # Guarantee at least one character from each category
        password = [
            random.choice(lowercase_letters),
            random.choice(uppercase_letters),
            random.choice(digits),
            random.choice(special_characters)
        ]

        # Fill the remaining length with random choices from all categories
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
        password += random.choices(all_characters, k=length - 4)

        # Shuffle the password to mix the characters
        random.shuffle(password)

        # Display the generated password
        result_entry.delete(0, tk.END)
        result_entry.insert(0, ''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Updates the clipboard with new data
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

# Setting up the main Tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Header label
header_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16))
header_label.pack(pady=10)

# Frame for password length input
length_frame = tk.Frame(root)
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12))
length_label.pack(side=tk.LEFT, padx=5)
length_input = tk.Entry(length_frame, font=("Helvetica", 12), width=10)
length_input.pack(side=tk.LEFT)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.pack(pady=10)

# Entry to display the result
result_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify="center")
result_entry.pack(pady=10)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12), command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
