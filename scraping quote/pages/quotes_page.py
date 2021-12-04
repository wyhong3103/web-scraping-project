#contain code that related getting data out of the quote page
from parsers.quote import QuoteParser
from locators.quote_page_locators import QuotePageLocators
from bs4 import BeautifulSoup

class QuotePage:
    def __init__(self,page):
        self.page = BeautifulSoup(page.content,"html.parser")
    
    @property
    def quotes(self):
        """
            getting all the quotes from the page(parsing every single div element that containt the quote)
        
        """
        return [QuoteParser(i) for i in self.page.select(QuotePageLocators.QUOTE)]
