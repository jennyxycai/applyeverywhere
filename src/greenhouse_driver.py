from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from profile_info import Profile
import requests
import os

APPLICATION_URLS = [
    'https://boards.greenhouse.io/sentry/jobs/5193895',
    'https://boards.greenhouse.io/appliedintuition/jobs/4296158005?gh_jid=4296158005',
]

class GreenHouseDriver:

    def __init__(self, profile = None):
        if profile:
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
        actions = ActionChains(self.driver)

        # Fill in the basic information fields
        try:
            self.driver.find_element(By.ID, 'first_name').send_keys('John')
        except:
            pass

        try:
            self.driver.find_element(By.ID, 'last_name').send_keys('Smith')
        except:
            pass
        try:
            self.driver.find_element(By.ID, 'email').send_keys('johnsmith@uni.edu')
        except:
            pass
        try:
            self.driver.find_element(By.ID, 'phone').send_keys('555555555')
        except:
            pass

        # add Location -- TODO: EDIT
        try:
            locate_me_button = self.driver.find_element(By.XPATH, "//a[contains(.,'Locate me')]")
            self.driver.move_to_element(locate_me_button)
            self.driver.click(locate_me_button)
            time.sleep(2)
        except:
            pass

        # Upload Resume
        try:
            self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys('/Users/jennycai/Desktop/applyeverywhere/src/resume.pdf')
            time.sleep(5)
        except NoSuchElementException:
            pass
        
        try:
            self.driver.find_element(By.XPATH, "//label[contains(.,'GitHub')]").send_keys('github.com/johnsmith')
        except NoSuchElementException:
            try:
                self.driver.find_element(By.XPATH, "//label[contains(.,'Github')]").send_keys('github.com/johnsmith')
            except:
                pass

        try:
            self.driver.find_element(By.XPATH, "//label[contains(.,'LinkedIn')]").send_keys('linkedin.com/in/johnsmith')
        except NoSuchElementException:
            pass # skip

        # for answering drop down questions
        try:
            auth_elem = self.driver.find_element(By.XPATH, "//label[contains(.,'authorization')]")
            if True:
                actions.click(on_element=auth_elem).send_keys(
                    Keys.ARROW_DOWN, Keys.ARROW_DOWN
                ).send_keys(Keys.ENTER).perform()
            else:  # not authorized
                actions.click(on_element=auth_elem).send_keys(
                    Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN
                ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        except:
            pass # while True: print("auth selection failing")
        
        try:
            if True:
                sponsor_elem = self.driver.find_element(By.XPATH, "//label[contains(.,'sponsorship')]")
                actions.click(on_element=sponsor_elem).send_keys(
                    Keys.ARROW_DOWN, Keys.ARROW_DOWN
                ).send_keys(Keys.ENTER).perform()
            else:  # does not require visa sponsorship
                actions.click(on_element=sponsor_elem).send_keys(
                    Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN
                ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        except:
            pass # while True: print("sponsor selection failing")

        time.sleep(10)
        print('finished!')        

    def submit_application(self):
         # Submit the application form
        self.driver.find_element(By.ID, 'submit_button_id').click()
        # Close the browser
        self.driver.quit()


gd = GreenHouseDriver()

for app_url in APPLICATION_URLS:
    gd.open_application_url(app_url)
    gd.fill_application_fields()
