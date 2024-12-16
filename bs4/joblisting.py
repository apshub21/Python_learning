import requests
from bs4 import BeautifulSoup

def fetch_job_listings(url):
    # Send an HTTP request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find job listings
    jobs = []
    
    # Adjust the selectors based on the actual website structure
    job_elements = soup.find_all('div', class_='job-listing')  # Example class
    for job in job_elements:
        title = job.find('h2', class_='job-title').get_text(strip=True)  # Example class
        company = job.find('div', class_='company-name').get_text(strip=True)  # Example class
        location = job.find('div', class_='job-location').get_text(strip=True)  # Example class
        description = job.find('p', class_='job-description').get_text(strip=True)  # Example class
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'description': description
        })
    
    return jobs

def display_job_listings(jobs):
    if jobs:
        for i, job in enumerate(jobs, 1):
            print(f"Job {i}:")
            print(f"  Title: {job['title']}")
            print(f"  Company: {job['company']}")
            print(f"  Location: {job['location']}")
            print(f"  Description: {job['description']}\n")

def main():
    url = 'https://www.simplyhired.co.in/search?q=cyber+security+analyst&l=india'  # Replace with the actual URL
    jobs = fetch_job_listings(url)
    if jobs:
        display_job_listings(jobs)

if __name__ == "__main__":
    main()
