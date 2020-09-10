import wikipedia
from random import choice
import time
class Crawly(object):
    
    numberOfChars = 100 # Not sure now many I can fit

    def __init__(self):
        self.current_article = "Wikipedia"
        wikipedia.set_rate_limiting(True) # Rate limit

    def get_next_page(self):
        try:

            page = wikipedia.page(self.current_article) # Get the current page

        except:
            page = wikipedia.random() # random page

        try:

            self.current_article = choice(page.links) # Randomly choose a link to follow

            summary = self.get_summary(self.current_article)

        except: # Must have failed, choose a random article

            noArticle = True
            while noArticle:
                try:
                    self.current_article = wikipedia.random()

                    summary = self.get_summary(self.current_article)

                    noArticle = False
                except:
                    pass

        return {'title' : self.current_article, 'summary' : summary}

    def get_summary(self, article):
        return wikipedia.summary(article, sentences = 1, chars = self.numberOfChars)

if __name__ == "__main__":
    
    w = Crawly()

