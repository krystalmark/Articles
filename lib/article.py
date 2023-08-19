
class Article:
    _all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all.append(self)


    def title(self):
        return self._title

    @classmethod
    def all(cls):
        return cls._all

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
    


from lib.article import Article

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
    
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazines = []
        for article in self._articles:
            magazine = article.magazine()
            if magazine not in magazines:
                magazines.append(magazine)
        return magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

    def topic_areas(self):
        categories = []
        for article in self._articles:
            magazine = article.magazine()
            category = magazine.category()
            if category not in categories:
                categories.append(category)
        return categories
