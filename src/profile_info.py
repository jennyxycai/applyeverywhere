import os
from pyairtable import Api

PROFILES = {
    "first_name": "John",
    "last_name": "Smith",
    "email": "johnsmith@uni.edu",
    "phone": "415-555-8190",
    "org": "University",
    "resume": "/resume.pdf",
    "resume_textfile": "",
    "linkedin": "https://www.linkedin.com/company/dummy-test-account/",
    "website": "https://www.linkedin.com/company/dummy-test-account/",
    "github": "https://github.com/ChadLei/",
    "twitter": "",
    "location": "San Francisco, California, United States",
    "grad_month": "06",
    "grad_year": "2024",
    "university": "University, USA",
    "most_recent_employer": "University",
    "reason_of_interest": "Having honed my skills in various software projects, I believe in the power of code to drive transformative change, and I am always eager to contribute to environments that champion creativity and problem-solving.",
}

api = Api(
    os.environ[
        "patGVfkDXNA8c54m9.2cbd2d736cdfcfa3c2c73aee4ed6761f2085916f908d3f803213cdcf58a62a7e"
    ]
)
table = api.table("appxBfSaIMlRGrhBZ", "tbltJNGPYAGz8IIOh")  # base ID, table ID
records = table.all()  # gets a list of dictionaries, where every dictionary is a record


class Profile:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


for record in records:
    new_record = Profile(record)  # make a Profile type from user-submitted information
    # probably will need logic here to run the greenhouse bot on the record
