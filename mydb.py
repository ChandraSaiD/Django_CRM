import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Chandra@1702',
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a Database
cursorObject.execute("CREATE DATABASE elderco")

print("all done")
