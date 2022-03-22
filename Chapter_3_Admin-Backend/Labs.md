# Ticket: User Report

## User Story

"As an administrator, I want to be able to view the top 20 users by their number of comments."

## Task

For this ticket, you'll be required to modify one method in db.py, most_active_commenters. This method produces a report of the 20 most frequent commenters on the MFlix site.

## Hint

This report is meant to be run from the backend by a manager that is very particular about the accuracy of data. Ensure that the read concern used in this read, avoids any potential document rollback. Remember to add the necessary changes in the pipeline to meet the requirements. More information can be found in the comments of the method.

You can find examples of Aggregation with the Python driver in notebooks/basic_aggregation.ipynb.

## MFlix Functionality

Once this ticket is completed, users with database access can make users administrators. Administrators will be able to generate a user report listing top commenters.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m user_report

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for User Report?

## Answer:

5accad3272455e5db79e4dad



(___)


# Ticket: Migration
## Task

For this ticket, you'll be required to complete the command-line script located in the migrations directory of mflix called movie_last_updated_migration.py.

Things always change, and a requirement has come down that the lastupdated value in each document of the movies collection needs to be stored as an ISODate rather than a String.

Complete the script so it updates the values using the bulk API.

To perform the migration, run the script:

python movie_last_updated_migration.py

You can find examples of Bulk Operations in notebooks/bulk_writes.ipynb.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m migration

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Migration?

## Answer:

5ad9f6a64fec134d116fb06f