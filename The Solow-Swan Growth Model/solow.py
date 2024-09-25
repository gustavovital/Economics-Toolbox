## Modules
import numpy as np
import matplotlib.pyplot as plt

# graphical perspective of solow-swan model

A, s, alpha, delta = 2, .3, .3, .4
x0 = .25
xmin, xmax = 0, 3

# now we gotta define a function for t+1 (g(t) = f(t+1))
def g(A, s, alpha, delta, k):
    return s * A * k ** alpha + (1 - delta)*k


def plot45(kstar=None):

    xgrid = np.linspace(xmin, xmax, 12000)
    
    fig, ax = plt.subplots()
    ax.set_xlim(xmin, xmax)
    g_values = g(A, s, alpha, delta, xgrid)
    ymin, ymax = np.min(g_values), np.max(g_values)

    ax.set_ylim(ymin, ymax)
    lb = r'$sAk^{\alpha} + (1 - \delta)k$'

    ax.plot(xgrid, g_values,  lw=2, alpha=0.6, label=lb)
    ax.plot(xgrid, xgrid, 'k-', lw=1, alpha=0.7, label='$45^{\circ}$')
    
    if kstar:

        fps = (kstar,)

        ax.plot(fps, fps, 'go', ms=10, alpha=0.6)
        ax.annotate(r'$k^* = (sA / \delta)^{(1/(1-\alpha))}$',
                 xy=(kstar, kstar),
                 xycoords='data',
                 xytext=(-40, -60),
                 textcoords='offset points',
                 fontsize=14,
                 arrowprops=dict(arrowstyle="->"))
        
    
    ax.legend(loc='upper left', frameon=False, fontsize=12)

    ax.set_xticks((0, 1, 2, 3))
    ax.set_yticks((0, 1, 2, 3))

    ax.set_xlabel('$k_t$', fontsize=12)
    ax.set_ylabel('$k_{t+1}$', fontsize=12)
    plt.show()


plot45()


