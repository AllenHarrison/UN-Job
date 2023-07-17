import requests
from bs4 import BeautifulSoup
import json
# define the URL
url = "https://www.unjobnet.org/jobs?orgtypes%5B0%5D=United+Nations+System&keywords=&orderby=closing"

# send a GET request to the URL
response = requests.get(url)

html_string = response.text

html_string = html_string.split("Vue.createApp({ data: function() { return { jobs :")[1]
html_string = html_string.split(", pager : ")[0]

jobs_data_list = json.loads(html_string)

for job in jobs_data_list:
    print(job["Title"])
    print(job["ShortName"] + "-" + job["LongName"])
    soup = BeautifulSoup(job["Deadline"], 'html.parser')
    print(soup.get_text())
    job_link = "https://www.unjobnet.org/jobs/detail/" + job["JobID"]
    print(job_link)


'''
# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
# find all job postings
job_postings = soup.find_all("div", class_="job")

# loop through the job postings
for job in job_postings:
    # get the job information
    job_title = job.find("a", class_="py-2 h6 fw-bold").text.strip()
    organization = job.find("a", class_="link-dark").text.strip()
    deadline = job.find("span", class_="text-danger font-weight-bold").text.strip()
    job_link = "https://www.unjobnet.org" + job.find("a", class_="py-2 h6 fw-bold")["href"]

    # print the job information
    print("Job Title:", job_title)
    print("Organization:", organization)
    print("Deadline:", deadline)
    print("Job Link:", job_link)
    print("--------------------")
'''
