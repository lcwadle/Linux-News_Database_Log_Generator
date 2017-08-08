# News Database Log Generator 

This is the code to generate a log from the postgress database "news" including the 3 most popular articles, the number of views each author received, and finally any day with more than 1% 404 errors returned.

## Structure

The code is written in python with a single file: **LogGenerator.py**

**Generator.py** makes 4 queries to the database.
* Selects article title and number of views per article limited to the top 3 by views.
* Selects author name and numbe rof views per author.
* Selects date and number of 404 errors by date.
* Seletcs date and total views by date.

**Generator.py** uses the last two queries to calculate the error percentage by day in python and outputs any day over 1%.

## Todo
Change the output to a text file vs a console output.

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

The content of this repository is licensed under a [Creative Commons Attribution License]
