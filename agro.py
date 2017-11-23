import sqlite3 as lite
import sys

agro = (
	('Temperature sensor1', 27.2, "Cel"),
	('Temperature sensor2', 30.0, "Cel"),
	('Temperature sensor3', 32.3, "Cel"),
	(   'Humidity sensor1', 80.0, "g/kg"),
	(   'Humidity sensor2', 82.0, "g/kg"),
	(   'Humidity sensor3', 77.0, "g/kg")
	
)
	
con = lite.connect('agro.db')

with con:

		cur = con.cursor()
		
		cur.execute("DROP TABLE IF EXISTS agro")
		cur.execute("CREATE TABLE agro( Name TEXT,Value FLOAT, Unit TEXT)")
		cur.executemany("INSERT INTO agro VALUES(?, ?, ?)",agro)
		