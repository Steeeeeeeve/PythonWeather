import sqlite3

class DBCM:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.commit()
        self.connection.close()