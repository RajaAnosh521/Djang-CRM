import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
)

# prepare a cursor object! 
cursorObject = database.cursor() 

# Create a database!
cursorObject.execute("CREATE DATABASE mydatabase")

print("All Done!") 