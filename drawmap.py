import sys
from map import *
class drawmap():
    def __init__(self,x,y,w,a,nome=""):
        self.app = QApplication(sys.argv)
        self.ex=Map(x,y,w,a,nome)
    def draw(self,i,j,n,x,y,cc=0,color=""):
        self.ex.changedraw(i,j,n,x,y,cc,color)
        
    def TSS(self,filename):
        self.ex.take_screenshot(filename)
    def cleardraw(self,i,j,n,x,y,cc=1,color=""):
        self.ex.deletedraw(i,j,n,x,y,cc,color)
    def clearmap(self):
        self.ex.deletemap()
