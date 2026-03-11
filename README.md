# Web Scraper Automation

A **production-ready Python automation script** that scrapes job listings from a website and exports structured data into a CSV file.

This project demonstrates **professional automation practices** such as configuration management, environment variables, logging, retry handling, and modular project structure. It is designed to be **freelancer-deliverable and client-friendly**.

---

# Project Demo

GitHub Repository

```
https://github.com/poojashriram-1/web_scraper_automation
```

Example Output File

```
data/jobs.csv
```

Example CSV Data

```
title,company,location
Python Developer,ABC Corp,New York
Backend Engineer,XYZ Ltd,Remote
```

---

# Features

• Automated website scraping
• Export scraped data to CSV
• Pagination support (scrape multiple pages)
• YAML configuration file
• Environment variable support
• Logging system
• Retry mechanism for failed requests
• Command-line arguments
• Modular folder structure
• Ready for freelance or production use

---

# Technologies Used

```
Python
Requests
BeautifulSoup
python-dotenv
PyYAML
Logging
```

---

# Project Structure

```
web_scraper_automation
│
├── main.py
├── config.yaml
├── .env
├── requirements.txt
├── README.md
│
├── data
│   └── jobs.csv
│
├── logs
│   └── app.log
│
├── utils
│   ├── scraper.py
│   ├── exporter.py
│   └── logger.py
│
└── tests
    └── test_script.py
```

---

# Installation

Clone the repository

```
git clone https://github.com/poojashriram-1/web_scraper_automation.git
```

Navigate to the project folder

```
cd web_scraper_automation
```

Create a virtual environment

```
python -m venv venv
```

Activate the virtual environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Configuration

Edit the `config.yaml` file.

Example configuration

```
url: https://realpython.github.io/fake-jobs/
output_file: data/jobs.csv
pages: 3
```

| Parameter   | Description               |
| ----------- | ------------------------- |
| url         | Website to scrape         |
| output_file | CSV output location       |
| pages       | Number of pages to scrape |

---

# Environment Variables

Create a `.env` file.

Example

```
USER_AGENT=Mozilla/5.0
```

This helps prevent websites from blocking automated requests.

---

# Running the Script

Run the scraper

```
python main.py
```

The script will:

1. Load configuration
2. Send request to website
3. Extract job data
4. Save results to CSV
5. Write logs

---

# Command Line Arguments

Override pages from command line

```
python main.py --pages 5
```

---

# Output

Generated CSV file


Screnshots


![Output Screenshot](csv_screenshot.PNG)

![Output Screenshot](logs.PNG)


```
data/jobs.csv
```

Example data

```
title,company,location
Python Developer,ABC Corp,New York
Backend Engineer,XYZ Ltd,Remote
```

---

# Logging

Log file location

```
logs/app.log
```

Example log output

```
Script started
Request sent to website
Page 1 scraped
50 jobs collected
CSV file generated
```

---

# Error Handling

If a request fails, the scraper retries automatically.

```
Retry 1
Retry 2
Retry 3
```

Errors are recorded in the log file.

---

# Testing

Basic tests are available in

```
tests/test_script.py
```

---

# Use Cases

• Job market analysis
• Competitor monitoring
• Lead generation
• Data collection for analytics
• Automated reporting

---

# Freelancer Value

This project demonstrates:

• Clean automation architecture
• Configuration driven scripts
• Logging and monitoring
• Error handling and retries
• Production ready structure

These qualities make it **client-ready automation software**.

---

# Author

Python Automation Project
Created for **freelance automation portfolio**
