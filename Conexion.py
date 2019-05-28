import mysql

db = mysql.connector(host="localhost",    # your host, 
                     user="root",         # your username
                     passwd="Milito30",  # your password
                     db="monedas")        # name of the data base

# you must create a Cursor object. It will let
cursor = db.cursor()

query = ("SELECT MAX(id) as idx FROM Monedas.monedasdiezcentimos")

cursor.execute(query)

profile=None
for row in cursor:
	profile=row
cursor.close

print(profile[0])