from feon.sa import *
import numpy as np
from feon.tools import pair_wise
import matplotlib.pyplot as plt
from matplotlib import cm
if __name__ == "__main__":
    E = 210e6
    P = 18
    X = np.linspace(0,3,6)
    _X = X -0.3
    
    A = [0.002+0.01*val/3. for val in _X[1:]]
    A.reverse()

    nds = [Node(x,0) for x in X]
    els = []

    count = 0
    for nd in pair_wise(nds):
        els.append(Link1D11(nd,E,A[count]))
        count += 1

    s = System()
    s.add_nodes(nds)
    s.add_elements(els)


    s.add_fixed_sup(0)
    s.add_node_force(nds[-1].ID,Fx = 18)
    s.solve()

    stress = np.array([el.sx[0][0] for el in els])
    a = np.zeros((5,5))
    fig, ax = plt.subplots()
    
    for i in xrange(5):
        a[i,:] = stress
    cax = ax.imshow(a,interpolation='nearest', cmap=cm.coolwarm)
    cbar = fig.colorbar(cax, orientation='horizontal')  
    plt.show()


    
