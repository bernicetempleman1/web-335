"""
Author: Bernice Templeman
Date: 07/06/2024
File Name: templeman_usersp1.py
Description: Python program that connects to web335DB database
"""

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.lftytpq.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

# Configure a variable to access the web335DB
db = client['web335DB']

print("All users in the collection:")
# Call the find function to display all of the users in the collection
for user in db.users.find({}, {"_id": 1, "firstName": 1, "lastName": 1, "employeeId": 1, 'email': 1, 'dateCreated': 1}):
    print(user)

print()
print("User with the employeeID of 1011:")
# Call the find_one function to display a user document where the employeeId is 1011.
print(db.users.find_one({"employeeId": "1011"}))

print()
print("User with the lastName of Mozart:")
# Call the find_one function to display a user document where the lastName is Mozart.
print(db.users.find_one({"lastName": "Mozart"}))
