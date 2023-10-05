import requests

# Replace with your Airtable API information
base_id = "appxBfSaIMlRGrhBZ"
table_name = "tbltJNGPYAGz8IIOh"
api_key = "patGVfkDXNA8c54m9.2cbd2d736cdfcfa3c2c73aee4ed6761f2085916f908d3f803213cdcf58a62a7e"

# Define the Airtable API endpoint URL
url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Set up the headers with your API key
headers = {
    'Authorization': f'Bearer {api_key}',
}

# Send a GET request to retrieve data from the Airtable table
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process and work with the retrieved data here
    print(data)
else:
    print(f"Error: {response.status_code}")

'''
import os
from pyairtable import Api

PROFILES = {
    "first_name": "John",
    "last_name": "Smith",
    "email": "johnsmith@uni.edu",
    "phone": "415-555-8190",
    "org": "University",
    "resume": "/resume.pdf",
    "linkedin": "https://www.linkedin.com/company/dummy-test-account/",
    "website": "https://www.linkedin.com/company/dummy-test-account/",
    "github": "https://github.com/ChadLei/",
    "twitter": "",
    "location": "San Francisco, California, United States",
    "grad_month": "06",
    "grad_year": "2024",
    "university": "University, USA",
    "most_recent_employer": "",
    "cover_letter": "Having honed my skills in various software projects, I believe in the power of code to drive transformative change, and I am always eager to contribute to environments that champion creativity and problem-solving.",
}


class Profile:
    def __init__(self, record):
        for key, value in record.items():
            setattr(self, key, value)

    def __str__(self):
        attributes = []
        for key, value in self.__dict__.items():
            attributes.append((key, value))
        return ", ".join([f"{key}: {value}" for key, value in attributes])


api = Api(
    os.environ[
        "patGVfkDXNA8c54m9.2cbd2d736cdfcfa3c2c73aee4ed6761f2085916f908d3f803213cdcf58a62a7e"
    ]
)
table = api.table("appxBfSaIMlRGrhBZ", "tbltJNGPYAGz8IIOh")  # base ID, table ID
records = table.all()  # gets a list of dictionaries, where every dictionary is a record


# TODO: Rona, can you run this code, so we can see what the records look like?
for record in records:
    new_record = Profile(record)  # make a Profile type from user-submitted information
    # probably will need logic here to run the greenhouse bot on the record

'''