# Quiz

## Connection Pooling

Which of the following are benefits of connection pooling?

The connection pool will persist after the client is terminated.
New operations can be serviced with pre-existing connections, so a new connection doesn't have to be created each time.
A large influx of operations can be handled more quickly with a pool of existing connections.
Multiple database clients can share a connection pool.

## Answer
New operations can be serviced with pre-existing connections, so a new connection doesn't have to be created each time.
A large influx of operations can be handled more quickly with a pool of existing connections.


## Robust Client Configuration

When should you set a wtimeout?

When our application is using a connection pool of 100 or more connections.
When our application is using a Write Concern more durable than w: 1.
When our application is issuing bulk operations in large batches.
When our application is using a Read Concern more durable than "available".

## Answer:
When our application is using a Write Concern more durable than w: 1.


## Change Streams

What of the following is true about Change Streams in Pymongo?

They output cursors, which contain change event documents.
They can stay open for up to 10 minutes.
They can be used to log changes to a MongoDB collection.
They will not log changes associated with insert operations.
They accept pipelines, which can be used to filter output from the change stream.

## Answer:
They output cursors, which contain change event documents.
They can be used to log changes to a MongoDB collection.
They accept pipelines, which can be used to filter output from the change stream.