import sqlite3


class Connect():
    def __init__(self,name):
        self.connection = sqlite3.connect(name)
        self.cursor=self.connection.cursor()

    def close(self): 
        self.commit=self.connection.commit()

    def Exemany(self,cmd):
        self.cursor.executemany(cmd)
    def Exescrp(self,cmd):
        self.cursor.executescript(cmd)
    def Exe(self,cmd):
        self.cursor.execute(cmd)
    def Insert(self,value,db="",tab=""):        
        db=self.dbself(db)
        self.Select(db)
        cmd="INSERT INTO {0} {1} VALUES{2}".format(db,tab,value)
        self.Exe(cmd)
    def Close(self):
        self.close()
    def Select(self,db,tab="*",mod=""):
        self.db=db
        self.tab=tab
        self.mod=mod
        cmd="SELECT {0} FROM {1} {2}".format(tab,db,mod)
        self.Exe(cmd)
    def Fetchall(self,db="",tab="*",mod=""):
        db=self.dbself(db)
        mod=self.modself(mod)
        tab=self.tabself(tab)
        self.Select(db,tab,mod)
        self.rows=self.cursor.fetchall()
    def Printall(self,db="",tab="*",mod=""):
        db=self.dbself(db)
        mod=self.modself(mod)
        tab=self.tabself(tab)
        self.Fetchall(db,tab,mod)
        for n in self.rows:
            print(n)
    def Fetchone(self,db="",tab="*",mod=""):
        db=self.dbself(db)
        mod=self.modself(mod)
        tab=self.tabself(tab)
        self.Select(db,tab,mod)
        self.one=self.cursor.fetchone()
        return self.one
    def Update(self,update,mod,db=""):
        db=self.dbself(db)
        cmd="UPDATE {0} SET {1} WHERE {2}".format(db,update,mod)
        self.Exe(cmd)
    def CreateDb(self,values,db=""):
        db=self.dbself(db)

        cmd="CREATE TABLE IF NOT EXISTS {0} {1};".format(db,values)
        self.Exe(cmd)
    def dbself(self,db): 
        if db=="":
            db=self.db
        return db

    def tabself(self,tab): 
        if tab=="*":
            tab=self.tab
        return tab

    def modself(self,mod): 
        if mod=="":
            mod=self.mod
        return mod

