from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new Chrome browser window
driver = webdriver.Chrome()

def hedlogin():
    # Navigate to a webpage with a captcha
    driver.get('https://admission.hed.gkp.pk/student_login.php')

    # Find the mobile number input field and enter the number
    mobile_number_field = driver.find_element(By.ID, "login_id")
    mobile_number_field.send_keys("03312345678")

    # Find the password input field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("nimra_1234")

    # get the values of the two numbers
    num1 = driver.find_element(By.NAME, "firstNumber").get_attribute("value")
    num2 = driver.find_element(By.NAME, "secondNumber").get_attribute("value")

    # calculate the answer to the captcha
    answer = str(int(num1) + int(num2))

    # enter the answer into the input field
    input_field = driver.find_element(By.ID, "mathresulttxt")
    input_field.clear()  # clear any existing value in the input field
    input_field.send_keys(answer)

    # locate the submit button element and click it
    submit_button = driver.find_element(By.CLASS_NAME, "read-more-btn")
    submit_button.click()