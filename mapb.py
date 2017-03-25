from api import *
from map import *
from sql import *
from fich import *
from drawmap import *
import sys,os
x=API("375722367:AAH4HoD2MITcxT8tS_Xwr-HdhLh_3-0ONVE")
sql=Connect("char.db")
sql.CreateDb("(nomechar VARCHAR(100), nomepessoa VARCHAR(20),vida INT, loucura INT,str INT,int INT,sab INT,dex INT,perk INT, pb INT)","char")
sql.CreateDb("(nomechar VARCHAR(100), habilidade VARCHAR(20),dhabilidade VARCHAR(2000),tipo VARCHAR(20))","habilidade")
sql.CreateDb("(nomechar VARCHAR(100),item VARCHAR(20), dano VARCHAR(20),atributo VARCHAR(20),tipo VARCHAR(20),mod VARCHAR(20))","item")
sql2=Connect("mapa.db")
sql2.CreateDb("(mapa VARCHAR(100),nomeobj VARCHAR(100),i INT,j INT,x INT,y INT,cc INT,color VARCHAR(100))","obmapa")
sql2.CreateDb("(mapa VARCHAR(100),x INT,y INT,w INT,a INT,n INT)","mapa")
while True:
    try:
        global dist
        global cc
        global color
        global nmap
        global p
        x.Response("getUpdates")
        x.Chat()
        print(x.text)
        if "/smap"  in x.cmd:
            comands=x.Paramch(x.cmd[1])
            for n in comands:
                if n[0]=="map":
                    nmap=n[1]
                    sql2.Select("mapa","*","WHERE mapa IN ('{0}')".format(nmap))
                    o=sql2.Fetchone()
                    xi=o[1]
                    yi=o[2]
                    we=o[3]
                    hei=o[4]
                    dist=o[5]
                    print(o)
            try:
                del p
                p=drawmap(xi,yi,we,hei,nmap)
            except:
                
                p=drawmap(xi,yi,we,hei,nmap)
        if "/ddraw" in x.cmd:    
            comands=x.cmd[1].split()
            i=int(comands[0])
            j=int(comands[1])
            xi=int(comands[2])
            yi=int(comands[3])
            color=comands[4]
            p.cleardraw(i,j,dist,xi,yi,1,color)

        if "/draw" in x.cmd:
            try:
                comands=x.Paramch(x.cmd[1])
            except IndexError:
                comands=['map',nmap]
            for n in comands:
                if n[0]=="map":
                    nmap=n[1]


            sql2.Select("mapa","*","WHERE mapa in ('{0}')".format(nmap))
            o=sql2.Fetchone()
            xi=o[1]
            yi=o[2]
            we=o[3]
            hei=o[4]
            dist=o[5]
            print(o)
            try:
                del p
                p=drawmap(xi,yi,we,hei,nmap)
            except:
                p=drawmap(xi,yi,we,hei,nmap)
            p.clearmap()

            p.draw(int(we/dist),inhei/dist),dist,0,0)        
            sql2.Select("obmapa","*","WHERE mapa in ('{0}')".format(nmap))
            for n in sql2.Fetchall():
                p.draw(n[2],n[3],dist ,n[4],n[5],1,n[7])
            p.TSS("map")

            x.Sendfile("map",x.cid)
        if "/tts" in x.cmd:
            comands=x.cmd[1].split()
            prin=comands[0]
            p.TSS(prin)
            x.Sendfile(prin,x.cid)
        if "/cmap" in x.cmd:
            comands=x.Paramch(x.cmd[1])
            xi=0
            yi=0
            dist=50
            hei=800
            we=800
            for n in comands:
                if n[0]=="we":
                    we=n[1]
                elif n[0]=="map":
                    nmap=n[1]
                elif n[0] == "hei":
                    hei=n[1]
                elif n[0]== "dist":
                    dist=n[1]

            mapf="('{0}',{1},{2},{3},{4},{5})".format(nmap,xi,yi,we,hei,dist)
            sql2.Insert(mapf,"mapa")
            
        if "/croll" in x.cmd:

            x.cSendmsg("user: {0}".format(x.firstname))
            x.roll(x.cmd,2)
            x.cSendmsg("dados finais:{0}".format(x.dados2))

            x.cSendmsg("resultados(com mod): {0}".format(x.resultados))
            x.cSendmsg("soma total: {0}".format(x.soma))

        if "/roll" in x.cmd:
            x.Sendmsg("user: {0}".format(x.firstname))
            x.roll(x.cmd,1)
            x.Sendmsg("dados finais:{0}".format(x.dados2))
            x.Sendmsg("resultados(com mod): {0}".format(x.resultados))
            x.Sendmsg("soma total: {0}".format(x.soma))
        if "/citem" in x.cmd:
            cmdd=x.Paramch(x.cmd[1])
            for n in cmdd:
                if n[0] == "char":
                    char=n[1]
                elif n[0] == "nitem":
                    nitem=n[1]
                elif n[0] == "ditem":
                    ditem=indiwt(n[1])
                elif n[0] == "atributo":
                    atrb=n[1]
                elif n[0] == "tipo":
                    tipo=n[1]
                elif n[0] == "mod":
                    mod=n[1]
                else:
                    x.Sendmsg("parametro {0} falso".format(n))
                print(x.Sendmsg(n))
            charf="('{0}','{1}','{2}','{3}','{4}','{5}')".format(char,nitem,ditem,atrb,tipo,mod)
            sql.Insert(charf, "item")
        if "/chab" in x.cmd:
            cmdd=x.Paramch(x.cmd[1])
            for n in cmdd:
                if n[0] == "char":
                    char=n[1]
                elif n[0] == "hab":
                    hab=n[1]
                elif n[0] == "dhab":
                    dhab=n[1]
                elif n[0] == "tipo":
                    tipo=n[1]
                else:
                    x.Sendmsg("parametro {0} falso".format(n))
                print(x.Sendmsg(n))
            charf="('{0}','{1}','{2}','{3}')".format(char,hab,dhab,tipo)
            sql.Insert(charf,"habilidade")
        if "/cchar" in x.cmd:
            cmdd=x.Paramch(x.cmd[1])
            for n in cmdd:
                if n[0] == "player":
                    player=n[1]
                elif n[0] == "char":
                    char=n[1]
                elif n[0] == "vida":
                    vida=int(n[1])
                elif n[0] == "loucura":
                    loucura=int(n[1])
                elif n[0] == "str":
                    strn=int(n[1])
                elif n[0] == "int":
                    intn=int(n[1])
                elif n[0] == "sab":
                    sab=int(n[1])
                elif n[0] == "dex":
                    dex=int(n[1])
                elif n[0] == "perk":
                    perk=int(n[1])
                elif n[0] == "pb":
                    pb=int(n[1])
                else:
                    x.Sendmsg("parametro falso:")
                x.Sendmsg(n)
            charf="('{0}','{1}','{2}','{3}',{4},{5},{6},{7},{8},{9})".format(char,player,vida,loucura,strn,intn,sab,dex,perk,pb)
            sql.Insert(charf,"char")
        if "/pchar" in x.cmd:
            x.cmd=x.cmd[1].split()
            y=Ficha("char.db")
            y.Selectchar(x.cmd[0])
            y.Changestt()
            y.Loucura()
            y.createsheet()
            x.Sendfile(x.cmd[0],x.cid)

        if "/imapbj" in x.cmd:
            cmmd=x.Paramch(x.cmd[1])
            y=Ficha("mapa.db")
            att=['map','nomeobj','i','j','x','y','color']
            for n in cmmd:
                if att[0] == n[0]:
                    nmap=n[1]
                elif att[1] == n[0]:
                    nome=n[1]
                elif att[2]==n[0]:
                    i=n[1]
                elif att[3]==n[0]:
                    j=n[1]
                elif att[4]==n[0]:
                    xi=n[1]
                elif att[5]==n[0]:
                    yi=n[1]
                elif att[6]==n[0]:
                    color=n[1]
                x.Sendmsg(n)
                
            charf="('{0}','{1}',{2},{3},{4},{5},1,'{6}')".format(nmap,nome,i,j,xi,yi,color)
            sql2.Insert(charf,"obmapa")
        sql.close()
        sql2.close()

        x.Clean()
    except IndexError as e :
        pass
    except Exception as inst: 
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        x.Sendmsg(inst)           # __str__ allows args to printed directly
        x.Clean()

