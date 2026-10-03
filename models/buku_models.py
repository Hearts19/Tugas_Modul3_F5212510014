from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    # Disesuaikan dengan kolom Laragon: id_buku, judul_buku, stok
    def create_buku(self, id_buku, judul_buku, stok):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (id_buku, judul_buku, stok) VALUES (%s, %s, %s)"
            val = (id_buku, judul_buku, stok)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False