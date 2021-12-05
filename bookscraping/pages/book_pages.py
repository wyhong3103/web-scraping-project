from bs4 import BeautifulSoup
from locators.book_page_locators import BookPageLocators
from parsers.parsers import BookParser
import re
import logging

logger = logging.getLogger("scraping.all_books_page")


class BookPages:
    def __init__(self,page):
        self.page = BeautifulSoup(page,"html.parser")
    
    @property
    def books(self):
        logger.debug(f"Finding all books in the page using {BookPageLocators.BOOK_PAGE_LOCATOR}...")
        return [BookParser(i) for i in self.page.select(BookPageLocators.BOOK_PAGE_LOCATOR)]
    
    @property
    def pages(self):
        logger.debug("Finding all number of catalogue pages available...")
        expression = "of ([0-9]+)"
        return re.search(expression,self.page.select_one(BookPageLocators.NUMBER_OF_PAGES).string)[1]
