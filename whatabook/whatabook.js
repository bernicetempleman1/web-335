/**
	Title: houses.js
    Author: Professor Krasso
    Date: 11 August 2022
    Description: MongoDB Shell Scripts for the houses and students collections.

      "_id": "ISBN-9781517295102",
      "title": "The Design of Web APIs",
      "author": "Arnaud Lauret",
      "genre": "Technology",
    },
    {
      "_id": "ISBN-9780321826626",
      "title": "NoSQL Distilled",
      "author": "Pramod J. Sadalage & Martin Fowler",
      "genre": "Technology",
    }


    "_id": "c1001",
      "firstName": "Hermione",
      "lastName": "Granger",
      "wishlistitems": [
        {
          "_id": "w1001",
          "customerId": "c1001",
          "bookId": "ISBN-9781517295102"
        },
        {
          "_id": "w1002",
          "customerId": "c1001",
          "bookId": "ISBN-9780321826626"
        }
      ]
    },
    {
      "_id": "c1002",
      "firstName": "Harry",
      "lastName": "Potter",
      "wishlistitems": [
        {
          "_id": "w1003",
          "customerId": "c1002",
          "bookId": "ISBN-9781517295102"
        },
        {
          "_id": "w1004",
          "customerId": "c1003",
          "bookId": "ISBN-9780321826626"
        }
      ]
    }
  ]
}

 */

// Delete the houses and students collections.
db.books.drop();
db.customers.drop();

// Create the houses and students collections using Document Validation.
db.createCollection("books", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      properties: {
        bookid: {
          bsonType: "string",
        },
        title: {
          bsonType: "string",
        },
        author: {
          bsonType: "string",
        },
        genre: {
          bsonType: "string",
        },
      },
    },
  },
});

db.createCollection("customers", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      properties: {
        customerid: {
          bsonType: "string",
        },
        firstName: {
          bsonType: "string",
        },
        lastName: {
          bsonType: "string",
        },
        wishlistitems: {
          bsonType: "array",
          properties: {
            customer_id: {
              bsonType: "string",
            },
            customerId: {
              bsonType: "string",
            },
            bookId: {
              bsonType: "string",
            },
          },
        },
      },
    },
  },
});

// Books
webapis = {
  bookid: "ISBN-9781517295102",
  title: "The Design of Web APIs",
  author: "Arnaud Lauret",
  genre: "Technology",
};

nosql = {
  bookid: "ISBN-9780321826626",
  title: "NoSQL Distilled",
  author: "Pramod J. Sadalage & Martin Fowler",
  genre: "Technology",
};

// Insert the documents.
db.books.insertOne(webapis);
db.books.insertOne(nosql);

// customers
hermione = {
  customerid: "c1001",
  firstName: "Hermione",
  lastName: "Granger",
  wishlistitems: [
    {
      wishid: "w1001",
      customerId: "c1001",
      bookId: "ISBN-9781517295102",
    },
    {
      wishid: "w1002",
      customerId: "c1001",
      bookId: "ISBN-9780321826626",
    },
  ],
};

harry = {
  customerid: "c1002",
  firstName: "Harry",
  lastName: "Potter",
  wishlistitems: [
    {
      wishid: "w1003",
      customerId: "c1002",
      bookId: "ISBN-9781517295102",
    },
    {
      wishid: "w1004",
      customerId: "c1003",
      bookId: "ISBN-9780321826626",
    },
  ],
};

// Insert the documents.
db.customers.insertOne(hermione);
db.customers.insertOne(harry);
