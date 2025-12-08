import mysql.connector as mysql_conn

class Database:
	def __init__(self) :
		self.mydb = mysql_conn.connect(
	 		host="localhost",
	 		user="root",
	 		password="",
	 		database="data_mahasiswa"
		)

		self.cursor = self.mydb.cursor()

db_conn = Database()2
