#!/usr/bin/env python
import psycopg2

# Creates a connection and a cursor to the 'news' database
# Returns connection and cursor in a tuple, (conn, cur)
def dbconnect():
    conn = psycopg2.connect(database="news")
    cur = conn.cursor()
    return (conn, cur)

# Closes the connection and cursor to the database
def dbdisconnect(conn_info):
    conn_info[0].close()
    conn_info[1].close()

# Executes specified query on the database while safely connection and
# disconnecting from the database
# Returns the query results
def exec_query(query):
    db_info = dbconnect()
    db_info[1].execute(query)
    records = db_info[1].fetchall()
    dbdisconnect(db_info)
    return records

# Prints the top 3 articles in the database
def print_top_articles():
    print ("1. What are the most popular three articles of all time?")
    records =  exec_query("""select articles.title, count(log.id) from articles,
                          log where log.path = '/article/' || articles.slug
                          group by articles.title order by count(log.id) desc
                          limit 3;""")
    for record in records:
        print (record[0] + " - " + str(record[1]) + " views")

# Prints the top rated authors by views from highest to lowest
def print_top_authors():
    print ("2. Who are the most popular article authors of all time?")

    records = exec_query("""select authors.name, count(log.id) from authors,
                         log, articles where log.path = '/article/' ||
                         articles.slug and articles.author = authors.id group
                         by authors.name order by count(log.id) desc;""")

    for record in records:
        print (record[0] + " - " + str(record[1]) + " views")

# Prints days where the error rate for connecting to articles was higher than
# 1%
def print_error_logs():
    print("3. On which days did more than 1% of requests lead to errors?")

    records = exec_query("""select date1, (cast(errors as float)/cast(total as
                     float)) as errorrate from (select date(time) as date1,
                     count(id) as total from log group by date1) as logtotal,
                     (select date(time) as date2, count(id) as errors from log
                     where status = '404 NOT FOUND' group by date2) as
                     logerror where date1 = date2 and
                     (cast(errors as float)/cast(total as float))  > .01 order
                     by date1;""")

    for record in records:
        print("{:%b %d, %Y}".format(record[0]) + " - " +
              "{:.1%}".format(float(record[1])) +
              " errors")


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_error_logs()
