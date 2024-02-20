import tkinter as tk
import socket

global username , password ,valid, s
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "example_user" and password == "example_password"and valid:
    
        login_status.config(text="Login successful", fg="green")
    else:
        login_status.config(text="Login failed. Please try again.", fg="red")

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    if password == confirm_password:
        s.send(username_entry +","+password_entry)
        print(s.recv(100000))
        sign_up_status.config(text="Sign up successful", fg="green")
    else:
        sign_up_status.config(text="Passwords do not match.", fg="red")

# Create main window
s=socket.socket()
port=1089
ip="127.0.0.1"
s.connect((ip,port))
username_entry=0
password_entry=0

root = tk.Tk()
root.title("Login Page")
valid=True

# Set the size of the window
root.geometry("300x300")  # Width x Height

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Confirm Password Label and Entry
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack(pady=5)

# Login Status
login_status = tk.Label(root, text="", fg="black")
login_status.pack(pady=5)

# Sign Up Status
sign_up_status = tk.Label(root, text="", fg="black")
sign_up_status.pack(pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

# Create sign up button
signup_button = tk.Button(root, text="Sign Up", command=sign_up)
signup_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()



s.close()
