from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_assamilogin():
    # set up the webdriver
    driver = webdriver.Chrome()
    driver.get("https://assami.kp.gov.pk/Login")

    try:
        # locate the input element and enter a value into it
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("h@gmail.com")

        # locate the input element and enter a value into it
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("12345")

        # Find the login button and click it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))).click()

        # Wait for the confirm button to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sweet-alert .confirm'))).click()

        # locate the button element and click on it
        driver.find_element(By.CLASS_NAME, "btn-primary").click()

        # locate the input element and enter a value into it
        driver.find_element(By.NAME, "first_name").send_keys("Nimra")

        dob_element = driver.find_element(By.ID, "dob")
        driver.execute_script("arguments[0].value = '05/05/2001';", dob_element)

        # locate the select element and select an option by its value
        Select(driver.find_element(By.ID, "gender")).select_by_value("1")

        # locate the select element and select an option by its value
        Select(driver.find_element(By.ID, "marital_status")).select_by_value("1")

        # locate the input element and enter text into it
        driver.find_element(By.ID, "father_name").send_keys("Ayaz")

        # locate the select element and select the "Islam" option
        Select(driver.find_element(By.NAME, "religion")).select_by_value("1")

        # Locate the phone number input element and clear its current value
        phone_input = driver.find_element(By.ID, "mobile_no")
        phone_input.clear()
        # Enter the phone number
        phone_input.send_keys("+92-0311-1234567")

        # Locate the landline number input element and clear its current value
        landline_input = driver.find_element(By.NAME, "land_line")
        landline_input.clear()

        # Enter the landline number
        landline_input.send_keys("+92-1111111111")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_assamilogin()


#The purpose of using `try`, `finally`, and `if __name__ == "__main__":` in the code is as follows:

#1. `try` block: The code inside the `try` block contains the main logic of the program, which is to interact with the web page and perform the required actions. If any exception occurs while executing the code inside the `try` block, the control will jump to the `except` block to handle the exception.

#2. `finally` block: The code inside the `finally` block is executed after the `try` block, regardless of whether an exception occurred or not. In this code, we have added a `driver.quit()` statement to ensure that the webdriver is closed properly after the test is completed.

#3. `if __name__ == "__main__":` block: This block is used to ensure that the code inside it is only executed if the script is being run as the main program, and not imported as a module by another program. This is a common way of organizing code in Python modules, and it ensures that the code is only executed when the module is run directly.

#In summary, `try` and `finally` blocks are used to handle exceptions and ensure that resources are properly cleaned up, while the `if __name__ == "__main__":` block is used to ensure that the code is only executed when the module is run directly as a script.