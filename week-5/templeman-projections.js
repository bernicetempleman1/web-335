/**
 * Author: Bernice Templeman
 * Date: 6/29/2024
 * File Name: templeman-projections.js
 * Description: MongoDB operations
 *
 */

// Check if user exists
db.users.findOne({lastName: 'Templeman'})

/**
 * Insert the newly user document.
 */

db.users.insertOne({ 'firstName':'Bernice', 'lastName': 'Templeman', 'employeeId': '10101010', 'email': 'btempleman@me.com', 'dateCreated': new Date()});

// verify user exists
db.users.findOne({lastName: 'Templeman'})

/**
 * Update the email address for Mozart
 */
// verify current email
db.users.findOne({lastName: 'Mozart'}, { _id: 0, firstName: 1, lastName: 1, email: 1})

// update email
db.users.updateOne({lastName: 'Mozart'}, {$set: {email: 'mozart@me.com'}})

// verify new email
db.users.findOne({lastName: 'Mozart'}, { _id: 0, firstName: 1, lastName: 1, email: 1})

// Display all users in the collection" use projection for firstName, lastName, and email
// $projection  https://www.mongodb.com/docs/manual/reference/operator/projection/positional/
// $filter (aggregation) https://www.mongodb.com/docs/manual/reference/operator/aggregation/filter/#mongodb-expression-exp.-filter
db.users.aggregate ({ $project: { _id: 0, firstName: 1, lastName: 1, email: 1 } })

