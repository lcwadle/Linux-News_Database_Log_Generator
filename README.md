# News Database Log Generator 

This is the code to generate a log from the postgress database "news" including the 3 most popular articles, the number of views each author received, and finally any day with more than 1% 404 errors returned.

## Structure

The code is written in python with a single file: **LogGenerator.py**

**LogGenerator.py** had 6 functions and makes 3 queries to the database.
* **dbconnect** creates a database connection and curssor to the news database.  It returns the connection and cursor as a tuple, (conn, cur).
* **dbdisconnect** takes a connection tuple, (conn, cur), and safely closes both the connection and cursor.
* **exec_query** takes in a query string and uses **dbconnect** to execute the query string on the database.  When the query is complete, the results are stored in a local variable and the connection is closed using **dbdisconnect**.  Finally, the results are returned.
* **print_top_articles** queries the database for the top 5 articles by number of views and outputs to console the article names and number of views sorted highest to lowest by number of views.
* **print_top_authors** queries the database for all the authors and outputs the author name and number of views all of the author's articles have received sorted highest to lowest by number of views received.
* **print_error_logs** queries the database for the number of views per day and number of 404 Not Found errors returned.  It then outputs any day with more than a 1% error rate and the corresponding error rate for that day.

## Todo
Change the output to a text file instead of a console output.

## Usage
* Start vagrant vm using vagrant up
* SSH into vagrant vm using vagrant ssh
* Navigate to the LogGenerator folder
* Run python generator.py to output the log

## Output
~~~~
vagrant@vagrant:/vagrant/loggenerator$ python generator.py
1. What are the most popular three articles of all time?
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
2. Who are the most popular article authors of all time?
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
3. On which days did more than 1% of requests lead to errors?
Jul 17, 2016 - 2.3% errors
vagrant@vagrant:/vagrant/loggenerator$
~~~~

## License

The content of this repository is licensed under a [MIT License](https://opensource.org/licenses/MIT)
