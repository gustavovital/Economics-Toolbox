# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import wbgapi as wb
import plotly.express as px

# To define a Lorenz Curve
def lorenz_curve(y):

    n = len(y)
    y = np.sort(y)
    s = np.zeros(n + 1)
    s[1:] = np.cumsum(y)
    
    cum_people = np.zeros(n + 1)
    cum_income = np.zeros(n + 1)

    for i in range(1, n + 1):
        cum_people[i] = i/n
        cum_income[i] = s[i] / s[n]
    
    return cum_people, cum_income

# Simulate model
n = 2000
sample = np.exp(np.random.randn(n))

fig, ax = plt.subplots()

f_vals, l_vals = lorenz_curve(sample)
ax.plot(f_vals, l_vals, label=f'lognormal sample', lw=2)
ax.plot(f_vals, f_vals, label='equality', lw=2)

ax.vlines([0.8], [0.0], [0.43], alpha=0.5, colors='k', ls='--')
ax.hlines([0.43], [0], [0.8], alpha=0.5, colors='k', ls='--')
ax.set_xlim((0, 1))
ax.set_xlabel("share of households")
ax.set_ylim((0, 1))
ax.set_ylabel("share of wealth")
ax.legend()
plt.show()

