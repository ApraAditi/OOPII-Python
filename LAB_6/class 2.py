from datetime import date

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

    def is_new_release(self):
        current_year = date.today().year
        if self.publication_year >= current_year - 1:
            print(f"{self.title} is a new release.")
        else:
            print(f"{self.title} is not a new release.")

# Creating an instance of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("Artificial Intelligence: A Modern Approach", "Stuart Russell and Peter Norvig", 2024)

# Displaying book details and checking if they are new releases
print("Book 1 Details:")
book1.display_details()
book1.is_new_release()

print("\nBook 2 Details:")
book2.display_details()
book2.is_new_release()
