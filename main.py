import argparse

import requests
from bs4 import BeautifulSoup
import csv
import yaml
from dotenv import load_dotenv
import os

from utils.logger import get_logger

logger = get_logger()

load_dotenv()

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def scrape_jobs(url):
    headers = {
        "User-Agent": os.getenv("USER_AGENT")
    }

    logger.info("Sending request to website")

    # response = requests.get(url, headers=headers)

    for attempt in range(3):

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                break

        except Exception as e:
            logger.error(f"Request failed attempt {attempt + 1}")

    else:
        logger.error("Website unreachable")
        return []

    if response.status_code != 200:
        logger.error("Failed to fetch webpage")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    cards = soup.find_all("div", class_="card-content")

    for card in cards:

        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    logger.info(f"{len(jobs)} jobs scraped")

    return jobs

import os

def save_to_csv(data, file_path):

    logger.info("Saving data to CSV")

    # Create folder if not exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=["title", "company", "location"])

        writer.writeheader()
        writer.writerows(data)

    logger.info("CSV file created")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--pages", type=int, help="Number of pages to scrape")

    args = parser.parse_args()

    config = load_config()

    url = config["url"]
    output = config["output_file"]

    # jobs = scrape_jobs(url)

    pages = config["pages"]

    jobs = scrape_multiple_pages(url, pages)

    if jobs:
        save_to_csv(jobs, output)
        print("Scraping completed")
    else:
        print("No data scraped")



def scrape_multiple_pages(base_url, pages):

    all_jobs = []

    for page in range(1, pages + 1):

        logger.info(f"Scraping page {page}")

        url = f"{base_url}?page={page}"

        jobs = scrape_jobs(url)

        all_jobs.extend(jobs)

    return all_jobs


if __name__ == "__main__":
    main()