class user():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}" 


class books():
   def __init__(self,title,author,isbn,available):
      self.title = title
      self.author = author
      self.isbn = isbn
      self.available = available

      def __str__(self):
         return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"

class library():
    def __init__(self):
      self.books = []

    def add_books(self,books):
      self.books.append(books)
      print(f"Book added: {books}")

    def lent_books(self,books):
      if books in self.books:
         self.books.remove(books)
         print(f"Book lent: {books}")
      else:
         print("Book not available")

    def return_books(self,books):
       self.books.append(books)
       print(f"Book returnded: {books}")

    def display_books(self):
       for book in self.books:
          print(book)
    
# Example usage
lib = library()
book1 = books("1984", "George Orwell", "1234567890", True)
book2 = books("To Kill a Mockingbird", "Harper Lee", "0987654321", True)

lib.add_books(book1)
lib.add_books(book2)

lib.display_books()

lib.lent_books(book1) 
lib.display_books()
lib.return_books(book1)
lib.display_books()
lib.lent_books(book2)
lib.display_books()
lib.return_books(book2)
lib.display_books()
lib.lent_books(book1)  # Attempt to lend a book that is not available
lib.display_books()
lib.return_books(book1)  # Return the book again

lib.display_books()  # Display books after returning
lib.lent_books(book2)  # Attempt to lend a book that is not available

lib.display_books()  # Display books after lending
lib.return_books(book2)  # Return the book again                    