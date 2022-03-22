# Final: Question 1

Assume a collection called elections that holds data about all United States Presidential Elections since 1789. All the documents in the elections collection look like this:


{
  "year" : 1828,
  "winner" : "Andrew Jackson",
  "winner_running_mate" : "John C. Calhoun",
  "winner_party" : "Democratic",
  "winner_electoral_votes" : 178,
  "total_electoral_votes" : 261
}


total_electoral_votes represents the total number of electoral votes that year, and winner_electoral_votes represents the number of electoral votes received by the winning candidates.

Which of the following queries will retrieve all the Republican winners with at least 160 electoral votes?


db.elections.find( { "winner_party": "Republican",
                    "winner_electoral_votes": { "$lt": 160 } })


db.elections.find( { "winner_party": "Republican",
                    "total_electoral_votes": { "$lte": 160 } } )


db.elections.find( { "winner_party": "Republican",
                    "winner_electoral_votes": { "$gte": 160 } } )



db.elections.find( { "total_electoral_votes": { "$gte": 160 },
                    "winner_party": "Republican" } )
- db.elections.find( { "winner_electoral_votes": { "$gte": 160 } } )


## Answer:

db.elections.find( { "winner_party": "Republican",
                    "winner_electoral_votes": { "$gte": 160 } } )






(___)
# Final: Question 2

Consider a collection of phones called phones, used by a phone manufacturer to keep track of the phones currently in production.

Each document in phones looks like this:

{
  "model": 5,
  "date_issued" : ISODate("2016-07-27T20:27:52.834Z"),
  "software_version": 4.8,
  "needs_to_update": false
}

There is an update required for phones with software_version earlier than 4.0. Anyone still using a version older than 4.0 will be asked to update.

The phone manufacturer wants to set the flag needs_to_update to true when the value of software_version is lower than 4.0. For example, a document like this one:

{
  "model": 5,
  "date_issued" : ISODate("2014-03-04T14:23:43.123Z"),
  "software_version": 3.7,
  "needs_to_update": false
}

Should be updated to look like this:

{
  "model": 5,
  "date_issued" : ISODate("2014-03-04T14:23:43.123Z"),
  "software_version": 3.7,
  "needs_to_update": true
}


Which of the following update statements will correctly perform this update?

db.phones.update_many( { "software_version": { "$lte": 4.0 } },
                    { "$set": { "needs_to_update": True } } )


db.phones.update_one( { "software_version": { "$lt": 4.0 } },
                  { "$set": { "needs_to_update": True } } )



db.phones.update_many( { "software_version": { "$lt": 4.0 } },
                    { "$set": { "needs_to_update": True } } )



db.phones.update_many( { "software_version": { "$gt": 4.0 } },
                    { "$set": { "needs_to_update": True } } )



db.phones.update_many( { "software_version": { "$lt": 4.0 } },
                    { "$inc": { "needs_to_update": True } } )



## Answer:

db.phones.update_many( { "software_version": { "$lt": 4.0 } },
                    { "$set": { "needs_to_update": True } } )





(___)
# Final: Question 3


Suppose an instance of MongoClient is created with the following URI string:

from pymongo import MongoClient

uri = "mongodb+srv://m220-user:m220-pass@m220-test.mongodb.net/test"
mc = MongoClient(uri, authSource="admin", retryWrites=True, connectTimeoutMS=50)


The variable representing our client, mc, will:

automatically retry writes that fail.
allow a maximum of 50 connections in the connection pool.
use SSL when connecting to MongoDB.
authenticate against the test database.
wait at most 50 milliseconds for timing out a connection .

## Answer:

automatically retry writes that fail.
use SSL when connecting to MongoDB.
wait at most 50 milliseconds for timing out a connection.





(___)
# Final: Question 4

Suppose a client application is sending writes to a replica set with 3 nodes:

Source: (https://camo.githubusercontent.com/38fb35051b7f5ee4636af756aaa883526503d244833028034bb1a61d8095027d/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6564752d7374617469632e6d6f6e676f64622e636f6d2f6c6573736f6e732f4d3232302f6e6f7465626f6f6b5f6173736574732f7265706c6963615f7365745f7072696d6172795f7365636f6e646172795f686967686c6967687465645f61636b2e706e67)



Before returning an acknowledgement back to the client, the replica set waits.

When the write has been applied by the nodes marked in stripes, it returns an acknowledgement back to the client.

What Write Concern was used in this operation?

w: available

w: 0

w: 1

w: majority



## Answer:

w:majority





(___)
#Final: Question 5

Given the following bulk write statement, to a collection called employees:

requests = 
[
  
  InsertOne({ '_id': 11, 'name': 'Edgar Martinez', 'salary': "8.5M" }),    # Insert #1
  
  InsertOne({ '_id': 3, 'name': 'Alex Rodriguez', 'salary': "18.3M" }),    # Insert #2
  
  InsertOne({ '_id': 24, 'name': 'Ken Griffey Jr.', 'salary': "12.4M" }),  # Insert #3
  
  InsertOne({ '_id': 11, 'name': 'David Bell', 'salary': "2.5M" }),        # Insert #4
  
  InsertOne({ '_id': 19, 'name': 'Jay Buhner', 'salary': "5.1M" })         # Insert #5

]

response = employees.bulk_write(requests)
Assume the employees collection is empty, and that there were no network errors in the execution of the bulk write.

Which of the insert operations in requests will succeed?

Insert #1

Insert #2

Insert #3

Insert #4

Insert #5



## Answer:

Insert #1

Insert #2

Insert #3







(___)
# Final: Question 6

Suppose a client application is sending writes to a replica set with three nodes, but the primary node stops responding:

Source: https://camo.githubusercontent.com/38f9ada452ad03cfd14793f6619ade7a5136bddb43ba468c8f8e4bf1b6bf7f42/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6564752d7374617469632e6d6f6e676f64622e636f6d2f6c6573736f6e732f4d3232302f6e6f7465626f6f6b5f6173736574732f7265706c6963615f7365745f7072696d6172795f646f776e2e706e67

Assume that none of the connection settings have been changed, and that the client is only sending insert statements with write concern w: 1 to the server.

After 30 seconds, the client still cannot connect to a new primary. Which of the following exceptions will be raised by Pymongo?

DocumentTooLarge
DuplicateKeyError
ServerSelectionTimeoutError
ConfigurationError
InvalidURI


## Answer:
ServerSelectionTimeoutError





(___)
# Final: Question 7

Assume a collection called people_heights with documents that look like this:

{
  "name": "Ada",
  "height": 1.7
}

Which of the following queries will find only the 4th- and 5th-tallest people in the people_heights collection?

db.people_heights.find().sort("height", -1).skip(5).limit(3)
db.people_heights.find().sort("height", -1).limit(5).skip(3)
db.people_heights.find().sort("height", -1).skip(3).limit(2)
db.people_heights.find().sort("height", -1).skip(3).limit(5)


## Answer:

db.people_heights.find().sort("height", -1).skip(3).limit(2)





(___)