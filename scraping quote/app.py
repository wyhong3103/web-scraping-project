import requests
from pages.quotes_page import QuotePage

html = requests.get("https://quotes.toscrape.com/")

quotescrapes = QuotePage(html)

for i in quotescrapes.quotes:
    print(i.tags)

