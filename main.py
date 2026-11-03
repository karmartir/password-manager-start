from tkinter import *
# ---------------------------- Save Password ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    reset()

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
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)
email_entry.insert(0, "example@gmail.com")

# Row 3: Password input and Generate button locked side-by-side
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", pady=5)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="w", padx=(5, 0), pady=5)

# Row 4: Add button spans columns 1 and 2 cleanly
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

window.mainloop()