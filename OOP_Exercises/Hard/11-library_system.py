class Book:
    def __init__(self,title,author,available):
        self.title = title
        self.author = author
        # self.amount = amount
        self.available = available
        
    def info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")
        if self.available == 'Yes':
            print("Available: Yes")
            
class Library:
    books = []
    
    
    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        # amount = input("Amount: ")
        available = input("Available: ")
        new_book = Book(title,author,available)
        self.books.append(new_book)
    
    # will show every books even which one is available and which one isn't also the total number of available and uavailable books
    def show_books(self):
        
        total = len(self.books)
        available_books = 0
        not_available = 0
        
        print("\n--- Book Catalog ---\n")
        
        for book in self.books:
            print(vars(book))
            if book.available == 'Yes':
                available_books += 1
            else:
                not_available += 1
    

        print("\n--- Summary Metrics ---")    
        print("Total Books: ",total)
        print("Available Books: ",available_books)
        print("Not Available Books: ",not_available)
    
    #need to search through the library's list of book objects and compare with the title(looping over list of objects)
    def borrow_books(self,name):
        for book in self.books:
            if name == book.title and book.available == 'Yes':
                book.available = 'No'
                print(f"Book {book.title} has been lent.")
            
        
    
    #when the book is returned it's status will be available = True 
    def return_books(self,name):
        for book in self.books:
            if name == book.title and book.available == "No":
                book.available = "Yes"
                print(f"Book {book.title} has been returned.")
    
'''
Future improvements:
1.Search by title
2.Prevent Duplicate books from entering the list
3.Give every book a unique ID
'''



class App:
    def __init__(self):
        self.running = True
        self.Library = Library()
        
    def run(self):
        self.__show_welcome()
        while self.running:
            self.__show_menu()
            choice = input("\n->").strip()
            self.__handle_choice(choice)
            
    def __show_welcome(self):
        print("-"*30)
        print("Welcome to Book and Quele Library")
        print("-"*30)
        
    def __show_menu(self):
        print("\n1.Librarian\n2.Borrower")
        
    def __handle_choice(self,choice):
        if choice == '1':
            self.rotation = True
            while self.rotation:
                print("Librarian can Add or Show books")
                print("1. for adding book\n2. for showing books.\n3. for exit")
                lchoice = input("\n-->").strip()
                if lchoice == '1':
                    self.Library.add_book()
                if lchoice == '2':
                    self.Library.show_books()
                if lchoice == '3':
                    self.rotation = False
                
        if choice == '2':
            self.rotation = True
            while self.rotation:
                print("Borrower can borrow or return books")
                print('\n.1 for borrowing new books\n2. for returning books\n3. for exit')
                bchoice = input('\n-->').strip()
                if bchoice == '1':
                    self.Library.borrow_books(input("Name of the book: "))
                if bchoice == '2':
                    self.Library.return_books(input("Name of the book: "))
                if bchoice == '3':
                    self.rotation = False
                    
        if choice == '3':
            self.running = False
                
                
if __name__ == "__main__":
    app = App()
    app.run()
        