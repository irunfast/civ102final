#imports
import math

#initialize constants
u1=0.2 #poisson
ee=4000 #youngs
#these are the things that you can change
ll=1300 #length of bridge
aa=813*1016 #area of matboard dedicated to this portion of bridge
Mp=165 #positive moment max coefficient: M=Mp*P
Mm=190 #negative moment max coefficient: M=Mm*P
tt=100 #minimum top beam width
ss=50 # minimum side beam width
bb=10 # minimum bottom beam width
dd=10 # minimum distance between beams

#i calculator INCOMPLETE
def icalc(

#q calculator INCOMPLETE
def qcalc(

#centroid calculator (1 refers to bottom,2 refers to side,3 refers to top)
#a refers to number of layers, b refers to length
#returns length from bottom  in mm
def cnt(a1,b1,a2,b2,a3,b3):
    return (a3*b3+2*a2*b2-a1*b1)/(4*a2)+1.27*a1

#area calculator --> returns decimal fraction of total matboard used
#input references same as in cnt, lt is length of span, at is total area
#dt is # of diaphragms, st is distance between 2 horizontal portions
def arc(a1,b1,a2,b2,a3,b3,at,lt,dt,st):
    return ((a1*b1+2*a2*(b2+10)+a3*b3)*lt+dt*(st+10))/at

#sigmacr --> use for d to end
def scr(k,e,n,t,b,a):
    if a==0:
        return((k*(math.pi**2)*e)/(12*(1-n**2)))*((t/b)**2)
    else:
        return((k*(math.pi**2)*e)/(12*(1-n**2)))*((t/b)**2-(t/a)**2)

#find P for step a to e
def pcr1(m,y,i,s):
    return (s*i)/(y*m)

#find P for step f 
def pcr2(t,i,b,q):
    return(t*i*b/q)    

#bridge calculator equation 3 sides --> output smallest p and where INCOMPLETE
def sml1(a1,b1,a2,b2,n,d):


#bridge calculator equation 4 sides -->output smallest p and where INCOMPLETE
def sml2(a1,b1,a2,b2,a3,b3,at,lt,dt,st):
    x=[] #pressure values
    y=[] #titles of pressures
    c=cnt(a1,b1,a2,b2,a3,b3)#y --> centroid
    i=icalc(? # i , INCOMPLETE
    
    x.append(pcr1(??,c,i,30)) #unknown m values
    y.append("a)Pointload M+ Tension")

    x.append(pcrl(??,c,i,6))
    y.append("a)Pointload M+ Tension")

    x.append(pcr1(??,c,i,30))
    y.append("a)Pointload M- Tension")

    x.append(pcrl(??,c,i,6))
    y.append("a)Pointload M- Compression")

    x.append(pcr2(4,i,a1*1.27,qcalc(#incomplete))
    y.append("b) Pointlaod shear")

    x.append(pcr2(2,i,a1*1.27,qcalc(#incomplete))
    y.append("c) Glue shear")

    x.append(
    
    return[y[x.index(min(x))],min(x)]

#actual runthrough
#loop 1: 4 sides
win=0
winlist=[]
x1=tt #top width
x2=1 #number of layers for top
x3=ss #side length
x4=1 # of side layers
x5=bb #bottom width
x6=1 # of bottom layers
x7=dd # distance between beams
x8=0 # number of diaphragms
while True:
    if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
    x2=1 #number of layers for top
    x3=ss #side length
    x4=1 # of side layers
    x5=bb #bottom width
    x6=1 # of bottom layers
    x7=dd # distance between beams
    x8=0 # number of diaphragms
    while True:
        if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
        x3=ss #side length
        x4=1 # of side layers
        x5=bb #bottom width
        x6=1 # of bottom layers
        x7=dd # distance between beams
        x8=0 # number of diaphragms
        while True:
            if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
            x4=1 # of side layers
            x5=bb #bottom width
            x6=1 # of bottom layers
            x7=dd # distance between beams
            x8=0 # number of diaphragms
            while True:
                if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
                x5=bb #bottom width
                x6=1 # of bottom layers
                x7=dd # distance between beams
                x8=0 # number of diaphragms
                while True:
                    if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
                    x6=1 # of bottom layers
                    x7=dd # distance between beams
                    x8=0 # number of diaphragms
                    while True:
                        if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
                        x7=dd # distance between beams
                        x8=0 # number of diaphragms
                        while True:
                            if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
                            x8=0
                            while True:
                                if arc(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)>=1:break
                                [z1,z2]=sml2(x2,x1,x4,x3,x6,x5,aa,ll,x8,x7)
                                if z1>win:
                                    z1=win
                                    winlist=[x1,x2,x3,x4,x5,x6,x7,x8]
                                x8+=1
                            x7+=0.5
                        x6+=1
                    x5+=0.5
                x4+=1
            x3+=0.5
        x2+=1
    x1+=0.5

print(winlist)
#loop 2: 3 sides

