import mysql.connector

class SqlConnector:
    def __init__(self) -> None:
        self.conn = None
        self.cur = None
    
    def connect(self):
        self.conn = mysql.connector.connect(
                        host="ksa-hack-aprabhu.mysql.database.azure.com",
                        user="aprabhu",
                        password="Builder!12",
                        database="antipirate"
                        )
        self.cur = self.conn.cursor()

    def retrieve(self, query):
        self.connect()
        self.cur.execute(query)
        res = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return res

    def insert(self, query):
        try:
            self.connect()
            self.cur.execute(query)
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except mysql.connector.errors.IntegrityError:
            print("this app has already been added to the database")
            pass




