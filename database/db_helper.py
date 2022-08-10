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
            with open('database\create_table.sql', 'r') as file:
                with self.connection.cursor() as cursor:
                    cursor.execute(file.read(), multi=True)
                self.connection.commit()
        else:
            print("Connection to MySQL Server failed")

    async def insert_row(self, data):
        try:
            with open('database\insert_row.sql', 'r') as file:
                with self.connection.cursor() as cursor:
                    cursor.execute(file.read(), data)
                    self.connection.commit()
        except Exception as ex:
            print('Database error', ex)

    async def get_row_by_id(self, _id):
        try:
            with open('database\get_by_id.sql', 'r') as file:
                with self.connection.cursor() as cursor:
                    cursor.execute(file.read(), (_id,))
                    customers = cursor.fetchone()
                    return customers
        except Exception as ex:
            print('Database error', ex)

    async def get_all_rows(self):
        try:
            with open('database\get_all.sql', 'r') as file:
                with self.connection.cursor() as cursor:
                    cursor.execute(file.read())
                    customers = cursor.fetchall()
                    return customers
        except Exception as ex:
            print('Database error', ex)
