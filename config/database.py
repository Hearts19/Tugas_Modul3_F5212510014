<<<<<<< HEAD
#Cliff Sebastian_036
import mysql.connector
from mysql.connector import Error
=======
import mysql.connector
>>>>>>> 6eabe776df8c584b4edb441c223ed6c812d6e27c

class Database:
    def __init__(self):
        self.host = "localhost"
<<<<<<< HEAD
        self.db_name = "perpustakaan"
        self.username = "root"
        self.password = ""
        self.conn = None

    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.db_name,
                user=self.username,
                password=self.password
            )

            if self.conn.is_connected():
                return self.conn

        except Error as e:
            print(f"Koneksi Gagal: {e}")
            return None


=======
        self.user = "root"
        self.password = ""
        self.database = "db_perpustakaan"  

    def get_connection(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Error Database: {err}")
            return None
>>>>>>> 6eabe776df8c584b4edb441c223ed6c812d6e27c
