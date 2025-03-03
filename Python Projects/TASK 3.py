#!/usr/bin/env python
# coding: utf-8

# ## TASK 3

# In[2]:


import tkinter
import random
import string

def password():
    name = E.get().strip()
    length_str = E1.get().strip()
    
    if not name:
        show_message("Please enter the name first", "red")
        return

    if not length_str.isdigit():
        show_message("Password length must be a number", "red")
        return

    length = int(length_str)

    if length < 4:
        show_message("Password length must be at least 4", "red")
        return

 
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

   
    password_chars = [random.choice(characters) for _ in range(length)]
    random.shuffle(password_chars)
    generated_password = ''.join(password_chars)

  
    E2.delete(0, tkinter.END)
    E2.insert(0, generated_password)
    show_message("Password generated successfully!", "green")

def show_message(message, color):
    status_label.config(text=message, fg=color)

def clear_all():
    E.delete(0, tkinter.END)
    E1.delete(0, tkinter.END)
    E2.delete(0, tkinter.END)
    show_message("", "black")

def reset_password():
    E2.delete(0, tkinter.END)
    show_message("", "black")


window = tkinter.Tk()
window.title("Password Generator")

tkinter.Label(window, text="Password Generator", font="Times 20 underline", fg="Green").grid(row=0, column=0, columnspan=2)

tkinter.Label(window, text="Enter user name:", font="Times 20").grid(row=1, column=0, pady=20)
E = tkinter.Entry(window, width=20, font="Times 20")
E.grid(row=1, column=1, pady=20)

tkinter.Label(window, text="Enter Password length:", font="Times 20").grid(row=2, column=0, pady=15)
E1 = tkinter.Entry(window, width=20, font="Times 20")
E1.grid(row=2, column=1, pady=15)

tkinter.Label(window, text="Generated Password:", font="Times 20").grid(row=3, column=0, pady=15)
E2 = tkinter.Entry(window, width=20, font="Times 20")
E2.grid(row=3, column=1, pady=15)

tkinter.Button(window, text="GENERATE PASSWORD", bg="Blue", fg="white", command=password).grid(row=4, column=1, pady=15)
tkinter.Button(window, text="ACCEPT", fg="Blue", command=clear_all).grid(row=5, column=1, pady=5)
tkinter.Button(window, text="RESET", fg="Blue", command=reset_password).grid(row=6, column=1, pady=5)


status_label = tkinter.Label(window, text="", font="Times 10")
status_label.grid(row=7, column=0, columnspan=2)

window.mainloop()

