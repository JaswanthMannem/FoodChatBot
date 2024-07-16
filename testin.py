'''import mysql.connector
from mysql.connector import Error

def check_mysql_connection():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pandeyji_eatery"
        )
        if cnx.is_connected():
            cursor = cnx.cursor()
            query = f"SELECT status FROM order_tracking WHERE order_id={41}"
            cursor.execute(query)
            result = cursor.fetchone()
            print(result[0])
            cursor.close()
            print("Connection to MySQL database is successful")
            return cnx
    except Error as e:
        print(f"Error: {e}")
        return None

# Usage
cnx = check_mysql_connection()
if cnx:
    # Perform database operations
    print(cnx)
    cnx.close()
else:
    print("Failed to connect to the database.")'''
import db_helper
print(db_helper.get_order_status(41))