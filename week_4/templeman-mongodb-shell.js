/**
 * Author: Bernice Templeman
 * Date: 6/15/2024
 * File Name: templeman-mongodb-shell.js
 * Description: MongoDB Shell Scripts for the users collection
 */

/**
 * 1. Review Guides 1, 2, and 3 in course document.
 * 2. Create a new database named web335DB with a collection named users.
 * 3. Create a new custom role named web335Admin.
 * 4. Create a new database user named web335_user with a password and assign it to the custom role from step 3.
 * 5. Download and install mongosh. Test the software’s installation by running the command: mongosh --help.
 * 6. Load the user.js script from week four of the course’s GitHub repository.
 *    use web335DB
 *    load("users.js")
 * 7. Example of user from users.js:
 *
    bach = {
        "firstName": "Johann",
        "lastName": "Bach",
        "employeeId": "1007",
        "email": "jbach@me.com",
        "dateCreated": new Date()
    }
MongoDB Shell:
    mongosh "mongodb+srv://bellevueuniversity.lftytpq.mongodb.net/" --apiVersion 1 --username <db_username>
 */

// Display all users in the collection.
db.users.find()

// Display the user with the email address jbach@me.com.
db.users.findOne({"email": "jbach@me.com"})

// Display the user with the last name Mozart.
db.users.findOne({"lastName": "Mozart"})

// Display the user with the first name Richard.
db.users.findOne({"firstName": "Richard"})

// Display the user with employeeId 1010.
db.users.findOne({"employeeId": "1010"})