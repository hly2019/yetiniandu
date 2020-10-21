import numpy as np



d = [1.225,1.188,1.193,1.181,1.191,1.199,1.195,1.187,1.191,1.175,1.190,1.198]
tim = [38.77, 38.43, 38.52 ,38.5 ,38.11 ,37.03]
sum = 0
ans =  np.std(tim,ddof=1)
ans2 = np.std(d,ddof=1)

print(ans)
print(ans2)