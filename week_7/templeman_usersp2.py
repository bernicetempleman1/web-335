"""
Author: Bernice Templeman
Date: 07/08/2024
File Name: templeman_usersp2.py
Description: Python program that connects to web335DB database
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# 2 Build a connection string to connect to
client = MongoClient(
    'mongodb+srv://web335_user:s3cret@bellevueuniversity.lftytpq.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity')

# Configure a variable to access the web335DB
db = client['web335DB']

# 3 Write the Python code to create a new user document.
harry = {
    "firstName": "Harry",
    "lastName": "Potter",
    "employeeId": "1013",
    "email": "harry@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
harry_user_id = db.users.insert_one(harry).inserted_id

print("New user document id:")
print(harry_user_id)
print()

# 4 Prove the document was created. The insert worked by searching the collection for the document
print("Inserted document:")
print(db.users.find_one({"employeeId": "1013"}))
print()
# 5. Write the Python code to update the email address of the document you created in step 3.
db.users.update_one(
    {"employeeId": "1013"},
    {
        "$set": {
            "email": "harry.potter@me.com"
        }
    }
)

# 6 Prove the update worked by searching the collection for the user by employeeId
print("Updated user document:")
print(db.users.find_one({"employeeId": "1013"}))
print()
# 7. Write the Python code to delete the document that was created in step 3.
# Build a query to remove a user document
result = db.users.delete_one({
    "employeeId": "1013"
})

# Display the results of the query
print("Deleted document:")
print(result)
print()
# 8. Write the Python code to prove the document was deleted.
# Prove the delete worked by searching the collection for the deleted document
print("Deleted document in the database:")
print(db.users.find_one({"employeeId": "1013"}))
