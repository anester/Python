import sqlite3 as sql

class DbMngr:
    def BuildConnectionString(server, database, userid, password):
        return 'DRIVER={{SQL Server}};SERVER={0};DATABASE={1};UID={2};PWD={3}'.format(server, database, userid, password)

    def __init__(self, server, database, userid, password):
        self.connectionstring = DbMngr.BuildConnectionString(server, database, userid, password)
        self.connection = self.GetConnection(self.connectionstring)

    def Destroy(self):
        self.connection.close()

    def GetConnection(self, constr):
        con = pyodbc.connect(constr)
        return con

    def ExecuteToCursor(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        return cur

    def ExecuteToArray(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        return list(cur)

    def ExecuteTopOne(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        return cur.fetchone()

    def ExecuteToArraySingle(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        return [x[0] for x in cur]

if __name__ == '__main__':
    mngr = DbMngr('192.168.50.27', 'Surescripts2013_DEV', 'erxuser','erxUser')

    cur = mngr.ExecuteToArraySingle("""SELECT DISTINCT MessageDetail_Patient 
	FROM MSG_MessageDetail MD
	JOIN MSG_Message MSG
		ON MSG.Message_ID = MD.Message_ID
	WHERE MessageDetail_MessageType = 'NewRx' AND Message_DateInserted > '11/01/2013'""")
    
    print(cur)

    mngr.Destroy()