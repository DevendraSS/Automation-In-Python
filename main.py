import time
from additional_defs import login
from additional_defs import prompt
from additional_defs import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *

win = Tk()
win.geometry("500x500")

#starting_page
start = Canvas(win)
start.create_text(200, 200, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
start.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
start.pack()

#userinput and password
userinput = Entry(win)
userinput.insert(0, 'Username')
userinput.pack()

password = Entry(win, show="*")
password.insert(0, 'Password')
password.pack()

#Button which says Click Here
button = Button(win, text="Click Here to Start", command=lambda: login(userinput.get(), password.get()))
button.pack()
win.mainloop()

#window for user entry
root = Tk()
root.geometry("500x500")

canvas = Canvas(root)
canvas.create_text(200, 200, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
canvas.create_text(200, 250, text="What do you want to access?", fill="black")
canvas.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
canvas.pack()

#For entering a text
userentry = Entry(root)
userentry.pack()

#Button which says Click Here
button1 = Button(root, text="Click Here", command=lambda: prompt(userentry.get()))
button1.pack()
root.mainloop()

time.sleep(5000)
