"""
Author: Bernice Templeman
Date: 07/23/2024
File Name: HouseArcadia_whatabook.py
Description: Python program that connects to web335DB database

Console Application Requirements:
1. Connect to your MongoDB database.
2. Display a list of books.
Format the output so it is easy to read.
3. Display a list of books by Genre.
For this requirement, supply the user with a list of genre choices and
display the appropriate books based on their selection.
4. Display a customers wishlist by customerId.
For this requirement, prompt the user to enter a customerId (c1007, c1008, or c1009) and display the appropriate wishlist.
5. Add basic error handling to account for an invalid customerId (hint: use an if…else or switch statement).
"""

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to
client = MongoClient(
    'mongodb+srv://web335_user:s3cret@bellevueuniversity.lftytpq.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity')

# Configure a variable to access the web335DB
db = client['web335DB']

def main_menu():
  print()
  print("Select: ")
  print("1. View All Books")
  print("2. View Books by Genre")
  print("3. View wishlist by Customer Id")
  print("4. Exit")

  choice = input("Please Select a choice: ")

  if choice == '1':
    print_books()
  elif choice == '2':
    genre_menu()
  elif choice == '3':
    print_wishlist()
  elif choice == '4':
    print("Thank you")
    exit()
  else:
    print("Invalid choice.")
  main_menu()

def print_books():
    # Print all documents in books collection
    print("\nList of all books:")
    for book in db.books.find({}, {'_id':0,'title': 1, 'author':1, 'genre': 1}):
        print(book)

def genre_menu():
  print()
  print("Select a Genre to Display Books")
  print("1. Technology")
  print("2. Science Fiction")
  print("3. Military History")
  print("4. Sports")
  print("5. Fantasy")
  print("6. Mystery")
  print("7. Romance")
  print("8. Exit")

  choice = input("Please Select a choice: ")

  if choice == '1':
    genre = "Technology"
  elif choice == '2':
    genre = "Science Fiction"
  elif choice == '3':
    genre = "Military History"
  elif choice == '4':
    genre = "Sports"
  elif choice == '5':
    genre = "Fantasy"
  elif choice == '6':
    genre = "Mystery"
  elif choice == '7':
    genre = "Romance"
  elif choice == '8':
    print("Thank you")
    exit()
  else:
    print("Invalid choice.")
    genre_menu()

  print("\nList of books in genre:", genre)
  for book in db.books.find({ 'genre': genre}, {'_id':0,'title': 1, 'genre': 1}):
    print(book)

def print_wishlist():
    # Display list of books by genre
    customer = input ('Please enter your customer id: ')
    if db.customers.count_documents({ 'customerId': customer }, limit = 1) != 0:
      print("Wishlist for customer ID")
      for wishlistitems in db.customers.find({'customerId': customer}, {'_id':0,'wishlistitems': 1}):
            print(wishlistitems)
    else:
        print("Please enter a valid customer id.")

def main():
  main_menu()

if __name__ == "__main__":
  main()

