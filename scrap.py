import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.instagram.com/janny__/"
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the website
links = soup.find_all()

# Loop through the links and extract the ones that start with "cnd"
for link in links:
    if link.has_attr("href"):
        href = link["href"]
        print(f"Found link: {href}")
        if href.startswith("cnd"):
            print(f"Matched link: {href}")


            

