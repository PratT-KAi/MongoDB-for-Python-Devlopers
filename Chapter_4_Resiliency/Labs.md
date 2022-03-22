# Ticket: Connection Pooling

## Task

For this ticket, you'll be required to modify the configuration of MongoClient to set the maximum size of the connection pool to 50 connections.

The MongoClient in db.py is initialized in the get_db method. A link to the MongoClient documentation is included here for your reference.

You can learn more about Connection Pooling in notebooks/connection_pooling.ipynb.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m connection_pooling

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Connection Pooling?

## Answer:

5ad4f4f58d4b377bcf55d742





(___)
# Ticket: Timeouts

## Task

For this ticket, you'll be required to modify the connection information for MongoClient to set a write timeout of 2500 milliseconds.

The MongoClient in db.py is initialized in the get_db method. A link to the relevant documentation is included here for your reference.

You can learn more about timeouts in notebooks/robust_applications.ipynb.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m timeouts

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Timeouts?

## Answer:

5addf035498efdeb55e90b01




(___)
# Ticket: Handling Errors

## Task

For this ticket, you'll be required to make the API more robust by handling exceptions. Specifically, what would happen should an incorrectly formatted _id be passed to get_movie in db.py?

To determine the exact exception that will be thrown in this case, please consult the documentation to see which exceptions pymongo and bson can raise:

pymongo exceptions
bson exceptions

Once you've determined the exception you need to handle, make sure to catch it in the get_movie method.

Although this ticket will only test that you've handled exceptions for the get_movie method, it's also a good idea to look over the entirety of db.py to look for other potential exceptions and handle them!

You can find examples of Error Handling in notebooks/error_handling.ipynb.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m error_handling

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant unit tests, what is the validation code for Error Handling?

## Answer:

5ae9b76a703c7c603202ef22





(___)
# Ticket: Principle of Least Privilege

## Task

For this ticket, you'll be required to add a new user on your Atlas cluster for the MFlix application to connect with.

The user should follow credentials:

username: mflixAppUser
password: mflixAppPwd

This user should have the readWrite role on the sample_mflix database. Use Add Default Privileges to assign the user this specific role.

After you have created this user, modify the SRV connection string in your configuration file so the application connects with the new username and password.

Testing and Running the Application

There are no unit tests associated with this ticket.

Once you have modified the connection string, stop and restart the application.

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## What is the validation code for Principle of Least Privilege?

## Answer:

5b61be29094dbae03bf30616