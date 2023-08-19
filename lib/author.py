class Author:
    _authors = []

    def __init__(self, name):
        self._name = name
        self._articles = []
        self._authors.append(self)

    def name(self):
        return self._name

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def articles(self):
        return self._articles

    def magazines(self):
        return [article.magazine() for article in self._articles]

    @classmethod
    def all(cls):
        return cls._authors


from .article import Article
