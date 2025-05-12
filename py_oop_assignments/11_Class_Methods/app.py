# Book naam ki class banai gayi hai
class Book:

    total_books = 0  # total_books aik class variable hai

    def __init__(self):
        Book.increment_book_count()  # jab book banai jaye to count barh jaye


    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # total_books ka value +1 hota hai


# yahan aik book banai gayi hai (assignment ke mutabiq sirf aik)
Book()


# blank line for better readability        
print()


# total books ka count print kiya gaya hai
print("Total number of books:", Book.total_books)
