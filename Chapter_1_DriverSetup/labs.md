## Ticket: Connection

## Task

MFlix will use MongoDB as a storage layer, so for this ticket you'll be required to perform some application setup.

1. First, make sure you've created a user on your Atlas cluster with read and write access to the mflix database.

1.  The user name should be m220student and the password should be m220password
2.  Don't forget to whitelist your IP address!

2.  Copy the connection string. Select that you'd like to connect with the mongo shell, version 3.6 or later - this will give you the srv connection string. Make sure this URI string contains your username and password!

3.  Locate the file called dotini_win or dotini_unix (depending on your operating system) and replace the information within with your own srv connection string. The [TEST] URI will be used by the unit tests, while the integration tests will use the [PROD] URI:


[PROD]
SECRET_KEY = super_secret_key_you_should_change
MFLIX_DB_URI = mongodb+srv://m220student:m220password@<your-atlas-cluster-address>
MFLIX_NS = sample_mflix

[TEST]
SECRET_KEY = super_secret_testing_key
MFLIX_DB_URI = your_testing_db_uri (can be the same as Atlas, or a local MongoDB database)
MFLIX_NS = sample_mflix




It's highly suggested you also change the SECRET_KEY to some very long, very random string. While this application is only meant for local use during this course, software has a strange habit of living a long time.


Rename dotini_win or dotini_unix to .ini. You can do this by running the following command from the mflix-python directory:


mv dotini_unix .ini   # on Unix

ren dotini_win .ini  # on Windows



Note: Once you rename this file to .ini, it will no longer be visible in Finder or File Explorer. However, it will be visible from Command Prompt or Terminal, so if you need to edit it again, you can open it from there:

vi .ini       # on Unix

notepad .ini  # on Windows


## Testing and Running the Application

In order to reinforce good development practices, everything asked of you in this course is backed up by unit tests. Reading through the tests for a specific exercise will tell you exactly what is expected.

You can run the unit tests for this ticket by running:

pytest -m connection



Once the unit tests are passing, run the application with:

python run.py


Now proceed to the status page to run the full suite of integration tests and get your validation code.

### After passing the relevant tests, what is the validation code for Connection?

## Answer:

5a9026003a466d5ac6497a9d


(___)


   
# Ticket: Projection

## User Story

"As a user, I'd like to be able to search movies by country and see a list of movie titles. I should be able to specify a comma-separated list of countries to search multiple countries."

## Task

Implement the get_movies_by_country method in db.py to search movies by country and use projection to return the title field.

You can find examples in notebooks/your_first_read.ipynb.

## MFlix Functionality

Once you complete this ticket, the UI will allow movie searches by one or more countries.

Testing and Running the Application

Make sure to look at the tests in test_projection.py to understand what is expected.

You can run the unit tests for this ticket by running:

            pytest -m projection


Once the unit tests are passing, run the application with:

            python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant unit tests, what is the validation code for Projection?

## Answer:

5a94762f949291c47fa6474d


(___)


# Ticket: Text and Subfield Search

## User Story

"As a user, I'd like to be able to search movies by cast members, genre, or perform a text search of the plot summary, full plot, and title."

## Task

For this ticket, you will need to modify the method build_query_sort_project in db.py to allow the following movie search criteria:

genres: finds all movies that match the search genres Already, the build_query_sort_project method is able to return results for two different types of movie search criteria:

text: performs a text search in the movies collection
cast: finds movies that include any of the wanted cast
You just need to construct the query that queries the movies collection by the genres field.

## Hint

Check the implementation of similar formats of search criteria - the genres query should be similar. 

## MFlix Functionality

Once you complete this ticket, the UI will allow movie searches by members of the cast, movie genres, movie title, and plot summary.

A text index was created for you when you restored the collections with mongorestore, so these queries will be performant once they are implemented.

Testing and Running the Application

Make sure to look at the tests in test_text_and_subfield_search.py to understand what is expected.

You can run the unit tests for this ticket with:

                pytest -m text_and_subfield_search


Once the unit tests are passing, run the application with:

                python run.py


Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Text and Subfield Search?

## Answer:

5a96a6a29c453a40d04922cc