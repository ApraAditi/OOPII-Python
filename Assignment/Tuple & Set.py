#Tuple
books = (
    ("To kill a Mockingbird", "Harper Lee", 1960),
("1984", "George Orwell", 1949),
("The Great Gastby", "F. Scott Fitzgerald", 1925)
)
#set
tags = {"classic", "dystopain", "novel", "literature"}

#a. Access the books tuple
print("The second book's author from the books tuple is: ",books[1][1])

#b. Add a new record for the book tuple
new_book = (("Brave New World", "Aldous Huxley", 1932),)
books +=new_book
print("\nAfter add new record: ",books)

#c. Unpack the details of the third book into separate variables
title, author, year = books[2]
print(f"\nThe book {title} by {author} published in {year}\n")

#d. d. Loop through the books tuple
for book in books:
    print("The book's titles are: ",book[0])

#e. Add a new tag "sci-fi"
tags.add("si-fi")
print("\n",tags)

#f. Use a method to remove the tag "novel"
tags.remove("novel")
print("\n",tags)