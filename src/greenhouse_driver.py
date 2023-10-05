from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from profile_info import Profile
from selenium.webdriver.common.action_chains import ActionChains
from profile_info import list_of_profiles
import os

APPLICATION_URLS = [
    "https://boards.greenhouse.io/sentry/jobs/5193895",
    "https://boards.greenhouse.io/appliedintuition/jobs/4296158005?gh_jid=4296158005",
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
        actions = ActionChains(self.driver)
        # Fill in the information fields
        # rona says: filled in the attributes for Sentry but this is not going to work for the other apps
        self.driver.find_element(By.ID, "first_name").send_keys(self.first_name)
        self.driver.find_element(By.ID, "last_name").send_keys(self.last_name)
        self.driver.find_element(By.ID, "email").send_keys(self.email)
        self.driver.find_element(By.ID, "phone").send_keys(self.phone_number)
        # self.driver.find_element(By.ID, "job_application_location").send_keys(
        #   self.location
        # )
        self.driver.find_element(
            By.ID, "job_application_answers_attributes_0_text_value"
        ).send_keys(
            self.linkedin
        )  # for linkedin

        self.driver.find_element(
            By.ID, "job_application_answers_attributes_2_text_value"
        ).send_keys(
            self.github
        )  # for github

        self.driver.find_element(By.CLASS_NAME, "drop-zone").send_keys(
            "/resume" + self.id + ".pdf"
        )
        # self.driver.find_element(By.ID, "job_application_answers_attributes_3_boolean_value").contextClick("Yes" if self.current_auth else "No")  # for current authorization in the US

        # for answering drop down question

        if self.current_auth:
            elementLocator = self.driver.find_element(
                By.ID, "s2id_job_application_answers_attributes_3_boolean_value"
            )
            actions.click(on_element=elementLocator).send_keys(
                Keys.ARROW_DOWN
            ).send_keys(Keys.ENTER).perform()
        else:  # not authorized
            elementLocator = self.driver.find_element(
                By.ID, "s2id_job_application_answers_attributes_3_boolean_value"
            )
            actions.click(on_element=elementLocator).send_keys(
                Keys.ARROW_DOWN
            ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        if self.visa_sponsor:
            elementLocator = self.driver.find_element(
                By.ID, "s2id_job_application_answers_attributes_4_boolean_value"
            )
            actions.click(on_element=elementLocator).send_keys(
                Keys.ARROW_DOWN
            ).send_keys(Keys.ENTER).perform()
        else:  # does not require visa sponsorship
            elementLocator = self.driver.find_element(
                By.ID, "s2id_job_application_answers_attributes_4_boolean_value"
            )
            actions.click(on_element=elementLocator).send_keys(
                Keys.ARROW_DOWN
            ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        # can you relocate to SF?
        elementLocator = self.driver.find_element(
            By.ID,
            "s2id_job_application_answers_attributes_6_boolean_value",
        )
        actions.click(on_element=elementLocator).send_keys(Keys.ARROW_DOWN).send_keys(
            Keys.ENTER
        ).perform()

        # accept the Sentry privacy policy
        elementLocator = self.driver.find_element(
            By.ID,
            "s2id_job_application_answers_attributes_7_answer_selected_options_attributes_7_question_option_id",
        )
        actions.click(on_element=elementLocator).send_keys(Keys.ARROW_DOWN).send_keys(
            Keys.ENTER
        ).perform()

        while True:
            pass

    def submit_application(self):
        # Submit the application form
        self.driver.find_element(By.ID, "submit_button_id").click()
        # Close the browser
        self.driver.quit()


# dummy profile
# profile = Profile(   {"first_name": "John", "last_name": "Smith", "email": "johnsmith@uni.edu"})

for profile in list_of_profiles:
    gd = GreenHouseDriver(profile)

    for app_url in APPLICATION_URLS:
        gd.open_application_url(app_url)
        gd.fill_application_fields()
