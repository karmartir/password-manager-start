from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan = 2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan = 2)
email_username_input.insert(0, "example@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

window.mainloop()