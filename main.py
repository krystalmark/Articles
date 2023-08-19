import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.author import Author 
from lib.article import Article
from lib.magazine import Magazine

magazine1 = Magazine("Food Magazine", "Food")
magazine2 = Magazine("Car Magazine", "Car")

print(magazine1.name())  
print(magazine2.name()) 

author1 = Author("Krystal mark")
author2 = Author("Lemmy")

print(author1.name())  
print(author2.name()) 

article1 = Article(author1, magazine1, "Chess guide")
article2 = Article(author2, magazine2, "Cooking guide")

print(article1.title())  
print(article2.title())  

author1.add_article(magazine1, "Introduction to chess")
author1.add_article(magazine2, "Benefits of food")
author2.add_article(magazine1, "Love")

print([article.title() for article in author1.articles()] or "No articles")  
print([article.title() for article in author2.articles()] or "No articles")  

print([magazine.name() for magazine in author1.magazines()] or "No magazines")  
print([magazine.name() for magazine in author2.magazines()] or "No magazines")  

contributing_authors1 = [author.name() for author in magazine1.contributing_authors()]
contributing_authors2 = [author.name() for author in magazine2.contributing_authors()]

print(contributing_authors1 or "No contributors")  
print(contributing_authors2 or "No contributors")  

print([magazine.name() for magazine in Magazine.all()] or "No magazines")  

magazine_found = Magazine.find_by_name("Food Magazine")
if magazine_found:
    print(magazine_found.name())
else:
    print("Magazine not found")

print([article.title() for article in Magazine.article_titles()] or "No articles") 

print(contributing_authors1 or "No contributors")  
print(contributing_authors2 or "No contributors")
