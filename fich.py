import re
from sql import *
from subprocess import call
from api import *
class Ficha():
    def __init__(self,db):
        self.db=db
    def Selectchar(self,nome):
        self.nome=nome
        self.x=Connect(self.db)
        self.x.Select("char","*","WHERE nomechar IN ('{0}')".format(nome))
    def Changestt(self,nome=""):
        nome=self.vself(nome)
        self.Selectchar(nome)
        row=self.x.Fetchone()
        print(nome,row)
        with open('sheet.tex', 'r') as file :
            filedata = file.read()
        att=['nomechar', 'nomepessoa','vida' , 'loucura' ,'str' ,'int' ,'sab' ,'dex' ,'perk','pb']
        a=0
        for n in att:

            if n != "vida" and n != "loucura" and n != "nomechar" and n !="nomepessoa": 
                mod=(int(row[a])-10)/2
                filedata=re.sub('mod{0}{{.*?}}'.format(n),'mod{0}{{{1}}}'.format(n,int(mod)),filedata)
            if n == "str":
                moddef=(int(row[a]-10)/2+10)
            if n == "dex":
                modesq=(int(row[a]-10)/2+10)
            filedata=re.sub('\\\{0}{{.*?}}'.format(n),'\\\{0}{{{1}}}'.format(n,row[a]),filedata)
            a=a+1
        print(moddef,modesq)
        filedata=re.sub('defe{.*?}','defe{{{0}}}'.format(int(moddef)),filedata)
        filedata=re.sub('esq{.*?}','esq{{{0}}}'.format(int(modesq)),filedata)
        with open('sheet.tex', 'w') as file:
            file.write(filedata)
    def Loucura(self,nome=""):
        nome=self.vself(nome)
        self.Selectchar(nome)
        row=self.x.Fetchone()
        with open('sheet.tex', 'r') as file :
            filedata = file.read()
        for n in range(row[3]):
            filedata=re.sub(r'(\\spot ) ','\cspot ',filedata,1)    
        with open('sheet.tex', 'w') as file:
            file.write(filedata)
    def vself(self,nome): 
        if nome=="":
            nome=self.nome
        return nome
    def createsheet(self,nome=""):
        nome=self.vself(nome)
        call(["pdflatex", "sheet.tex"])
        call(["convert", "-density","300","-trim","sheet.pdf","-quality","100",nome+".jpg"])

