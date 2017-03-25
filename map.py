from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QScreen
from PyQt5.QtCore import Qt

class Map(QWidget):

    def __init__(self ,x,y,w,a,n):
        super().__init__()
        self.i=[]
        self.j=[]
        self.n=[]
        self.x=[]
        self.y=[]
        self.c=[]
        self.color=[]
        self.initUI(x,y,w,a,n)
   
    def deletemap(self):
        del self.i[:]
        del self.j[:]
        del self.n[:]
        del self.x[:]
        del self.y[:]
        del self.c[:]
        del self.color[:]
    
    def deletedraw(self,i,j,n,x,y,cc,color):
        b=0
        print("oi2")
        for k in self.i:
            if self.i[b]==i and self.j[b]==j and  self.n[b]==n and self.x[b]==x and self.y[b]==y and self.c[b]==cc and self.color[b]==color:
                del self.i[b]
                del self.j[b]
                del self.n[b]
                del self.x[b]
                del self.y[b]
                del self.c[b]
                del self.color[b]
                print("oi")
            b=b+1
    
    def changedraw(self,i,j,n,x,y,c,color):
        
        self.i.append(i)
        self.j.append(j)
        self.n.append(n)
        self.x.append(x)
        self.y.append(y)
        self.c.append(c)
        self.color.append(color)
        
    def initUI(self,x,y,w,a,n):      

        self.setGeometry(x, y, w, a)
        self.setWindowTitle(n)

    def paintEvent(self,e):

        qp = QPainter()
        qp.begin(self)
        b=0
        print(self.i,self.j,self.n,self.x,self.y,self.c,self.color)
        for n in self.i:
            self.drawLines(qp,n,self.j[b],self.n[b],self.x[b],self.y[b],self.c[b],self.color[b])
            
            b=b+1
        qp.end()

    def drawRectangles(self, qp,x,y,l,a,color):
          
            col = QColor(0, 0, 0)
            col.setNamedColor('#d4d4d4')
            qp.setPen(col)

            qp.setBrush(QColor(color))
            qp.drawRect(x, y, l, a)
    def take_screenshot(self,filename):
        p=self.grab()
        p.save(filename+".jpg", 'jpg')

    def drawLines(self,qp,numberx,numbery,distance,lminx,lminy,ct,color):

        
        pen = QPen(Qt.black, 2, Qt.SolidLine)
            
        for n in range (int(numbery)):
            for b in range(int(numberx)):
                if ct==1:
                    self.drawRectangles(qp,distance*(lminx+n),distance*(lminy+b),distance,distance,color)
                pen.setStyle(Qt.DashLine)
                qp.setPen(pen)
                qp.drawLine(distance*(lminx+n), distance*(lminy+b), distance*(lminx+n),distance*(lminy+b+1))
                qp.drawLine(distance*(lminx+n), distance*(lminy+b),distance*(lminx+n+1),distance*(lminy+b) )
        qp.drawLine(distance*(lminx+numbery),distance*lminy,distance*(lminx+numbery),distance*(lminy+numberx))
        qp.drawLine(distance*lminx,distance*(lminy+numberx),distance*(lminx+numbery),distance*(lminy+numberx) )



