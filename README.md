# Ministry of Health Web Scraping Project

## Overview
This project is a web scraping script that extracts facility details and services information from the Ministry of Health website. The data is collected and saved into an Excel file with two sheets: one for facility details and another for facility services. This README provides an overview of the project, instructions for running the script, and details about the data collected.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before running the web scraping script, make sure you have the following prerequisites installed:
- Python (>=3.6)
- Selenium
- BeautifulSoup
- Chrome WebDriver (for Selenium)

You can install the required Python packages using pip:
```bash
pip install selenium beautifulsoup4
```

## Getting Started
1. Clone this repository to your local machine:
```bash
[git clone https://github.com/your-username/ministry-of-health-web-scraper.git
](https://github.com/Kruthardh11/Python-script-web-scrapping.git)```

2. Navigate to the project directory:
```bash
cd your-folder-name
```

3. Download the Chrome WebDriver (chromedriver.exe) and place it in the project directory. You can download it from [here](https://sites.google.com/chromium.org/driver/).

## Usage
To run the web scraping script, execute the following command:
```bash
python services.py
```

The script will start scraping data from the Ministry of Health website and save it to an Excel file named `Final_data.xlsx`.

## Data Structure
The data collected from the Ministry of Health website is organized into two sheets within the Excel file:
1. **Facility Details Sheet**: This sheet contains information about different health facilities. The columns may include Facility Name, Status, Facility Code, Date Opened, Facility Type, Ownership, Address, Official Phone, Website, In-Charge Qualification, CTC ID, Nearest Facility, MSD ID, MTUHA ID, etc.

2. **Facility Services Sheet**: This sheet provides details about the services offered by the health facilities. Each service is listed with its corresponding Facility Code and a unique identifier. Columns may include Service Name and Service Description.

## Contributing
Contributions to this project are welcome! If you encounter any issues, have ideas for improvements, or would like to add new features, please open an issue or create a pull request.

---
