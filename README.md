# Amazon Scrapy Project

This project scrapes product information from Amazon using the Scrapy framework in Python. It extracts product details such as title, price, ratings, author and description.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements
To install and run this project, you'll need the following:
- Python 3.X
- Scrapy Python library

## Installation
To install and setup this project on your local machine, perform the following steps:

1. Clone this repository: 
```bash
git clone https://github.com/Manthan-hub/Amazon-Product-Scraper.git
```

2. Navigate into the project directory:
```bash
cd amazon_scraper
```

3. Installation of required Python libraries:
```bash
pip install -r requirements.txt
```

## Usage
After the installation, to start the scraping process, you can run the following command in your terminal:

For JSON Output:

```bash
scrapy crawl amazon -o amazon.json
```

For CSV Output:

```bash
scrapy crawl amazon -o amazon.csv
```
