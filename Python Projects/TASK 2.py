#!/usr/bin/env python
# coding: utf-8

# ## TASK 2

# In[2]:


import tkinter as tk
import tkinter.messagebox  
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(window, padx=10)
frame.pack()
entry = tk.Entry(frame,width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=5)
  
  
def myclick(number):
    entry.insert(tk.END, number)
  
  
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
  
  
def clear():
    entry.delete(0, tk.END)
def backspace():
    current_text = entry.get()
    new_text = current_text[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, new_text)
  
button_1 = tk.Button(frame, text='1', padx=15,pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(frame, text='2', padx=15,pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(frame, text='3', padx=15,pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(frame, text='4', padx=15,pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(frame, text='5', padx=15,pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(frame, text='6', padx=15,pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(frame, text='7', padx=15,pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(frame, text='8', padx=15,pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=0, pady=2)
button_add = tk.Button(frame, text="+", padx=15,pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)
button_subtract = tk.Button(frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)
button_multiply = tk.Button(frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)
button_div = tk.Button(frame, text="/", padx=15,pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)  
button_backspace = tk.Button(frame, text="backspace",padx=15, pady=5, width=12, command=backspace)
button_backspace.grid(row=6, column=1, columnspan=2, pady=2)
button_equal = tk.Button(frame, text="=", padx=15,pady=5, width=12, command=equal)
button_equal.grid(row=4, column=1, columnspan=2, pady=2)
button_clear = tk.Button(frame, text="clear",padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=7, column=0, columnspan=3, pady=3)
window.mainloop()

