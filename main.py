from tkinter import *
from tkinter import messagebox  # This is not a class, it is just a piece of code, hence we need to import manually
import random


# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)  # Generate random letters (8,9,10)
    # print(nr_letters)
    nr_symbols = random.randint(2, 4)   # Generate random symbols (2,3,4)
    nr_numbers = random.randint(2, 4)   # Generate random numbers (2,3,4)

    # Generate a list 'password_letters' of random letters
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # print(password_letters)
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)   # Converting list to string
    password_input.insert(0, password)
    # pyperclip.copy(password) # get generated password automatically copied to clipboard

    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Extract the values entered by user:
    website_text = website_input.get()
    password_text = password_input.get()
    email_text = email_us_input.get()

    if len(website_text) == 0 and len(password_text) == 0:
        messagebox.showinfo(title="Oops !!", message="Please make sure you haven't left any fields empty !!!")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f"These are the details entered: \nWebsite: {website_text}\nEmail: {email_text} "
                                               f"\nPassword: {password_text}\nIs it ok to save? ")

        if is_ok:
            with open("password.txt", "a") as data_file:  # will close file automatically
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                email_us_input.delete(0, END)
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)  # , bg=YELLOW,
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# "Website" text
website_label = Label(text="Website: ", highlightthickness=0)  # fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold")
website_label.grid(column=0, row=1)
# "Email/Username" text
email_us_label = Label(text="Email/Username: ",
                       highlightthickness=0)  # fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold")
email_us_label.grid(column=0, row=2)
# "Password" text
password_label = Label(text="Password: ", highlightthickness=0)  # fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold")
password_label.grid(column=0, row=3)

# Input Box for Website
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=3)
website_input.focus()  # To put cursor at beginning of the input box
# Input Box for Email/Username
email_us_input = Entry(width=52)
email_us_input.grid(column=1, row=2, columnspan=3)
email_us_input.insert(0, "raina@email.com")  # Pre-populate the input box
# Input Box for Password
password_input = Entry(width=33)
password_input.grid(column=1, row=3, columnspan=1)

# Generate password Button
gen_button = Button(text="Generate Password", height=1, command=generate_password)  # Call generate_password
gen_button.grid(column=2, row=3)
# Add Button
add_button = Button(text="Add", width=44, command=save) # Call save func to save the details to txt file.
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
