import numpy as np
import mathx
from qdht import QDHT
import pyqtgraph_extended as pg


def test_self_trans(N=32,R=None):
    """Test self-transform of exp(-r**2/2)"""
    ht=QDHT(N)
    if R is None:
        # For same r and k axes
        R=ht.j_Np1**0.5
    r=ht.points(R)
    k=ht.conj_points(R)
    Er=np.exp(-r**2/2)
    print(ht.norm_squared(Er,R))
    Ek=ht.transform(Er,R)
    print(ht.conj_norm_squared(Ek,R))
    plt=pg.plot(r,Er)
    plt.plot(k,Ek,pen='r')
    
def test_arb_trans():
    ##
    ht=QDHT(64)
    R=5
    r=ht.points(R)
    k=ht.conj_points(R)
    Er=np.exp(-r**2/2)
    Ek=ht.transform(Er,R)
    Eka=ht.transform_to_arb(Er,R,k)
    assert np.allclose(Ek,Eka)
    Eka=ht.transform_to_arb(Er,R,mathx.reshape_vec(k,-3))
    assert np.allclose(Ek,Eka.squeeze()) and Eka.shape==(64,1,1)
    
    R=ht.j_Np1**0.5
    r=ht.points(R)
    k=ht.conj_points(R)
    Er=np.exp(-r**2/2)
    Erp=-r*np.exp(-r**2/2)
    Ekp=ht.transform_to_arb(Er,R,k,deriv=1)
    assert np.allclose(Erp,Ekp)
    plt=pg.plot(r,Erp,pen=pg.mkPen('b',width=10))
    plt.plot(k,Ekp,pen='r')
    ##
    
if __name__=="__main__":
    test_arb_trans()
    test_self_trans()
    test_self_trans(R=5)
   
