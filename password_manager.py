import sys
import os
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# Helper function to find resource paths whether running as script or compiled .exe
relative_path = ""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ---------------------------- File I/O Helpers (DRY) ---------------------------- #
def load_data():
    """Helper to load existing data, or return an empty dict if the file doesn't exist yet."""
    try:
        with open("data.json", "r") as data_file:
            return json.load(data_file)
    except FileNotFoundError:
        return {}


def json_dump(u_data):
    """Helper to write data back to the file."""
    with open("data.json", "w") as f_data_file:
        json.dump(u_data, f_data_file, indent=4)


# ----------------------------Password Generator-----------------------------#
def clear_clipboard():
    try:
        pyperclip.copy("🔒 Copied password removed from clipboard after 30 seconds")
    except Exception as e:
        with open("error_log.txt", "a") as log:
            log.write(f"Clipboard error: {e}\n")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
    window.after(30000, clear_clipboard)


# ---------------------------- Find & Reset View Logic ------------------------------- #
def find_password():
    website = website_entry.get().strip()

    # Validate that the user actually typed a website name
    if len(website) == 0:
        messagebox.showinfo(title="Validation Error", message="The Website field cannot be empty.")
        return

    data = load_data()

    if data == {}:
        messagebox.showinfo(title="Error", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]

        # 1. Populate email and password fields with found data
        email_entry.delete(0, END)
        email_entry.insert(0, email)

        password_entry.delete(0, END)
        password_entry.insert(0, password)

        # 2. Turn all input backgrounds black with white text for the "negative" security look
        for entry in (website_entry, email_entry, password_entry):
            entry.config(bg="black", fg="white")

        # 3. Disable the generate button to prevent accidental overwrites
        generate_password_button.config(state="disabled")

        # 4. Morph Search button into a Reset button
        search_button.config(text="Reset", command=reset_search_view)

        # 5. Copy password to clipboard and schedule auto-clear for 30 seconds
        pyperclip.copy(password)
        window.after(30000, clear_clipboard)

        # Clear, explicit user notification
        messagebox.showinfo(
            title=website,
            message=f"Email: {email}\nPassword: {password}\n\n"
                    f"🔒 Password has been copied to your clipboard!\n"
                    f"It will automatically clear in 30 seconds for security."
        )
    else:
        messagebox.showinfo(title="Error", message=f"No details for '{website}' exist.")


def reset_search_view():
    """Resets the UI from 'Retrieved Mode' back to normal 'Search/Add Mode'."""
    website_entry.delete(0, END)

    email_entry.delete(0, END)
    email_entry.insert(0, "example@gmail.com")

    password_entry.delete(0, END)

    # Restore original white background and black text on all inputs
    for entry in (website_entry, email_entry, password_entry):
        entry.config(bg="white", fg="black")

    # Re-enable generate button
    generate_password_button.config(state="normal")

    # Morph Reset button back into Search button
    search_button.config(text="Search", command=find_password)
    website_entry.focus()


# ---------------------------- Save Password ------------------------------- #
def save():
    fields = {
        "Website": website_entry.get().strip(),
        "Email/Username": email_entry.get().strip(),
        "Password": password_entry.get().strip()
    }

    # Loop through each field to validate dynamically
    for field_name, value in fields.items():
        if len(value) == 0:
            messagebox.showinfo(title="Validation Error", message=f"The {field_name} field cannot be empty.")
            return

        if len(value) > 50:
            if field_name == "Password":
                messagebox.showinfo(title="Validation Error",
                                    message=f"The Password field is over 50 characters!\n\n(Did you accidentally paste the clipboard warning?)")
            else:
                messagebox.showinfo(title="Validation Error",
                                    message=f"The {field_name} input is too long (over 50 characters).")
            return

    website = fields["Website"]
    email = fields["Email/Username"]
    password = fields["Password"]
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    is_ok = messagebox.askokcancel(title="Password Manager",
                                   message=f"These are the details entered: "
                                           f"\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        data = load_data()
        data.update(new_data)
        json_dump(data)
        reset()
        messagebox.showinfo(title="Password Manager", message="Password saved!")


def reset():
    """Resets the form after a successful save action."""
    website_entry.delete(0, END)

    email_entry.delete(0, END)
    email_entry.insert(0, "example@gmail.com")

    password_entry.delete(0, END)

    for entry in (website_entry, email_entry, password_entry):
        entry.config(bg="white", fg="black")

    generate_password_button.config(state="normal")
    search_button.config(text="Search", command=find_password)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", pady=5)

# Row 1: Website Input & Search Button
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="ew", pady=5)
website_entry.focus()

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1, sticky="ew", padx=(5, 0), pady=5)

# Row 2: Email Input
email_entry = Entry(width=35)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)

# Row 3: Password Input & Generate Button
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w", padx=(5, 0), pady=5)

# Row 4: Add Button
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

window.mainloop()