import mpl_interactions.ipyplot as iplt
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, np.pi, 100)
l = 3

def f1(x, l):
    return x*l

fig, ax = plt.subplots()

controls = iplt.plot(x, f1, l=l, beta=(1, 10, 100), label="f1")
iplt.plot(x, f1, controls=controls, label="f1")
_ = plt.legend()
plt.show()

