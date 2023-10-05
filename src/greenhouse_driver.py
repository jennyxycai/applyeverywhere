from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from profile_info import Profile
import os

APPLICATION_URLS = [
    'https://boards.greenhouse.io/sentry/jobs/5193895',
    'https://boards.greenhouse.io/appliedintuition/jobs/4296158005?gh_jid=4296158005',
]

class GreenHouseDriver:

    def __init__(self, profile: Profile):
        for info, value in profile.__dict__.items():
            setattr(self, info, value)

        # Set up the driver (assuming you're using Chrome, but you can use others like Firefox)
        # make sure your selenium version is at least 4.6.0. use `pip3 install selenium`
        self.driver = webdriver.Chrome()

    def open_application_url(self, url: str, timeout: int = 10):
        # Open the Greenhouse job application page
        self.driver.get(url)

        # Wait for the page to load
        WebDriverWait(self.driver, timeout)  # Adjust the timeout as needed

    def fill_application_fields(self):
        # Fill in the information fields
        self.driver.find_element(By.ID, 'first_name').send_keys('John')
        self.driver.find_element(By.ID, 'last_name').send_keys('Smith')
        self.driver.find_element(By.ID, 'email').send_keys('johnsmith@uni.edu')
        while True:
            pass        


    def submit_application(self):
         # Submit the application form
        self.driver.find_element(By.ID, 'submit_button_id').click()
        # Close the browser
        self.driver.quit()

# dummy profile
profile = Profile({'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith@uni.edu'})

gd = GreenHouseDriver(profile)

for app_url in APPLICATION_URLS:
    gd.open_application_url(app_url)
    #gd.fill_application_fields()
