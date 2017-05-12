class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.book_list = []
        # List of Book objects
        
    def get_books(self):
        return self.book_list
        
    def search_books(self, title=None, author=None):
        results = []
        for book in self.book_list:
        # Reference each Book Object
            if title is None:
                if author.name.lower() in book.author.name.lower():
                    # if title/author from search_books matches title/author of Book object
                    results.append(book)
            elif author is None:
                if title.lower() in book.title.lower():
                    # if title/author from search_books matches title/author of Book object
                    results.append(book)
        return results
                
                
    def add_book(self, book):
        self.book_list.append(book)


class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.book_list = []


    def get_books(self):
        return self.book_list


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.book_list.append(self)