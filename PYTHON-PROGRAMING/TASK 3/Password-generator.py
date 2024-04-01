import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_var.set("Invalid length")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_var.set(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Increase the frame padding
frame = tk.Frame(window, bg="skyblue", padx=20, pady=20)
frame.pack()

# Label and Entry for password length
length_label = tk.Label(frame, text="Password Length:", font=("Arial", 16))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(frame, font=("Arial", 16))
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", font=("Arial", 16), command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Label to display generated password
password_var = tk.StringVar()
password_label = tk.Label(frame, textvariable=password_var, wraplength=300, font=("Arial", 16))
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
