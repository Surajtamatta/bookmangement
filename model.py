class Book:
    def __init__(self, id, title, author, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.published_year = published_year

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
        }
