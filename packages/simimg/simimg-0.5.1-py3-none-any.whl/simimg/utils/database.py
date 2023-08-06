import os
import sqlite3
import simimg.utils.handyfunctions as HF

def CreateDBConnection(db_file):
    'Create a connection to the DataBase'

    dirName = os.path.dirname(db_file)
    if not os.path.isdir(dirName):
        try:
            os.mkdir(dirName)
        except OSError as error:
            print(error)
            return None
            
    try:
        db_connection = sqlite3.connect(db_file)
        return db_connection
    except sqlite3.Error as error:
        print(error)
        return None

def CreateDBTables(db_connection, clear=None):
    'Create or empty the required tables in the DataBase'

    sql_delete_table = ' DROP TABLE IF EXISTS HashValueTable '
    sql_create_table = ' CREATE TABLE IF NOT EXISTS HashValueTable ( id integer PRIMARY KEY, FileHash text NOT NULL, HashMethod text NOT NULL, ImageHashValue text NOT NULL) '

    try:
        db_cursor = db_connection.cursor()
        if clear:
            db_cursor.execute(sql_delete_table)
        db_cursor.execute(sql_create_table)

        db_cursor.close()
        db_connection.commit()
        return True
    except sqlite3.Error as error:
        print(error)
        return False

def CloseDBConnection(db_connection):
    try:
        db_connection.commit()
        db_connection.close()
    except sqlite3.Error as error:
        print(error)

def GetHashValueFromDataBase(md5, hashname, db_connection=None):
    # which function to use to translate the string to hash
    convDict = {
        'HSV':HF.hexstring2array,
        'HSV (5 regions)':HF.hexstring2array,
        'RGB':HF.hexstring2array,
        'RGB (5 regions)':HF.hexstring2array,
        'Luminosity':HF.hexstring2array,
        'Luminosity (5 regions)':HF.hexstring2array,
        'Horizontal':HF.hexstring2array,
        'Vertical':HF.hexstring2array,
        }
    try:
        db_cursor = db_connection.cursor()
        db_cursor.execute(
            'SELECT ImageHashValue FROM HashValueTable WHERE FileHash=? AND HashMethod=?',
            (md5, hashname)
        )
        hashvalue = db_cursor.fetchone()
        db_cursor.close()
        if hashvalue:
            return convDict[hashname](hashvalue[0])
    except sqlite3.Error as error:
        print(error)
        db_cursor.close()
    return None

def SetHashValues(Md5HashValueTuples, hashname, db_connection=None):

    if not Md5HashValueTuples:
        return

    # which function to use to translate the hash to string
    convDict = {
        'HSV':HF.array2hexstring,
        'HSV (5 regions)':HF.array2hexstring,
        'RGB':HF.array2hexstring,
        'RGB (5 regions)':HF.array2hexstring,
        'Luminosity':HF.array2hexstring,
        'Luminosity (5 regions)':HF.array2hexstring,
        'Horizontal':HF.array2hexstring,
        'Vertical':HF.array2hexstring,
        }

    tupled_data = [(md5, hashname, convDict[hashname](imagehashvalue)) for md5, imagehashvalue in Md5HashValueTuples]

    db_cursor = db_connection.cursor()
    db_cursor.executemany(
        'INSERT INTO HashValueTable (FileHash, HashMethod, ImageHashValue) VALUES(?, ?, ?)',
        tupled_data
    )
    db_cursor.close()
    db_connection.commit()
