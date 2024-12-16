#-------------------- NOT WORKING PROPERLY----------------------------

import requests
from bs4 import BeautifulSoup

def get_weather(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    weather = {}

    # Adjust the selectors based on the website structure
    weather['temperature'] = soup.find('span', class_='current-temp').get_text()
    weather['condition'] = soup.find('span', class_='current-condition').get_text()

    return weather

def display_weather(weather):
    if weather:
        print(f"Current Temperature: {weather['temperature']}")
        print(f"Condition: {weather['condition']}")

def main():
    url = 'https://weather.com/weather/today/l/Manhattan+NY?canonicalCityId=fc47c333c5d13e34e34c9fdb6e047ceb70f7891e01bc9e1d574b5f93f58aa76d'  # Replace with the actual URL
    weather = get_weather(url)
    display_weather(weather)

if __name__ == "__main__":
    main()
