#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    #get MySQL username, pasword, and database name from arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, 
                         user=mysql_user, password=mysql_password, 
                         db=db_name)
    
    #create a cursor object to interact with the database
    cursor = db.cursor()

    #Execute yhe query to select states starting with 'N'
    query = "SELECT * FROM states WHERE names LIKE 'N%' ORDER BY ASC;"
    cursor.execute(query)
    
    #Fetch all results and print them
    states = cursor.fechall()
    for state in states:
        print(states)

#Close cursor and database connection
cursor.close()
db.close()
