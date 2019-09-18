import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

TIMIT = "/Users/zhangyousong/Downloads/data/lisa/data/timit/raw/TIMIT/TRAIN"

connection = mysql.connector.connect(host='localhost',
                                     database='timit',
                                     user='root',
                                     password='111111')





def getRecord(region):
        cursor = connection.cursor()
        query = "SELECT * from record where region = %s"
        cursor.execute(query, (region, ))
        result = cursor.fetchall()
        return result
