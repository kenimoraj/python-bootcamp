from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
N_OF_LETTERS = 10
N_OF_NUMS = 5
N_OF_SYMBOLS = 5
LETTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
NUMBERS = "1234567890"
SYMBOLS = "!@#$%^&*()-=_+[]{};:,./<>?"
import random
import pyperclip
import json
def generate_password():

    letters = [letter for letter in LETTERS]
    numbers = [num for num in NUMBERS]
    symbols = [sym for sym in SYMBOLS]

    pw_chars = []

    for _ in range(N_OF_LETTERS):
        pw_chars.append(random.choice(LETTERS))

    for _ in range(N_OF_NUMS):
        pw_chars.append(random.choice(NUMBERS))

    for _ in range(N_OF_SYMBOLS):
        pw_chars.append(random.choice(SYMBOLS))

    random.shuffle(pw_chars)

    pw_string = "".join(pw_chars)

    global password_entry
    password_entry.delete(0, END)
    password_entry.insert(0, pw_string)
    pyperclip.copy(pw_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_contents_to_file():
    global website_entry
    global username_entry
    global password_entry

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {website: {username: password}}
    if len(website) > 0 and len(username) > 0 and len(password) > 0:

        is_ok = messagebox.askokcancel(title="Save password?", message=f"Save the following details?\n"
                                                                       f"Website: {website}\n"
                                                                       f"Username: {username}\n"
                                                                       f"Password: {password}")
        if is_ok:

            try:
                with open("./data.json", "r") as file:
                    data = json.load(file)
                    print(data)
                    data.update(new_data)
                    print(data)

                with open("./data.json", "w") as file:
                    json.dump(data, fp=file, indent=4)

                for e in [website_entry, password_entry]:
                    e.delete(0, END)

            except FileNotFoundError:
                messagebox.showwarning(title="File Not Found", message="No \"data.json\" file found.")

            except json.decoder.JSONDecodeError:
                messagebox.showwarning(title="Corrupted Data File", message="Data file was corrupted.")
            finally:
                website_entry.focus()
    else:
        messagebox.showinfo(title="Oops!", message="Don't leave any of the fields empty!")

# ------------------------- SEARCH WEBSITE --------------------------- #

def search_website():
    website = website_entry.get()

    try:
        with open("./data.json", "r") as file:
            data = json.load(fp=file)

        uname = list(data[website].items())[0][0]
        passwd = list(data[website].items())[0][1]
        messagebox.showinfo(title=f"Search results for {website}", message=f"Username: {uname}\nPassword: {passwd}")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message=f"Data File \"data.json\" not found")
    except KeyError:
        messagebox.showinfo(title="Search results", message=f"No data for website '{website}'")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#input labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email / Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#input boxes
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=51)
username_entry.insert(0, "michal@jarominek.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#buttons

search_button = Button(text="Search", command=search_website, width=14)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_contents_to_file)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
