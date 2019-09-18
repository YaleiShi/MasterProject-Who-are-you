import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='timit',
                                         user='root',
                                         password='111111')

    mySql_insert_query = """INSERT INTO record (path)
                           VALUES
                           ('/DR7/FGWR0/SI2208.WAV') """

    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query)
    connection.commit()
    print("Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")
