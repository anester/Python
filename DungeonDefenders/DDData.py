import sqlite3 as sql
from DDQueries import *

class DDDb:
    '''All data access to the sqlite3 database happens here.'''
    
    def __init__(self, connection, reinitdb=False):
        if(reinitdb):
            self.__reinitdb__()
        self.conn = connection

    def __lastinsertrowid__(self):
        sql = 'select last_insert_rowid();'    
        res = self.executequery(sql)
        row = res.fetchone()
        
        return row[0]

    def __reinitdb__(self):
        droptables = DDQUERIES['createdb']['drop_tables']
        createtables = DDQUERIES['createdb']['create_tables']

        for q in droptables:
            self.nonquery(q)

        for q in createtables:
            self.nonquery(q)

    def executequery(self, sql, params = None):
        cur = self.conn.cursor()
        res = cur
        res = None

        if params != None:
            res = cur.execute(sql, params)
        else:
            res = cur.execute(sql)

        return res

    def nonquery(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)

        return res

