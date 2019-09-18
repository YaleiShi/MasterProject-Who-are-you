import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

TIMIT = "/Users/zhangyousong/Downloads/data/lisa/data/timit/raw/TIMIT/TRAIN"

connection = mysql.connector.connect(host='localhost',
                                     database='timit',
                                     user='root',
                                     password='111111')





def getRecords(region):
        cursor = connection.cursor()
        query = "SELECT record.id, sentence.body, record.path_root from record ,sentence  where sentence.id = record.sid and region = %s "
        cursor.execute(query, (region, ))
        result = cursor.fetchall()
        return result

def getRecordInfo(id):
        cursor = connection.cursor()
        query = "SELECT * from record  where id = %s "
        cursor.execute(query, (id, ))
        result = cursor.fetchone()
        return result

def getRecordPath(id):
        cursor = connection.cursor()
        query = "SELECT path from record where id = %s "
        cursor.execute(query, (id, ))
        result = cursor.fetchone()
        return TIMIT + result[0]

def getRecordPathRoot(id):
        cursor = connection.cursor()
        query = "SELECT path_root from record where id = %s "
        cursor.execute(query, (id, ))
        result = cursor.fetchone()
        return TIMIT + result[0]
