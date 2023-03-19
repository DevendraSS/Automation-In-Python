from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *

driver = webdriver.Chrome()
teacher_names = [
    "Prof. Santosh K. Bharadwaj",
    "Prof. Jitendra Kumar Muthele",
    "Prof. Angad Singh Ojha",
    "Dr. Vikas Shinde",
    "Dr. D K. Jain",
    "Prof. Prabhakar Sharma",
    "Prof. ARUN KUMAR",
    "Dr. Abhishek Dixit",
    "Prof. RAHUL SAGWAL",
    "Dr. Sanjeev Khanna",
    "Dr. Ashish Soni",
    "Dr. Nidhi Saxena",
    "Dr.Divya Chaturvedi",
    "Dr.Minakshi",
    "Dr.Atul Kumar Ray",
    "Mr.Vivek Sharma",
    "SKB",
    "JKM",
    "ASO",
    "VS",
    "DKJ",
    "Psharma",
    "AKU",
    "PS"
]
def login(username, password):
    win = Tk()
    win.geometry("500x500")
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


def prompt(userchoice):

    x = userchoice.split()

    if "attendance" in x:
        root = Tk()
        root.geometry("500x500")

        canvas = Canvas(root)
        canvas.create_text(200, 200, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(200, 250, text="Who's page do you want to access for attendance?", fill="black")
        canvas.pack()

        # For entering a text
        userentry = Entry(root)
        userentry.pack()

        # Button which says Click Here
        button1 = Button(root, text="Click Here", command=lambda: teachers(userentry.get()))
        button1.pack()
        root.mainloop()


    elif "page" in x:
        root = Tk()
        root.geometry("500x500")

        canvas = Canvas(root)
        canvas.create_text(200, 200, text="Moodle Automation", fill="black", font=('Helvetica 15 bold'))
        canvas.create_text(200, 220, text="Version: 0.0.1α", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(200, 250, text="Who's page do you want to access?", fill="black")
        canvas.pack()

        # For entering a text
        userentry = Entry(root)
        userentry.pack()

        # Button which says Click Here
        button1 = Button(root, text="Click Here", command=lambda: teachers(userentry.get()))
        button1.pack()
        root.mainloop()



