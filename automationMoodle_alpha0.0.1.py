import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *

driver = webdriver.Chrome()

def login(username, password):
    driver.get("http://moodle.mitsgwalior.in/login/index.php")
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()
    win.destroy()

def teachers(teachnames):
    if teachnames.lower() == "dkj":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=344")

    elif teachnames.lower() == "aso":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=355")

    elif teachnames.lower() == "psharma":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=366")

    elif teachnames.lower() == "sk":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=530")

    elif teachnames.lower() == "ashish":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=771")

    elif teachnames.lower() == "vs":
        driver.get("http://moodle.mitsgwalior.in/course/view.php?id=724")


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
button1 = Button(win, text="Click Here to Start", command=lambda: login(userinput.get(), password.get()))
button1.pack()
win.mainloop()


root = Tk()
root.geometry("500x500")

#heading
canvas = Canvas(root)
canvas.create_text(200, 200, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
canvas.create_text(200, 250, text="Who's page do you want to access?", fill="black")
canvas.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
canvas.pack()

#For entering a text
teachername = Entry(root)
teachername.pack()

#Button which says Click Here
button = Button(root, text="Click Here", command=lambda: teachers(teachername.get()))
button.pack()
root.mainloop()


time.sleep(60)

time.sleep(5000)