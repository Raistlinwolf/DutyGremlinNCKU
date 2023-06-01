from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser

# Create variables for login credentials.
browser = webdriver.Edge()
url = "https://github.com/login"
username = "USERNAME"
password = "PASSWORD"


# Launch the browser and open the URL in your web driver.
browser.get(url)

# Find the username/email field and send the username to the input field.
uname = browser.find_element(By.ID, "login_field") 
uname.send_keys(username)

# Find the password input field and send the password to the input field.
pword = browser.find_element(By.ID, "password")
pword.send_keys(password)

# Click sign in button to login the website.
browser.find_element("name", "commit").click()
