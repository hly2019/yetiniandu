import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
temp = [297.6, 300.7, 305.5, 310.6, 316.4, 318.6, 321.6, 325.5]
vis = [0.893, 0.645, 0.464, 0.327, 0.229, 0.195, 0.175, 0.140]
temp_ans = []
vis_ans = []
for it in temp:
    temp_ans.append( (1/it))
print(temp_ans)
print("*********************")
for it in vis:
    vis_ans.append( math.log(it))
print(vis_ans)
if __name__ == '__main__':
    plt.figure(figsize=(10, 5), facecolor='w')
    plt.plot(temp_ans, vis_ans, 'ro', lw=2, markersize=6)
    plt.grid(b=True, ls=':')
    plt.xlabel(u'X', fontsize=16)
    plt.ylabel(u'Y', fontsize=16)
    plt.show()
    print("********")