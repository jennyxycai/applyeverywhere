from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from profile_info import Profile

# from profile_info import list_of_profiles
import requests
import os

APPLICATION_URLS = [
    "https://boards.greenhouse.io/appliedintuition/jobs/4296158005?gh_jid=4296158005",
    "https://boards.greenhouse.io/sentry/jobs/5193895",
]


class GreenHouseDriver:
    def __init__(self, profile=None):
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

        # # Fill in the basic information fields
        # try:
        #     self.driver.find_element(By.ID, "first_name").send_keys(self.first_name)
        # except:
        #     pass

        # try:
        #     self.driver.find_element(By.ID, "last_name").send_keys(self.last_name)
        # except:
        #     pass
        # try:
        #     self.driver.find_element(By.ID, "email").send_keys(self.email)
        # except:
        #     pass
        # try:
        #     self.driver.find_element(By.ID, "phone").send_keys(self.phone_number)
        # except:
        #     pass

        # add Location -- TODO: EDIT
        try:
            locate_me_button = self.driver.find_element(
                By.ID, "job_application_location"
            )

            actions.click(on_element=locate_me_button).send_keys(
                "Cambridge, MA"
            ).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
            print("1")

            # self.driver.(locate_me_button)
            # self.driver.click(locate_me_button)
            time.sleep(2)
        except:
            print("2")
            pass

        # Upload Resume
        # try:
        #     self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(
        #         "/Users/rona/Documents/GitHub/applyeverywhere-1/src/resumes/"
        #         + self.id
        #         + ".pdf"
        #     )  # for now we'll have to just change the path every time
        #     #   for whoever is running this code on their laptop since we don't have the same path
        #     time.sleep(5)
        # except NoSuchElementException:
        #     pass

        try:
            # school_elem = self.driver.find_element(
            #     By.XPATH, "//label[contains(.,'School')]"
            # )
            school_elem = self.driver.find_element(
                By.ID, "s2id_education_school_name_0"
            )
            actions.click(on_element=school_elem).send_keys(
                "Massachusetts Institute of Technology"
            ).perform()
            time.sleep(5)  # give the school search time
            actions.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER).perform()
            print("4")

        except NoSuchElementException:
            print("3")
            pass
        # try:
        #     self.driver.find_element(
        #         By.XPATH, "//label[contains(.,'GitHub')]"
        #     ).send_keys(self.github)
        # except NoSuchElementException:
        #     try:
        #         self.driver.find_element(
        #             By.XPATH, "//label[contains(.,'Github')]"
        #         ).send_keys(self.github)
        #     except:
        #         pass

        # try:
        #     self.driver.find_element(
        #         By.XPATH, "//label[contains(.,'LinkedIn')]"
        #     ).send_keys(self.linkedin)
        # except NoSuchElementException:
        #     pass  # skip

        # for answering drop down questions
        # try:
        #     auth_elem = self.driver.find_element(
        #         By.XPATH, "//label[contains(.,'authorization')]"
        #     )
        #     if self.current_auth:
        #         actions.click(on_element=auth_elem).send_keys(
        #              Keys.ARROW_DOWN
        #         ).send_keys(Keys.ENTER).perform()
        #     else:  # not authorized
        #         actions.click(on_element=auth_elem).send_keys(
        #              Keys.ARROW_DOWN, Keys.ARROW_DOWN
        #         ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # except:
        #     pass  # while True: print("auth selection failing")

        # try:
        #     if self.visa_sponsor:
        #         sponsor_elem = self.driver.find_element(
        #             By.XPATH, "//label[contains(.,'sponsorship')]"
        #         )
        #         actions.click(on_element=sponsor_elem).send_keys(
        #             Keys.ARROW_DOWN, Keys.ARROW_DOWN
        #         ).send_keys(Keys.ENTER).perform()
        #     else:  # does not require visa sponsorship
        #         actions.click(on_element=sponsor_elem).send_keys(
        #             Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN
        #         ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # except:
        #     pass  # while True: print("sponsor selection failing")

        # self.submit_application()
        time.sleep(10)

        print("finished")

    def submit_application(self):
        # Submit the application form
        self.driver.find_element(By.ID, "submit_app").click()
        # Close the browser
        # self.driver.quit()


# for profile in list_of_profiles:
# gd = GreenHouseDriver(profile)
gd = GreenHouseDriver()

for app_url in APPLICATION_URLS:
    gd.open_application_url(app_url)
    gd.fill_application_fields()
    gd.submit_application()
# gd.submit_application()
