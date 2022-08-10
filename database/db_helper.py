import traceback
import mysql.connector


class Database:

    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="furqan12345",
            database="mifos"
        )

        if self.connection.is_connected():
            dbInfo = self.connection.get_server_info()
            print("Connected to MySQL Server version ", dbInfo)
            with open('database\create_table.sql', 'r') as f:
                with self.connection.cursor() as cursor:
                    cursor.execute(f.read(), multi=True)
                self.connection.commit()
        else:
            print("Connection to MySQL Server failed")

    async def insert_row(self, data):
        try:
            with open('database\insert_row.sql', 'r') as f:
                with self.connection.cursor() as cursor:
                    cursor.execute(f.read(), data)
                    self.connection.commit()
        except Exception as ex:
            print('error', ex)

    async def get_row_by_id(self, _id):
        pass

    async def get_all_rows(self):
        pass
