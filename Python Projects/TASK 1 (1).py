#!/usr/bin/env python
# coding: utf-8

# ## TASK 1

# In[1]:


import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        show_message("Task added successfully", "green")
    else:
        show_message("Enter the text", "red")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        show_message("Deleted text successfully", "Royal blue")
    else:
        show_message("There is no text/Select the text", "red")

def Edit():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_items = listbox.get(selected_task_index[0])
        entry.delete(0, tk.END)
        entry.insert(0, selected_items)
        show_message("Task loaded for editing", "blue")
    else:
        show_message("Select a task to edit", "red")

def Done():
    edited_task = entry.get()
    selected_task_index = listbox.curselection()
    if selected_task_index and edited_task:
        listbox.delete(selected_task_index[0])
        listbox.insert(selected_task_index[0], edited_task)
        entry.delete(0, tk.END)
        show_message("Edited text successfully", "green")
    else:
        show_message("No text selected or no input for edit", "red")

def show_message(message, color):
    status_label.config(text=message, fg=color)

root = tk.Tk()
root.title("Todo List")

title_label = tk.Label(root, text="ToDo List", font="Garamond 30", fg="Black", bg="green")
title_label.pack(fill="both")

l1 = tk.Label(root, text="Enter the text", font="Times 10")
l1.pack()

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Submit", command=add_task)
add_button.pack()

done = tk.Button(root, text="Edit the text", command=Done)
done.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

remove_button = tk.Button(root, text="Delete", command=remove_task)
remove_button.pack()

edit = tk.Button(root, text="EDIT", command=Edit)
edit.pack()


status_label = tk.Label(root, text="", font="Times 10")
status_label.pack()

root.mainloop()


# In[ ]:





# In[ ]:





# In[2]:




