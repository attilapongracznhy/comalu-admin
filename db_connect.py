import mysql.connector

mydb = mysql.connector.connect(
  host="dbserver12.hydro.com",
  user="dbservice_comalu",
  password="Super$3cr3tP4ssw0rd!"
)

print(mydb)
