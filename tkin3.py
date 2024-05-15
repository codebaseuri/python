import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cryptography
def send_email(sender_email, receiver_email, subject, message, sender_password):
    # SMTP server configuration for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Port for secure SMTP (TLS)

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable encryption

        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

        # Quit the SMTP session
        server.quit()
    except Exception as e:
        print("Error sending email:", e)

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt(message, key, iv):
    # Pad the message to a multiple of 16 bytes (AES block size)
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message)
    padded_message += padder.finalize()

    # Create an AES CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded message
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return ciphertext

def decrypt(ciphertext, key, iv):
    # Create an AES CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the message
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message)
    message += unpadder.finalize()

    return message
import tkinter as tk
from tkinter import messagebox

def submit_selection():
    if var.get() == 1:
        # RSA selected
        messagebox.showinfo("Selected Key Exchange Method", "RSA selected.")
        # Call function to initiate RSA key exchange
        initiate_rsa_key_exchange()
    elif var.get() == 2:
        # Diffie-Hellman selected
        messagebox.showinfo("Selected Key Exchange Method", "Diffie-Hellman selected.")
        # Call function to initiate Diffie-Hellman key exchange
        initiate_diffie_hellman_key_exchange()
    else:
        messagebox.showerror("Error", "Please select a key exchange method.")
    window.destroy()  # Close the window after selection

def initiate_rsa_key_exchange():
    # Implement RSA key exchange logic
    print("Initiating RSA key exchange...")
    # Your code here

def initiate_diffie_hellman_key_exchange():
    # Implement Diffie-Hellman key exchange logic
    print("Initiating Diffie-Hellman key exchange...")
    # Your code here

# Create Tkinter window
window = tk.Tk()
window.title("Key Exchange Method Selection")
window.geometry("300x400")  # Width x Height
# Create radio buttons
var = tk.IntVar()
tk.Label(window, text="Select Key Exchange Method:").pack()
tk.Radiobutton(window, text="RSA", variable=var, value=1).pack(anchor=tk.W)
tk.Radiobutton(window, text="Diffie-Hellman", variable=var, value=2).pack(anchor=tk.W)

# Create Submit button
tk.Button(window, text="Submit", command=submit_selection).pack()

# Run the Tkinter event loop
window.mainloop()


# Example usage
key = os.urandom(32)  # Generate a 256-bit (32-byte) random key
iv = os.urandom(16)   # Generate a 128-bit (16-byte) random IV

message = b"Hello, world!"  # Message to be encrypted

# Encrypt the message
ciphertext = encrypt(message, key, iv)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, key, iv)
print("Decrypted message:", decrypted_message.decode())

# Example usage

