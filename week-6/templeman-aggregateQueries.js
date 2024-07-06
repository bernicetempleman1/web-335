/**
	  Title: templeman-aggregateQueries.js
    Author: Bernice Templeman
    Date: 6 July 2024
    Description: MongoDB Shell Scripts for the houses and students collections.
 */

// Display all students.
db.students.find();

// Add a new student. Ensure the fields in the new document match the existing fields in the collection.
db.students.insertOne({
  firstName: "Roger",
  lastName: "Moore",
  studentId: "s007",
  houseId: "h1007",
});

//Next, prove the new student was added successfully.
db.students.findOne({ lastName: "Moore" });

//Update one of the properties from the student you added.
db.students.updateOne({ lastName: "Moore" }, { $set: { houseId: "h1010" } });

//Next, prove the property was updated successfully.
db.students.findOne({ lastName: "Moore" });

// Delete the student you created in step
db.students.deleteOne({ lastName: "Moore" });

// Next, prove the student was removed successfully.
db.students.findOne({ lastName: "Moore" });

// Display all students by house. The order should be: Houses Students
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student",
    },
  },
  { $unwind: "$student" },
  {
    $group: {
      _id: { houseId: "$houseId" },
      students: {
        $push: {
          firstName: "$student.firstName",
          lastName: "$student.lastName",
        },
      },
    },
  },
  {
    $project: {
      _id: 0,
      houseId: "$_id.houseId",
      students: "$students",
    },
  },
  { $sort: { houseId: 1 } },
]);

// Display all students in house Gryffindor. The order should be: Gryffindor Students
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student",
    },
  },
  { $match: { houseId: "h1007" } },
  { $unwind: "$student" },
  {
    $group: {
      _id: { houseId: "$houseId" },
      students: {
        $push: {
          firstName: "$student.firstName",
          lastName: "$student.lastName",
        },
      },
    },
  },
  {
    $project: {
      _id: 1,
      students: "$students",
    },
  },
]);

// Display all students in the house with an Eagle mascot. The order should be: House Students
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "student",
    },
  },
  { $match: { mascot: "Eagle" } },
  { $unwind: "$student" },
  {
    $group: {
      _id: { houseId: "$houseId" },
      mascot: { $first: "$mascot" },
      students: {
        $push: {
          firstName: "$student.firstName",
          lastName: "$student.lastName",
        },
      },
    },
  },
  {
    $project: {
      _id: 1,
      mascot: 1,
      students: "$students",
    },
  },
]);
