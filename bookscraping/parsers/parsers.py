from locators.book_locators import BookLocators
import re
import logging

logger = logging.getLogger("scraping.books_parser")




class BookParser:
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f"Book Title:\"{self.title}\"\nBook Prices:{self.price}\nBook Rating:{self.rating} stars"


    @property
    def title(self):
        logger.debug(f"Finding the title of the book using {BookLocators.TITLE}...")
        return self.parent.select_one(BookLocators.TITLE).attrs["title"]
    
    @property
    def price(self):
        logger.debug(f"Finding the price of the book using {BookLocators.PRICE}...")
        expression = "£([0-9]+\.[0-9]+)"
        price_string = self.parent.select_one(BookLocators.PRICE).string
        return float(re.search(expression,price_string)[1])
    
    @property
    def rating(self):
        dic_rating = {
            "One" : 1,
            "Two" : 2,
            "Three" : 3,
            "Four" : 4,
            "Five" : 5
        }
        
        logger.debug(f"Finding the rating of the book using {BookLocators.RATING}...")
        stars = dic_rating[self.parent.select_one(BookLocators.RATING).attrs["class"][1]]
        logger.debug(f"Converting alphabetical rating into number rating...")
        return stars



