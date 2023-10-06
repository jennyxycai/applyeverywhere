import requests

# Replace with your Airtable API information
base_id = "appxBfSaIMlRGrhBZ"
table_name = "tbltJNGPYAGz8IIOh"
api_key = (
    "patGVfkDXNA8c54m9.2cbd2d736cdfcfa3c2c73aee4ed6761f2085916f908d3f803213cdcf58a62a7e"
)

# Define the Airtable API endpoint URL
url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

# Set up the headers with your API key
headers = {
    "Authorization": f"Bearer {api_key}",
}

# Send a GET request to retrieve data from the Airtable table


class Profile:  # make Profile class
    def __init__(self, record):
        fields = record["fields"]
        self.id = record["id"]
        self.first_name = fields["First Name"]
        self.last_name = fields["Last Name"]
        self.phone_number = fields["Phone Number"]
        self.email = fields["Email"]
        self.organization = fields["School"]
        self.linkedin = fields["LinkedIn Profile"]
        self.graduation_date = fields[
            "Graduation Date"
        ]  # need to figure out how to input a date into greenhouse
        self.expertise = fields["Experience Level"]
        self.location = fields["Location"]
        self.github = fields["GitHub Profile"]
        self.current_auth = fields[
            "Do you currently have authorization to work in the US?"
        ]
        self.visa_sponsor = fields[
            "Do you now or will you in the future require visa sponsorship to work in the US?"
        ]

        self.cover_letter = fields["Cover Letter"]

        r = requests.get(fields["Resume"][0]["url"], allow_redirects=True)
        open("resumes/" + self.id + ".pdf", "wb").write(r.content)
        self.resume = "resumes/" + self.id + ".pdf"  # link to resume

    def __str__(self):
        attributes = []
        for key, value in self.__dict__.items():
            attributes.append((key, value))
        return ", ".join([f"{key}: {value}" for key, value in attributes])


response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    # Process and work with the retrieved data here
    print(data)
    table = data["records"]
    list_of_profiles = []
    for id in table:
        print(id)
        list_of_profiles.append(
            Profile(id)
        )  # for every record, make a new Profile instance and add it to the list of profiles
else:
    print(f"Error: {response.status_code}")


"""
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

"""
