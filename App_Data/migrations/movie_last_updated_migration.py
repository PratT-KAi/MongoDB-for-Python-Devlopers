from pymongo import MongoClient, UpdateOne
from pymongo.errors import InvalidOperation
from bson import ObjectId
import dateutil.parser as parser

"""
Ticket: Migration

Update all the documents in the `movies` collection, such that the "lastupdated"
field is stored as an ISODate() rather than a string.

The parser.parse() method can transform date strings into ISODate objects for
us. We just need to make sure the correct operations are sent to MongoDB!
"""

# ensure you update your host information below!
host = "mongodb+srv://m001-student:m001-mongo-pass@sandbox.9bf8t.mongodb.net/test"

# don't update this information
MFLIX_DB_NAME = "sample_mflix"
mflix = MongoClient(host)[MFLIX_DB_NAME]

# TODO: Create the proper predicate and projection
# add a predicate that checks that the "lastupdated" field exists, and then
# checks that its type is a string
# a projection is not required, but may help reduce the amount of data sent
# over the wire!
# here we're making sure "lastupdated" exists in the document as a string
predicate = {"lastupdated": {"$exists": True, "$type": "string"}}
# this projection only sends the "lastupdated" and "_id" fields back to the client
projection = {"lastupdated": 1}

cursor = mflix.movies.find(predicate, projection)

updates = []
for doc in cursor:
    doc_id = doc.get('_id')
    lastupdated = doc.get('lastupdated', None)
    updates.append(
        {
            "doc_id": ObjectId(doc_id),
            "lastupdated": parser.parse(lastupdated)
        }
    )

print(f"{len(updates)} documents to update")

try:
    # this will gather UpdateOne operations into a bulk_updates array
    # we target the document with "_id" and then set its "lastupdated" field
    # to the new ISODate type
    bulk_updates = [UpdateOne(
        {"_id": update.get("doc_id")},
        {"$set": {"lastupdated": update.get("lastupdated")}}
    ) for update in updates]

    bulk_results = mflix.movies.bulk_write(bulk_updates)
    print(f"{bulk_results.modified_count} documents updated")

except InvalidOperation:
    print("no updates necessary")
except Exception as e:
    print(str(e))
