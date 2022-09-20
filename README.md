# ChatBotForSlackAwsFAQ
This is Chat Bot for Slack where it is possible to ask questions and the Bot is going to answer based on the FAQ of the official AWS documentation.

# How to start the Web Scraping
Run command: `scrapy crawl ec2 -O outputfile.json` inside `/WebScraping` directory.

# Creating a project
Creating a new Scrapy project is as simple as running `scrapy startproject tutorial`

# First spider
Spiders are classes that you define and that Scrapy uses to scrape information from a website (or a group of websites).
They must subclass Spider and define the initial requests to make, optionally how to follow links in the pages, and how to parse the downloaded page content to extract data.
This is the code for our first Spider. Save it in a file named nameOfTheSpider.py under the `tutorial/spiders` directory in your project.

# Official documentation
You can find the official Scrapy documentation in [https://docs.scrapy.org/_/downloads/en/latest/pdf/](https://docs.scrapy.org/_/downloads/en/latest/pdf/)
