import cv2
import numpy as np
import mysql 

db = mysql.connector(host="localhost",    # your host, 
                     user="root",         # your username
                     passwd="Milito30",  # your password
                     db="monedas")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

# Execute SQL select statement
#cursor.execute("SELECT * FROM Monedas.monedasdiezcentimos")

#print(cursor.fetchall())

# Close the connection
#db.close()

query = ("SELECT MAX(id) as idx FROM Monedas.monedasdiezcentimos")

cursor.execute(query)

profile=None
for row in cursor:
	profile=row
cursor.close

##falta analisar
sampleNumber=0;
while (True):
	ret, img=cam.read();
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);
	for (x,y,w,h) in faces:
		sampleNumber=sampleNumber+1;
		cv2.imwrite("dataSet/User."+str(profile[0])+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
		cv2.rectangle(img, (x,y),(x+y,y+h),(0,0,255),2)
		cv2.waitKey(100);
	cv2.imshow("Face",img);
	cv2.waitKey(1);
	if (sampleNumber>100):
		break;

cam.release()
cv2.destroyAllWindows()	