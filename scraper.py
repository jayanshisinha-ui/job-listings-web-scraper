import requests
from bs4 import BeautifulSoup
from utils import save_to_csv
from config import BASE_URL, OUTPUT_FILE

def fetch_page(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None

def parse_jobs(html):

    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:

        title = job.find("h2", class_="title")
        company = job.find("h3", class_="company")
        location = job.find("p", class_="location")

        job_data = {

            "Job Title": title.text.strip() if title else "N/A",

            "Company": company.text.strip() if company else "N/A",

            "Location": location.text.strip() if location else "N/A"

        }

        jobs.append(job_data)

    return jobs

def main():

    print("Starting Job Scraper...")

    html = fetch_page(BASE_URL)

    if html:

        job_data = parse_jobs(html)

        save_to_csv(job_data, OUTPUT_FILE)

        print("Scraping completed successfully!")

if __name__ == "__main__":
    main()