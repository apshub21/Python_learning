import requests
from bs4 import BeautifulSoup

def get_vaccine_data(url):
    # Send an HTTP request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the vaccine data in the HTML
    # This part will depend on the structure of the website you are scraping
    # Here we assume the data is in a table
    data = []
    table = soup.find('table')  # Find the table in the HTML
    if table:
        rows = table.find_all('tr')  # Find all rows in the table
        for row in rows:
            cols = row.find_all('td')  # Find all columns in the row
            cols = [col.text.strip() for col in cols]  # Extract text and strip extra spaces
            data.append(cols)
    return data

def display_vaccine_data(data):
    # Print the vaccine data
    for row in data:
        print('\t'.join(row))

def main():
    url = 'https://www.dshs.texas.gov/immunizations/public/vis'  # Replace with the actual URL
    vaccine_data = get_vaccine_data(url)
    if vaccine_data:
        display_vaccine_data(vaccine_data)

if __name__ == "__main__":
    main()
