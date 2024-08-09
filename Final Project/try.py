# import requests
# from bs4 import BeautifulSoup


# # Making a GET request
# r = requests.get('https://www.hindustantimes.com/')

# # check status code for response received
# # success code - 200
# print(r)

# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())


# import requests
# from bs4 import BeautifulSoup

# # Define headers to mimic a browser
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# # Making a GET request
# r = requests.get('https://www.hindustantimes.com/', headers=headers)

# # Check status code for response received
# if r.status_code == 200:
#     print("Request successful")
#     # Parsing the HTML
#     soup = BeautifulSoup(r.content, 'html.parser')
#     print(soup.prettify())
# else:
#     print(f"Failed to retrieve data: {r.status_code}")



import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = 'https://timesofindia.indiatimes.com/'

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trying a different class name or structure
    # Sometimes headlines are under <span> or <h2> tags with different class names
    headlines = soup.find_all('span', class_='w_tle')  # Try other common headline classes
    
    # If headlines are empty, print a message
    if not headlines:
        print("No headlines found. The class name might have changed.")
    else:
        # Print out each headline
        for idx, headline in enumerate(headlines):
            print(f"{idx + 1}. {headline.get_text(strip=True)}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
