import MySQLdb
class BaseDao():
    def __init__(self, connection):
        self.conn = connection

    def open(self):
        return self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def close(self, cursor):
        cursor.close()

    def commit(self):
        self.conn.commit()
