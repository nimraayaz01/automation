import os
import time
from selenium_app import SeleniumApp
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def main():
    try:
        selenium_obj = SeleniumApp(os.getenv("APP_URL"))
        selenium_obj.input_text_into_field_via_name("email", os.getenv("APP_USERNAME"))
        selenium_obj.input_text_into_field_via_name("password", os.getenv("APP_PASSWORD"))
        time.sleep(5)
        selenium_obj.exit_automation()
    except:
        pass


if __name__ == "__main__":
    main()
