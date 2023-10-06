from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# from profile_info import list_of_profiles

APPLICATION_URLS = [
    #"https://boards.greenhouse.io/appliedintuition/jobs/4296158005?gh_jid=4296158005",
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

    def fill_basic_fields(self, url):
        try:
            self.driver.find_element(By.ID, "first_name").send_keys(
                'john')  # send_keys(self.first_name)
        except:
            pass

        try:
            self.driver.find_element(By.ID, "last_name").send_keys(
                'smith')  # send_keys(self.last_name)
        except:
            pass
        try:
            self.driver.find_element(By.ID, "email").send_keys(
                'john@gmail.com')  # send_keys(self.email)
        except:
            pass
        try:
            self.driver.find_element(By.ID, "phone").send_keys(
                '55555555')  # .send_keys(self.phone_number)
        except:
            print(f'No phone field in {url}')
            pass

    def fill_autocomplete_fields(self, url):
        # add Location
        try:
            location_field = self.driver.find_element(
                By.ID, 'job_application_location')
            if location_field:
                location_field.find_element(By.ID, 'auto_complete_input').send_keys(
                    "Cambridge, Massachusetts"  # self.location
                ).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()

                print("Location entered")
                time.sleep(1)
        except:
            print(f"No location field in {url}")
            pass

    def fill_education_fields(self, url):
        actions = ActionChains(self.driver)

        # School drop down
        try:
            school_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'School')]"
            )
            school_elem = self.driver.find_element(
                By.ID, "s2id_education_school_name_0"
            )
            actions.click(on_element=school_elem).send_keys(
                "Massachusetts Institute of Technology"  # self.organization
            ).perform()
            time.sleep(1)  # give the school search time
            actions.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                              Keys.ENTER).perform()
        except NoSuchElementException:
            print(f"No school field in {url}")
            pass

        # Degree drop down
        try:
            degree_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'Degree')]"
            )
            degree_elem = self.driver.find_element(
                By.ID, "s2id_education_degree_0"
            )
            actions.click(on_element=degree_elem).send_keys(
                "Bachelor"  # self.expertise
            ).perform()
            time.sleep(1)  # give the degree search time
            actions.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                              Keys.ENTER).perform()
        except:
            print(f"No degree field in {url}")
            pass

        # end/graduation date
        try:
            end_date_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'End Date')]"
            )
            month_input = end_date_elem.find_element(By.XPATH, "//input[contains(@name, 'month')]").send_keys(
                '06',  # self.graduation_date.split()[0]
            )
            year_input = end_date_elem.find_element(By.XPATH, "//input[contains(@name, 'year')]").send_keys(
                '2024',  # self.graduation_date.split()[1]
            )
        except:
            pass

        try:
            end_date_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'graduat')]"
            )
            if end_date_elem:
                end_date_elem.send_keys(
                    Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER).perform()
        except:
            pass

    def fill_short_answers(self, url):
        # github
        try:
            self.driver.find_element(
                By.XPATH,
                "//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'github')]"
            ).send_keys(
                'github.com/johnsmith'  # self.github
            )
        except:
            pass

        # linkedin
        try:
            self.driver.find_element(
                By.XPATH,
                "//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'linkedin')]"
            ).send_keys(
                'linkedin.com/in/johnsmith'  # self.linkedin
            )
        except:
            pass

        # fill GPA
        try:
            gpa_elem = self.driver.find_element(
                By.XPATH,
                "//label[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'gpa')]").send_keys(
                '4.0'  # self.gpa
            )
        except:
            pass

    def fill_auth_sponsorship_questions(self, url):
        actions = ActionChains(self.driver)
        # sponsorship question -- hard code 'no' to requiring sponsorship
        try:
            sponsor_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'sponsorship')]"
            )
            actions.click(on_element=sponsor_elem).send_keys(
                Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN
            ).send_keys(Keys.ENTER).perform()
            time.wait(2)
        except:
            pass

        # hardcode sponsorship question if dropdown is hidden element
        try:
            sponsor_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'sponsorship')]"
            )
            actions.click(on_element=sponsor_elem).send_keys(
                Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN
            ).send_keys(Keys.ENTER).perform()
            
            time.wait(2)
        except:
            pass

        # authorization question -- hard code in 'yes' to having authorization
        try:
            auth_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'authorization')]"
            )
            actions.click(on_element=auth_elem).send_keys(
                Keys.ARROW_DOWN, Keys.ARROW_DOWN
            ).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        except:
            pass

    def fill_dropdowns(self, url):
        actions = ActionChains(self.driver)
        # how'd you hear about us?
        try:
            how_hear_about_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'hear about us')]")
            actions.click(on_element=how_hear_about_elem).send_keys(
                Keys.ARROW_DOWN,
            ).send_keys(Keys.ENTER).perform()
        except:
            pass

        # relocation office
        try:
            relocate_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'office')]")
            actions.click(on_element=relocate_elem).send_keys(
                Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            ).send_keys(Keys.ENTER).perform()
        except:
            pass

        # agree to privacy policy
        try:
            privacy_elem = self.driver.find_element(
                By.XPATH, "//label[contains(.,'Privacy')]")
            actions.click(on_element=privacy_elem).send_keys(
                Keys.ARROW_DOWN, Keys.ARROW_DOWN,
            ).send_keys(Keys.ENTER).perform()
        except:
            pass

    def fill_application_fields(self, url):
        actions = ActionChains(self.driver)

        # # Fill in the basic information fields
        #self.fill_basic_fields(url)

        # Upload Resume
        try:
            resume_fieldset = self.driver.find_element(
                By.ID, 'resume_fieldset')
            if resume_fieldset:
                resume_fieldset.find_element(By.XPATH, '//input[@type="file"]').send_keys(
                    # "/Users/jennycai/Desktop/applyeverywhere/src/resumes/" + self.id + ".pdf"
                    '/Users/jennycai/Desktop/applyeverywhere/src/resumes/resume.pdf'
                )  # for now we'll have to just change the path every time
                #   for whoever is running this code on their laptop since we don't have the same path
                time.sleep(1)
        except NoSuchElementException:
            print(f'Did not upload resume for {url}')
            pass

        # Fill autocomplete fields
        #self.fill_autocomplete_fields(url)
        #self.fill_education_fields(url)
        #self.fill_short_answers(url)

        # for answering drop down questions
        #self.fill_auth_sponsorship_questions(url)
        #self.fill_dropdowns(url)

        time.sleep(5)

        # find the submit button at the end
        #submit_button = self.driver.find_element(By.ID, "submit_app")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        print(f"finished {url}")

    def submit_application(self):
        # Submit the application form
        self.driver.find_element(By.ID, "submit_app").click()


# for profile in list_of_profiles:
#    gd = GreenHouseDriver(profile)

gd = GreenHouseDriver()
for app_url in APPLICATION_URLS:
    gd.open_application_url(app_url)
    gd.fill_application_fields(app_url)
    # gd.submit_application()
