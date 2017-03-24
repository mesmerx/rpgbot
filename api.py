import urllib.request
import json
import time
import re
import random
import sys
import requests
import sys
dados2=[]
resultados=[]
soma=0

    
class API():
    def __init__(self,token):
        self.token="375722367:AAH4HoD2MITcxT8tS_Xwr-HdhLh_3-0ONVE"
   
    def Response(self,cmd,param=""):
        response = urllib.request.Request('https://api.telegram.org/bot{0}/{1}?{2}'.format(self.token, cmd,param))
        self.response=urllib.request.urlopen(response).read().decode('utf-8')
        self.Json()
        return self.response
    def Sendfile(self,prin,chat):
        url = "https://api.telegram.org/bot{0}/sendPhoto".format(self.token)
        files = {'photo': open(prin+'.jpg', 'rb')}
        data = {'chat_id' : chat}
        r= requests.post(url, files=files, data=data)

        
        req = urllib.request.Request('http://www.example.com', data)
    def Json(self):
        self.json = json.loads(self.response,encoding='utf-8')
        return self.json

    def group(self):
        self.group=self.json['result'][-1]['message']
    def Chat(self):
        self.chat=self.json['result'][-1]['message']['chat']
        self.frm=self.json['result'][-1]['message']['from']
        try:
            self.user=self.frm['username']
        except:
            pass
        self.id=self.frm['id']
        self.cid=self.chat['id']
        self.firstname=self.frm['first_name']
        self.lastoff=self.json['result'][-1]['update_id']
        self.type=self.chat['type']
        try: 
            self.text=self.json['result'][-1]['message']['text']
            self.cmd=self.text.split(" ",1)
        except:
            pass
        
        

    def cSendmsg(self,cmd):    
        f=self.Param({'chat_id':self.cid,'text':cmd })
        msg=self.Response('sendMessage',f)
        print("texto: {}".format(cmd))

   
    def Clean(self):
        self.Response("getUpdates",self.Param({"offset":self.lastoff+1}))

    def Sendmsg(self,cmd):    
        print(cmd)
        f=self.Param({'chat_id':self.id,'text':cmd })
        msg=self.Response('sendMessage',f)
        print("texto: {}".format(cmd))


    def roll(self,cmd,p):
        global soma
        global resultados
        global dados2
        if len(cmd)==1:
            dados=["1d20"]
        else: 
            dados=cmd[1].split()
        i=0
        soma=0
        dados2=[]
        resultados=[]
        for n in dados:
            i=i+1
            dice = re.match('(\d+)?d(\d+)([-+\/*]\d+)?([-+\/*]\d+)?([-+\/*]\d+)?([-+\/*]\d+)?([-+\/*]\d+)?([-+\/*]\d+)?', n)
            if dice.group(1) is None:
                times=1
            else:
                times=dice.group(1)
            ndice=dice.group(2)
            for b in range(int(times)):
                mod=""
                value=random.randint(1,int(dice.group(2)))
                for d in dice.groups()[2:]:
                    if d is not None:
                        mod=mod+d
                final=eval("{0}{1}".format(value,mod))
                if p==1:
                    self.Sendmsg("{0} dice (d{1}) roll {2} ->  {3}{4} sum: {5}".format(i,ndice,b+1,value,mod,final))
                else:
                    self.cSendmsg("{0} dice (d{1}) roll {2} ->  {3}{4} sum: {5}".format(i,ndice,b+1,value,mod,final))


                soma=soma+int(final) 
                dados2.append(value)
                resultados.append(int(final))
            self.dados2=dados2
            self.soma=soma
            self.resultados=resultados


 
    def Param(self,params):
        self.param = urllib.parse.urlencode(params)
        return self.param

    def Paramch(self,param):
        self.pa=re.findall('(\w+)=(.*?);',param)
        print(self.pa)
        return self.pa
