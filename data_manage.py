from  test import vis_ans,temp_ans
import numpy as np 
import matplotlib.pyplot as plt
def Least_squares(x,y):
    x_ = x.mean()
    y_ = y.mean()
    m = np.zeros(1)
    n = np.zeros(1)
    k = np.zeros(1)
    p = np.zeros(1)
    for i in np.arange(8):
        k = (x[i]-x_)* (y[i]-y_)
        m += k
        p = np.square( x[i]-x_ )
        n = n + p
    a = m/n
    b = y_ - a* x_
    return a,b
if __name__ == '__main__':
    print("******")
    print(np.std(temp_ans,ddof=1))
    x = np.array(temp_ans)
    y = np.array(vis_ans)
    print(x)
    print(y)
    a,b = Least_squares(x,y)
    print ("a : ")
    print(a)
    print ("b : ")
    print(b)
    y1 = a * x + b
    plt.figure(figsize=(10, 5), facecolor='w')
    plt.plot(x, y, 'ro', lw=2, markersize=6)
    plt.plot(x, y1, 'r-', lw=2, markersize=6)
    plt.grid(b=True, ls=':')
    plt.xlabel(u'X (1/T)', fontsize=16)
    plt.ylabel(u'Y (lnη)', fontsize=16)
    plt.show()