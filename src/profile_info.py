import requests
import os

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
        self.gpa = fields["GPA"]

        self.cover_letter = fields["Cover Letter"]

        r = requests.get(fields["Resume"][0]["url"], allow_redirects=True)
        # print(r.content)
        with open(
            os.path.abspath(os.curdir) + "/resumes/" + self.id + ".pdf", "wb"
        ) as pdf_file:
            pdf_file.write(response.content)

        # open("resumes/" + self.id + ".pdf", "wb").write(r.content)
        self.resume = "resumes/" + self.id + ".pdf"  # link to resume

    def __str__(self):
        attributes = []
        for key, value in self.__dict__.items():
            attributes.append((key, value))
        return ", ".join([f"{key}: {value}" for key, value in attributes])


response = requests.get(url, headers=headers)
# if requests.exceptions.ConnectionError:
#     response.status_code = "Connection refused"

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
