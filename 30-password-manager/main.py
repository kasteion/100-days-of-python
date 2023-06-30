import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ------------------------- GENERATE PASSWORD ------------------------- #

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    characters = [choice(letters) for _ in range(0, randint(8, 10))] + \
                 [choice(symbols) for _ in range(0, randint(2, 4))] + \
                 [choice(numbers) for _ in range(0, randint(2, 4))]
    shuffle(characters)
    password_entry.delete(0, END)
    pyperclip.copy(''.join(characters))
    password_entry.insert(END, pyperclip.paste())

# --------------------------- SAVE PASSWORD ---------------------------- #


def save_password():
    website = website_entry.get().strip()
    user = email_users_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error", message="Hey!\nDon't leave fields empty!")
        window.focus()
        website_entry.focus()
        return

    # messagebox.showinfo(title="Title", message="Message")
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}\n"
                                                          f"Password: {password}\nIs it ok to save?")

    if is_ok:
        # with open("data.txt", mode="a") as data:
        #     data.write(f"{website} | {user} | {password}\n")
        # Write
        # json.dump(new_data, data_file, indent=4)
        # Read
        # data = json.load(data_file)
        # print(data)
        # Update
        # data = json.load(data_file)
        # data.update(new_data)
        # json.dump(data, data_file, indent=4)
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except (FileNotFoundError, json.JSONDecodeError):
            data_file_w = open("data.json", mode="w")
            json.dump(new_data, data_file_w, indent=4)
        else:
            data_file_w = open("data.json", mode="w")
            json.dump(data, data_file_w, indent=4)
        finally:
            data_file_w.close()

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ----------------------------- SEARCH PASSWORD ------------------------ #
def search_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            value = data.get(website)
            if value is not None:
                messagebox.showinfo(title=website, message=f"Email: {value.get('email')}\n"
                                                           f"Password: {value.get('password')}")
            else:
                messagebox.showerror("Not found", "No details for the website exist")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="No contents in file")




# ------------------------------ UI SETUP ------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(fg="black", bg="white", highlightthickness=0)
website_entry.grid(column=1, row=1, sticky='ew', pady=5, padx=5)
website_entry.focus()

website_search = Button(text="Search", fg="black", bg="white", highlightthickness=0, command=search_password)
website_search.grid(column=2, row=1, sticky='ew', padx=5, pady=5)

email_users_label = Label(text="Email/Username", fg="black", bg="white")
email_users_label.grid(column=0, row=2)

email_users_entry = Entry(fg="black", bg="white", highlightthickness=0)
email_users_entry.grid(column=1, row=2, columnspan=2, sticky='ew', pady=5, padx=5)
email_users_entry.insert(0, "email@example.com")

password_label = Label(text="Password:", fg="black", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(fg="black", bg="white", highlightthickness=0, width=21)
password_entry.grid(column=1, row=3, pady=5, sticky="ew", padx=5)

password_button = Button(text="Generate Password", fg="black", bg="white", highlightthickness=0,
                         command=generate_password)
password_button.grid(column=2, row=3, padx=5)

add_button = Button(text="Add", fg="black", bg="white", highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew', padx=5)
window.mainloop()
