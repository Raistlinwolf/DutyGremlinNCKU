from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import random

# Set the Check in/out time.
duty_hour = 7
duty_min = random.randint(31, 39)
off_hour = 16
off_min = random.randint(40, 49)


# Create variables for login credentials.
browser = webdriver.Edge(EdgeChromiumDriverManager().install())
url = "https://eadm.ncku.edu.tw/welldoc/ncku/iftwd/signIn.php"
username = "YourUsername"
password = "YourPassword"

def login():
    # Launch the browser and open the URL in your web driver.
    browser.get(url)

    # Find the username/email field and send the username to the input field.
    uname = browser.find_element(By.ID, "psnCode") 
    uname.send_keys(username)

    # Find the password input field and send the password to the input field.
    pword = browser.find_element(By.ID, "password")
    pword.send_keys(password)

def now():
    print(f"It is now {time.localtime().tm_hour}:{time.localtime().tm_min}")

def click_button(xpath):
    try:
        button = browser.find_element(By.XPATH, xpath)
        button.click()
    except:
        print(f"Could not find button with xpath {xpath}")

def check_time(current_time, duty_hour, duty_min, off_hour, off_min):
    if current_time.tm_hour < duty_hour:
        print(f"Good morning, today you'll on duty by {duty_hour}:{duty_min}")
        time.sleep(60)
        return True
    
    elif current_time.tm_hour == duty_hour and current_time.tm_min < duty_min:
        print(f"Good morning, today you'll on duty by {duty_hour}:{duty_min}")
        time.sleep(60)
        return True
        
    elif current_time.tm_hour == duty_hour and current_time.tm_min > duty_min:
        print(f"You are on duty, the duty off time would be {off_hour}:{off_min}")
        time.sleep(60)
        return True

    elif current_time.tm_hour == duty_hour and current_time.tm_min == duty_min:
        login()
        time.sleep(20)
        click_button("//button[1]") # Check in
        print('CheckIn Success, welcome to the office!')
        return True

    elif current_time.tm_hour == off_hour and current_time.tm_min == off_min:
        login()
        time.sleep(20)
        click_button("//button[2]") # Check out
        print('CheckOut Success, thanks for your work today!')
        return True

    elif current_time.tm_hour > duty_hour and current_time.tm_hour < off_hour:
        now()
        print(f"You are on duty, the duty off time would be {off_hour}:{off_min}")
        time.sleep(60)
        return True
    
    elif current_time.tm_hour == off_hour and current_time.tm_min < off_min:
        now()
        print(f"You are on duty, the duty off time would be {off_hour}:{off_min}")
        time.sleep(60)
        return True

    elif current_time.tm_hour == off_hour and current_time.tm_min > off_min:
        now()
        print(f"Thanks for your work today, tomorrow you'll on duty by {duty_hour}:{duty_min}")
        time.sleep(60)
        return True
    
    elif current_time.tm_hour > off_hour:
        now()
        print(f"Thanks for your work today, tomorrow you'll on duty by {duty_hour}:{duty_min}")
        time.sleep(60)
        return True

    return False

def main():
    while True:
        current_time = time.localtime()
        if check_time(current_time, duty_hour, duty_min, off_hour, off_min):
            pass

if __name__ == "__main__":
    main()
