import MySQLdb
class BaseDao():
    def __init__(self, connection):
        self.conn = connection

    def open(self):
        self.cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def close(self):
        self.cursor.close()

