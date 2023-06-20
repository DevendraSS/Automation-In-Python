# Automation-In-Python
# Automating a student learning website (Moodle) using Selenium 

The code begins by importing the necessary modules: time, tkinter, and selenium. The time module provides functionality for time-related operations, tkinter is a Python GUI toolkit used for creating graphical user interfaces, and selenium is a web automation framework that allows interaction with web browsers.

Next, an instance of the Chrome WebDriver is created using webdriver.Chrome(). This WebDriver is essential for automating interactions with the Chrome browser. It enables the program to navigate web pages, fill in forms, and click buttons programmatically.

The login() function is defined, which takes the username and password as parameters. Inside this function, the Selenium WebDriver is used to automate the login process on the Moodle platform. It maximizes the browser window, opens the Moodle login page using driver.get(), enters the provided username and password into the respective fields using driver.find_element(), and finally clicks the login button using driver.find_element().click(). The win.destroy() statement closes the tkinter window after successful login.

The teachers() function is responsible for navigating to specific Moodle course pages based on the provided teacher names. It takes the teachnames parameter and checks for specific teacher names using conditional statements. If a match is found, it uses driver.get() to navigate to the corresponding URL. For example, if the input is "DKJ" or "Deepak", it opens the page for Deepak's course on Moodle. The same pattern applies to other teachers.

The prompt() function is called when the user wants to access either the attendance or a specific teacher's page. It creates a new tkinter window using tkinter.Tk() to prompt the user for input. The user's choice is split into separate words using split(). If the word "attendance" is present, the function destroys the current window win2.destroy() and creates a new window using tkinter.Tk(). It sets the window dimensions, creates labels and entry fields using tkinter.Label() and tkinter.Entry(), and provides a button to trigger the teacher_attendance() function.

The teacher_attendance() function is called when the user wants to check the attendance of a specific teacher. It takes teachername and subject as parameters. Inside the function, the teacher name and subject are split into separate words using split(). Then, based on the teacher name and subject provided, the function uses conditional statements to navigate to the corresponding attendance page using driver.get(). If the attendance page is found, it checks if the attendance prompt is available. If it is, it navigates to the attendance page. Otherwise, it displays a message indicating that no attendance prompt is available.

The initial tkinter GUI window is created using tkinter.Tk(). It sets the window title, dimensions, and background color. Labels are added to display information about the program. Entry fields are provided for the user to enter their username and password. A button labeled "Click Here to Start" is provided to trigger the login() function when clicked.

Another tkinter GUI window is created for user input using tkinter.Tk(). It prompts the user with a question and provides an entry field for their input. Clicking the "Click Here" button invokes the prompt() function, passing the user's input as a parameter.

The mainloop() calls in the code start the event loops for the tkinter windows, ensuring they remain visible and responsive to user interactions.

At the end of the code, there is a time.sleep(5000) statement, which pauses the program for 5 seconds before exiting. This pause is unnecessary and can be removed.

Overall, this code provides a user-friendly interface for automating the login process and accessing specific pages on the Moodle platform. It utilizes the Selenium WebDriver to interact with web elements and navigate through web pages. The tkinter GUI components enable the user to input their credentials, select options, and view information conveniently. The code demonstrates how different functions can be structured and interconnected to automate web tasks and provide an enhanced user experience.
