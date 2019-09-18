import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import os
import boto3

TIMIT = "/Users/zhangyousong/Downloads/data/lisa/data/timit/raw/TIMIT/TRAIN"

connection = mysql.connector.connect(host='localhost',
                                     database='timit',
                                     user='root',
                                     password='111111')



def getRecords():
        cursor = connection.cursor()
        query = "SELECT path, path_root from record"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

list = getRecords();
index = 0
for path in list:

    commond = "ffmpeg -i " + TIMIT + path[0] + " " + TIMIT +  path[1]  + ".mp3"
    os.system(commond)

    remotePath = path[1][1:]  + ".mp3"
    localPath = TIMIT +  path[1]  + ".mp3"
    client = boto3.client('s3', region_name='us-west-1')
    client.upload_file(localPath, 'audio2timit', remotePath,
                       ExtraArgs={'ContentType': 'audio/mp3', 'ACL': 'public-read'})

    print(localPath, remotePath )
    index = index + 1
    print(">>>>>>>>>>>>>>>", index)
