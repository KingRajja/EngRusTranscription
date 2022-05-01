import sqlite3

class DB:
    def __init__(self, conn,cur):
        self.conn = conn
        self.cur = cur
    def getTrans(self,eng):
        self.cur.execute(f"SELECT TRANS FROM dictonary WHERE ENG = '{eng}';")
        return self.cur.fetchall()[0][0]


#cur.execute("CREATE TABLE dictonary(id INTEGER PRIMARY KEY AUTOINCREMENT,ENG text,TRANS text)")
#conn.commit()

def addToTable(array_values):
    conn = sqlite3.connect('Dictonary.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO dictonary VALUES(NULL,?,?);", array_values)
    conn.commit()

def GetFullInfo(table_name):
    conn = sqlite3.connect('Dictonary.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    return cur.fetchall()

def GetColumnName(table_name):
    conn = sqlite3.connect('Dictonary.db')
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM pragma_table_info('{table_name}');")
    colnames = []
    for i in cur.fetchall():
        colnames.append(i[0])
    return colnames

def DeleteFromTable(colname,value):
    conn = sqlite3.connect('Dictonary.db')
    cur = conn.cursor()
    cur.execute(f"DELETE FROM translations WHERE {colname} = '{value}';")
    conn.commit()






