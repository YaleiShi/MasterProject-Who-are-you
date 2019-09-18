import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

TIMIT = "/Users/zhangyousong/Downloads/data/lisa/data/timit/raw/TIMIT/TRAIN"

connection = mysql.connector.connect(host='localhost',
                                     database='timit',
                                     user='root',
                                     password='111111')





def getSentenceBody(path):

    with open(TIMIT+path) as fp:
        mylist = fp.read().splitlines()
        line = mylist[0]
        index = line.index(" ", 3)
        line2 = line[index+1:]
        return line2



def getSentenceID(s, path):

    cursor = connection.cursor()
    query = "SELECT id from sentence where name = %s "
    rows_count = cursor.execute(query, (s, ))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        body = getSentenceBody(path + ".TXT")
        try:
            cursor2 = connection.cursor()
            query = "INSERT INTO sentence (name, body) VALUES (%s, %s)"
            print(s, body)
            result = cursor2.execute(query, (s, body,))
            connection.commit()
            return cursor2.lastrowid
        except TypeError as e:
            print(e)

def getSpeakerID(s, gender, rid):

    cursor = connection.cursor()
    query = "SELECT id from speaker where name = %s "
    rows_count = cursor.execute(query, (s, ))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:

        cursor2 = connection.cursor()
        query = "INSERT INTO speaker (name, gender, rid) VALUES (%s, %s, %s)"
        result = cursor2.execute(query, (s, gender, rid))
        connection.commit()
        return cursor2.lastrowid



def insertRecord(sid,spid, path, path_root,region):
        cursor = connection.cursor()
        query = "SELECT id from record where sid = %s and spid=%s"
        cursor.execute(query, (sid,  spid))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result[0]
        else:

            cursor2 = connection.cursor()
            query = "INSERT INTO record (sid,spid, path, path_root, region ) VALUES (%s, %s, %s, %s, %s)"
            result = cursor2.execute(query, (sid, spid, path, path_root,region))
            connection.commit()
            return cursor2.lastrowid



def processLine(s):
        a = s.split("/")
        region = a[1]
        gender = a[2][0]
        speaker = a[2][1:]
        aa = a[3].split(".")
        sentence = aa[0]
        path = "/" + a[1]+"/"+a[2] +"/"+sentence

        sid = getSentenceID(sentence, path)
        spid = getSpeakerID(speaker, gender, region[2:])
        insertRecord(sid, spid, s, path, region[2:])

        print(region, "-", gender, "-", speaker, "-", path, spid, region[2:])


with open('data.txt') as fp:
	mylist = fp.read().splitlines()


for line in mylist:
    line.strip('.')
    processLine(line[1:])
#processLine("/DR4/MMDM0/SI681.WAV")
#print(mylist[0])
