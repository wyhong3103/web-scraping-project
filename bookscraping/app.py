import requests
from pages.book_pages import BookPages
from parsers.parsers import BookParser
import logging

logging.basicConfig(format = "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",datefmt ="%d-%m-%Y %H:%M:%S" ,level = logging.INFO,filename = "logs.txt")

logger = logging.getLogger("scraping")


def get_books(page):
    logger.info(f"Loading content from page {page}...")
    html = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html").content
    book_page = BookPages(html)
    return [book_page.books,book_page.pages]



