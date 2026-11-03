from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ----------------------------Password Generator-----------------------------#
def clear_clipboard():
    try:
        # Windows clipboards sometimes ignore a totally empty string.
        # Overwriting with a single space forces the active clipboard to clear.
        pyperclip.copy("🔒 Copied password removed from clipboard after 30 seconds")
    except Exception as e:
        # Since you are in --windowed mode, if it fails,
        # this writes the error to a local debug file so you can see it!
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

# ---------------------------- Save Password ------------------------------- #
def save():
    # Map field names to their current values
    fields = {
        "Website": website_entry.get(),
        "Email/Username": email_entry.get(),
        "Password": password_entry.get()
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

    # If all checks pass, proceed with confirmation and saving
    website = fields["Website"]
    email = fields["Email/Username"]
    password = fields["Password"]

    is_ok = messagebox.askokcancel(title="Password Manager",
                           message=f"These are the details entered: "
                                   f"\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        reset()
        messagebox.showinfo(title="Password Manager", message="Password saved!")

def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock column proportions so Windows/Linux don't stretch column 2 randomly
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

# FIXED: Removed columnspan=2 so the logo stays centered on column 1
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="e", pady=5)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", pady=5)

# Entries (sticky="ew" forces them to fill columns 1 and 2 evenly)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", pady=5)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)

# Row 3: Password input and Generate button locked side-by-side
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", pady=5)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w", padx=(5, 0), pady=5)

# Row 4: Add button spans columns 1 and 2 cleanly
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

window.mainloop()