from tkinter import *
from tkinter import messagebox
import secrets
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12):
    password_entry.delete(0, END)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    result = messagebox.askyesno("Confirm Save", "Are you sure you want to save the password?")
    if not result:
        return
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif website.lower() in (open("passwords.txt").read().lower()):
        messagebox.showinfo(title="Oops", message="Website already exists.")
    else:
        with open("passwords.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")
        messagebox.showinfo(title="Success", message=f"Password:'{password}' for Website: '{website}' saved successfully.")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1,column=1,padx=20,pady=20)

website_label = Label(text="Website:")
website_label.grid(row=2,column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=2,column=1,columnspan=2,padx=20,pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=3,column=0)
email_entry = Entry(width=35)
email_entry.insert(0,"dikshyant01@gmail.com")
email_entry.grid(row=3,column=1,columnspan=2,padx=20,pady=5)

password_label = Label(text="Password:")
password_label.grid(row=4,column=0)
password_entry = Entry(width=21,show="*")
password_entry.grid(row=4,column=1,padx=20,pady=5)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=4,column=2,padx=20,pady=5)

add_button = Button(text="Add",width=36, command=save_password)
add_button.grid(row=5,column=1,columnspan=2,padx=20,pady=5)


window.mainloop()