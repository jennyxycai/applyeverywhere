from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the webdriver executable (e.g., chromedriver)
driver_path = '/Users/jennycai/Desktop/chromedriver_mac64'

# Set the URL of the greenhouse job application page
application_url = 'https://example.com/job-application'

# Set up the driver (assuming you're using Chrome, but you can use others like Firefox)
driver = webdriver.Chrome(driver_path)

# Open the Greenhouse job application page
driver.get(application_url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
wait.until(EC.presence_of_element_located((By.ID, 'form_field_id')))

# Fill in the information fields
driver.find_element(By.ID, 'form_field_id').send_keys('Field Value')

# Submit the application form
driver.find_element(By.ID, 'submit_button_id').click()

# Close the browser
driver.quit()
