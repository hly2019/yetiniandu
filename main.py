# -*- coding: utf-8 -*
import numpy as np
import matplotlib.pyplot as plt
x = [297.6, 300.7, 305.5, 310.6, 316.4, 318.6, 321.6, 325.5]
y = [0.793, 0.645, 0.464, 0.327, 0.229, 0.195, 0.175, 0.140]
if __name__ == '__main__':
    plt.figure(figsize=(10, 5), facecolor='w')
    # print(x)
    plt.plot(x, y, 'ro', lw=2, markersize=6)
    plt.grid(b=True, ls=':')
    plt.xlabel(u'X (K)', fontsize=16)
    plt.ylabel(u'Y (Pa*s)', fontsize=16)
    plt.show()
