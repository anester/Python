import sqlite3 as sql
from DDQueries import *

class MyDb:
    def __init__(self, dbfilename):
        self.filename = dbfilename
        self.conn = sql.connect(dbfilename)

    def __lastinsertrowid__(self):
        sql = 'select last_insert_rowid();'    
        res = self.query(sql)
        row = res.fetchone()
        return row[0]

    def query(self, sql, params = None):
        cur = self.conn.cursor()
        if params != None:
            res = cur.execute(sql, params)
        else:
            res = cur.execute(sql)
        return res

    def maptoobject(self, objtype, sql, params=None):
        res = self.query(sql, params)
        arr = []
        for row in res.fetchall():
            i = 0
            obj = objtype()
            for colname in (c[0] for c in res.description):
                setattr(obj, colname, row[i])
                i += 1
            arr.append(obj)
        return arr

class DDDb(MyDb):
    '''All data access to the sqlite3 database happens here.'''
    
    def __init__(self, dbname, reinitdb=False):
        MyDb.__init__(self, dbname)
        self.__reinitdb__(reinitdb)
 
    def __reinitdb__(self, reinit):
        droptables = DDQUERIES['createdb']['drop_tables']
        createtables = DDQUERIES['createdb']['create_tables']

        if reinit:
            for q in droptables:
                self.query(q)

        for q in createtables:
            self.query(q)

    def insert_stats(self, values):
        sql = DDQUERIES['modifydb']['insert']['Stats']
        res = None
        
        if type(values) == list or type(values) == tuple:
            self.query(sql, values)
        elif type(values) == dict:
            v = values
            self.query(sql, (values['Stats_Value'],
                             values['Stats_Level'],
                             values['Stats_Max_Level'],
                             values['Stats_Hero_Health'],
                             values['Stats_Hero_Damage'],
                             values['Stats_Hero_Speed'],
                             values['Stats_Hero_Casting_Rate'],
                             values['Stats_Hero_Special1'],
                             values['Stats_Hero_Special2'],
                             values['Stats_Defense_Health'],
                             values['Stats_Defense_Damage'],
                             values['Stats_Defense_Area_Effect'],
                             values['Stats_Defense_Attack_Rate'],
                             values['Stats_Armor_Resist_Base'],
                             values['Stats_Armor_Resist_Fire'],
                             values['Stats_Armor_Resist_Electric'],
                             values['Stats_Armor_Resist_Poison']))
        ret = self.__lastinsertrowid__()
        return ret

    def insert_armor(self, values):
        sql = DDQUERIES['modifydb']['insert']['Armor']

        if type(values) == list or type(values) == tuple:
            statsvals = values[:17]
            armorvals = values[17:]
            statid = self.insert_stats(statsvals)
            armorvals.insert(0, statid)

            self.query(sql, armorvals)
            ret = self.__lastinsertrowid__()
        elif type(values) == dict:
            statid = self.insert_stats(values)
            values['Stats_ID'] = statid
            self.query(sql, (values['Stats_ID'],
                             values['Armor_Name'],
                             values['Armor_Quality'],
                             values['Armor_Type'],
                             values['Armor_Kind']))
            
            ret = self.__lastinsertrowid__()

        return ret
        
if __name__ == '__main__':
    db = DDDb('temp.db', False)
    print(db.insert_stats((100,1,100,1,1,1,1,1,1,1,1,1,1,1,1,1,1)))
    
