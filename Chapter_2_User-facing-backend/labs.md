# Ticket: Paging

## User Story

"As a user, I'd like to get the next page of results for my query by scrolling down in the main window of the application."

## Task

Modify the method get_movies in db.py to allow for paging. You can see how the page is parsed and sent in the api_search_movies method from movies.py.

You can find examples of using cursor methods in notebooks/cursor_methods_agg_equivalents.ipynb.

## MFlix Functionality

The UI is already asking for infinite scroll! You may have noticed a message stating "paging not implemented" when scrolling to the bottom of the page.

Once this ticket is completed, this message will go away, and scrolling to the bottom of the page will result in a new page of movies.

Testing and Running the Application

Make sure you look at the tests in test_paging.py to look at what is expected.

You can run the unit tests for this ticket by running:

                    pytest -m paging


Once the unit tests are passing, run the application with:

                    python run.py


Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Paging?

## Answer:

5a9824d057adff467fb1f526

(___)


# Ticket: Faceted Search

## User Story

"As a user, I want to be able to filter cast search results by one facet, metacritic rating."

## Task

For this Ticket, you'll be required to implement one method in db.py, get_movies_faceted, so the MFlix application can perform faceted searches.

## MFlix Functionality

What is a Faceted Search?

Faceted search is a way of narrowing down search results as search parameters are added. For example, let's say MFlix allows users to filter movies by a rating from 1 to 10, but Kate Winslet has only acted in movies that have a rating of 6 or higher.

If we didn't specify any other search parameters, MFlix would allow us to choose a rating between 1 and 10. But if we first search for Kate Winslet, the application would only let us choose a rating between 6 and 10, because none of the movie documents in the result set have a rating below 6.

If you're curious, you can read more about Faceted Search here.

Faceted Search in MFlix

Faceted searches on the MFlix site cannot be supported with the basic search method get_movies, because that method uses the Mongo query language. For faceted searches, the application must use the Aggregation Framework.

The method get_movies_faceted uses the Aggregation Framework, and the individual stages in the pipeline have already been completed. Follow instructions in the db.py file to append the required stages to the pipeline object. ** Testing and Running the Application**

Look in the test_facets.py file in your tests directory to view the unit tests for this ticket.

You can run the unit tests for this ticket by running:

pytest -m facets

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Faceted Search?

## Answer:

5aa7d3948adcc3fb770f06fb



(___)


# Ticket: User Management

## User Story

"As a user, I should be able to register for an account, log in, and logout."

## Task

For this Ticket, you'll be required to implement all the methods in db.py that are called by the API endpoints in user.py. Specifically, you'll implement:

get_user
add_user
login_user
logout_user
get_user_session
delete_user
For this ticket, you will need to use the find_one(), update_one() and delete_one() methods. You can find examples in the following notebooks:

notebooks/deletes.ipynb
notebooks/your_first_write.ipynb
MFlix Functionality

Once this ticket is completed, users will be able to register for a new account, log in, logout, and delete their account.

Registering should create an account and log the user in, ensuring an entry is made in the sessions collection. There is a unique index on the user_id field in sessions, so we can efficiently query on this field.

Testing and Running the Application

Look within the test_user_management.py file in your tests directory to view the unit tests for this ticket.

You can run the unit tests for this ticket by running:

pytest -m user_management

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for User Management?

## Answer:

5a8d8ee2f9588ca2701894be


(___)


# Ticket: Durable Writes

## Task

For this ticket, you'll be required to increase the durability of the add_user method from the default Write Concern of w: 1.

When a new user registers for MFlix, their information must be added to the database before they can do anything else on the site. For this reason, we want to make sure that the data written by the add_user method will not be rolled back.

We can completely eliminate the chances of a rollback by increasing the write durability of the add_user method. To use a non-default Write Concern with a database operation, use Pymongo's with_options flag when issuing the query.

You can find examples of Write Concerns in notebooks/write_concerns.ipynb.

Testing and Running the Application

There are no unit or integration tests for this lab.

Please complete the multiple choice question below, and then implement the correct Write Concern in the add_user method.

The implementation of this task will not be tested, but using the default of w: 1 might result in a rollback of your users' account data!

## Which of the following Write Concerns is more durable than the default?

w: "majority"
w: 0
w: 1
w: 2

## Answe:

w: "majority
w: 2




(___)




# Ticket: User Preferences

## User Story

"As a user, I want to be able to store preferences such as my favorite cast member and preferred language."

## Task

For this Ticket, you'll be required to implement one method in db.py, update_prefs. This method allows updates to be made to the "preferences" field in the users collection.

## MFlix Functionality

Once this ticket is completed, users will be able to save preferences in their account information.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m user_preferences

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for User Preferences?

## Answer:

5aabe31503ac76bc4f73e267






(___)


# Ticket: Get Comments

## User Story

"As a user, I want to be able to view comments for a movie when I look at the movie detail page."

## Task

For this ticket, you'll be required to extend the get_movie method in db.py so that it also fetches the comments for a given movie. The comments should be returned in order from most recent to least recent using the date key.

Movie comments are stored in the comments collection, so this task can be accomplished by performing a $lookup. Refer to the Aggregation Quick Reference for the specific syntax.

You can find examples of Aggregation with the Python driver in notebooks/basic_aggregation.ipynb.

## MFlix Functionality

Once this ticket is completed, each movie's comments will be displayed on that movie's detail page.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m get_comments

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Get Comments?

## Answer:

5ab5094fb526e43b570e4633





(___)


# Ticket: Create/Update Comments
## User Story

"As a user, I want to be able to post comments to a movie page as well as edit my own comments."

## Task

For this ticket, you'll be required to implement two methods in db.py, add_comment and update_comment.

Ensure that update_comment only allows users to update their own comments, and no one else's comments.

## MFlix Functionality

Once this ticket is completed, users will be able to post comments on their favorite (and least favorite) movies, and edit comments they've posted.

Testing and Running the Application

You can run the unit tests for this ticket by running:

pytest -m create_update_comments

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant unit tests, what is the validation code for Create/Update Comments?

## Answer:

5aba8d5113910c25d7058f8f


(___)



# Ticket: Delete Comments

## User Story

"As a user, I want to be able to delete my own comments."

## Task

For this ticket, you'll be required to modify one method in db.py, delete_comment. Ensure the delete operation is limited so only the user can delete their own comments, but not anyone else's comments.

You can find examples of delete_one() in notebooks/deletes.ipynb.

## MFlix Functionality

Once this ticket is completed, users will be able to delete their own comments, but they won't be able to delete anyone else's comments.

Testing and Running the Application

You can run all the tests for this ticket by running:

pytest -m delete_comments

Once the unit tests are passing, run the application with:

python run.py

Now proceed to the status page to run the full suite of integration tests and get your validation code.

## After passing the relevant tests, what is the validation code for Delete Comments?

## Answer:

5ac25c280a80ed6e67e1cecb