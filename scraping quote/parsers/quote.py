from locators.quote_locators import QuoteLocators

class QuoteParser:
        def __init__(self,parent):
            #parent is going to be the div we will be receiving
            self.parent = parent
        
        def __repr__(self):
            return f"<Quote {self.content}, by {self.author}>"

        @property
        def content(self):
            return self.parent.select_one(QuoteLocators.CONTENT).string
        
        @property
        def author(self):
            return self.parent.select_one(QuoteLocators.AUTHOR).string
        
        @property
        def tags(self):
            return [i.string for i in self.parent.select(QuoteLocators.TAGS)]
