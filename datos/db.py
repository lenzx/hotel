import pymysql
class DB():
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='hotel2'
        )
        self.cursor = self.connect.cursor()
        print("Conectado!!!!")

