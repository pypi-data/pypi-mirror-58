from ode import splitstep
import numpy as np
import fourier
import pyqtgraph_extended as pg
from ode import drive
import scipy

t=np.linspace(-20,20,400)
omega=fourier.conj_axis(t)
ft=fourier.FTD(sign=-1,x=t,k=omega)
#Et=np.exp(-0.5*t**2)
Et=1./scipy.cosh(t)
#Et=5*np.random.randn(*t.shape)
Ef=ft.trans(Et)
#Ef=Ef*np.exp(-0.1*omega**2)
beta_2=-1
gamma=1

def prop_1(z,Ef,h):
    return np.exp(0.5j*h*beta_2*omega**2)*Ef

def prop_2(z,Et,h):
    return np.exp(1j*h*gamma*Et*Et.conj())*Et

glw=pg.GraphicsLayoutWidget()
tplt=glw.addAlignedPlot(labels={'left':'|E(t)|','bottom':'t'},title='-')
tplt.plot(t,abs(Et),pen='b')
tl=tplt.plot(pen='r')
glw.nextRows()
fplt=glw.addAlignedPlot(labels={'left':'|E(omega)|','bottom':'omega'})
fplt.plot(omega,abs(Ef),pen='b')
fl=fplt.plot(pen='r')
glw.show()

def update_plot(_,z,Ef,h,steps,interp):
    if glw.isHidden():
        return True # terminate
    Et=ft.inv_trans(Ef)
    tplt.setTitle('#%d, z=%.3f, h=%.3f'%(steps,z,h))
    tl.setData(t,abs(Et))
    fl.setData(omega,abs(Ef))
    pg.QtGui.QApplication.processEvents()
    
def step(z,h,Ef,_):
    return splitstep.adaptive(z,Ef,h,prop_1,ft.inv_trans,prop_2,ft.trans,1e-5)

steps_queue=drive.EventQueue()
steps_queue.add_event(0,update_plot,1)
drive.go(0,Ef,step,0.1,steps_queue=steps_queue)








