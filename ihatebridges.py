#imports
import math

#initialize constants
u1=0.2
e1=4000

#i calculator

#

#sigmacr
def scr(k,e,n,t,b,a):
    if a==0:
        return((k*(math.pi**2)*e)/(12*(1-n**2)))*((t/b)**2)
    else:
        return((k*(math.pi**2)*e)/(12*(1-n**2)))*((t/b)**2-(t/a)**2)

#find Q
def pcr(t,i,b,q):
    return(t*i*b/q)    

#bridge calculator equation
def sml(t1,b1,t2,b2):
    x=[0]*11
    y=["a)M+Tens","a)M+Comp","a)M-Tens","a)M-Comp","b)Matboardshear","c)Glueshear","d)M+Flangeinner","d)M+Flangeouter","e)M+web","e)M-web","f)shearweb"]
    x[1]=
    x[2]=
    x[3]=
    x[4]=
    x[5]=
    x[6]=
    x[7]=
    x[8]=
    x[9]=
    x[10]=
    x[11]=
    
    return[y[x.indexof(min(x))],min(x)]

#actual runthrough
