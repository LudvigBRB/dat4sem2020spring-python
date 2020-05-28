import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import time

def make_SQL_cursor(database):
    cnx = mysql.connector.connect(user='dev', password='ax2',
                                  host='127.0.0.1',
                                  port='3307',
                                  database=database,
                                  use_pure=True)
    cursor = cnx.cursor()
    return cursor, cnx


def take3Variables(a, b, c):
    return a, b, c

def make_graph(database, table):
    data_list1, data_list2, data_list3 = retrieve_return(database, table)
    id_list = retrieve_return_id(database, table)
    
    plt.scatter([id_list], [data_list1])
    plt.scatter([id_list], [data_list2])
    plt.scatter([id_list], [data_list3])
    plt.show()

def retrieve_return(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    #query = ("SELECT a FROM " + database + "." + table)
    query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    #aList = [value for value in cursor]
    fList = [value for value in cursor]

    aList = []
    bList = []
    cList = []

    for i in range(0, len(fList)):
        aList.append(fList[i][0])
        bList.append(fList[i][1])
        cList.append(fList[i][2])

    cursor.close()
    cnx.close()

    return aList, bList, cList

def retrieve_return_id(database, table):  # this works
    cursor, cnx = make_SQL_cursor(database)

    query = ("SELECT id FROM " + database + "." + table)
    #query = ("SELECT a, b, c FROM analysis.info")

    cursor.execute(query)

    aList = [value for value in cursor]
    bList = []
    
    for i in range(0, len(aList)):
        bList.append(aList[i][0])

    cursor.close()
    cnx.close()

    return bList

def insert_into_database(database, table, a, b, c):
    #a, b, c = take3Variables(a, b, c)

    cursor, cnx = make_SQL_cursor(database)
    
    localtime = time.asctime( time.localtime(time.time()) )

    query = ("INSERT INTO " + table + " VALUES (null, %s, %s, %s, %s)")

    cursor.execute(query, (a, b, c, localtime))
    
    cnx.commit()

    cursor.close()
    cnx.close()

    return 'færdig'
