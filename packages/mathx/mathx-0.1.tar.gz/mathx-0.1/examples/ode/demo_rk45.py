import numpy as np
import pyqtgraph_extended as pg
from ode.model_systems import constant_force,sinusoidal_force,wave
from ode.rk45 import *

y_0,soln,f,P=constant_force(2)
y_0=np.array(y_0)

h=2
N=100
n=np.arange(N)[:,None]
t=n*h
y=np.zeros((N,len(y_0)),y_0.dtype)
y[0,:]=y_0
fe=None
ok=np.zeros(N)
hn=np.zeros(N)
rtol=1e-3
interps=[]
for n in range(1,N):
    if P is None:
        y[n,:],ok[n],hn[n],fe,interp,_,_=step((n-1)*h,h,y[n-1,:],f,fe,rtol)
        #fe=fes[-1]
    else:
        y[n,:],ok[n],hn[n],fe,interp,_,_=step_precon((n-1)*h,h,y[n-1,:],f,fe,P,rtol)
    interps.append(interp)
y_s=soln(t)

figs=[]

def plot(plt,x,y,color):
    plt.plot(x.squeeze(),y.real,pen=color)
    if np.iscomplexobj(y):
        plt.plot(x.squeeze(),y.imag,pen=pg.mkPen(color,style=pg.DashLine))
def plot_cmp(plt,t,yb,yr):
    plot(plt,t,yb,'b')
    plot(plt,t,yr,'r')
glw=pg.GraphicsLayoutWidget()
last_plt=None
for m in range(len(y_0)):
    plt=glw.addAlignedPlot()
    plot_cmp(plt,t,y[:,m],y_s[:,m])
    plt.setXLink(last_plt)
    glw.nextRows()
    last_plt=plt
p3=glw.addAlignedPlot()
p3.plot(t.squeeze(),ok,pen='b')
p3.setXLink(p3)
glw.show()
figs.append(glw)

interp=interps[50]
ti=interp.t+h*np.linspace(0,1,50)[:,None]
y_i=interp(ti)
y_si=soln(ti)
glw=pg.GraphicsLayoutWidget()
last_plt=None
for m in range(len(y_0)):
    plt=glw.addAlignedPlot()
    plot_cmp(plt,ti,y_i[:,m],y_si[:,m])
    plt.setXLink(last_plt)
    glw.nextRows()
    last_plt=plt
glw.show()
figs.append(glw)