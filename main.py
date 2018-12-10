# グラフ化に必要なものの準備
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt


k1=-2.97
k2=-1.02
x1=0.523599
x2=0
dt=0.01
f1=x2
tau=1.272
f2=(-9.784735*tau)
xaxis=np.arange(0,10,0.01)
yaxis=np.array([x1])
tauaxis=np.array([tau])
#初期値入力


for t in range(1 ,1000, 1):

    x1+=(f1*dt)
    x2+=(f2*dt)
    f1=x2

    T=(-k1*x1)+(-k2*x2)
    print(x1, x2 ,T)
    if T>0 :
        hugo=1
    else :
        hugo=-1

    if abs(T)>1.272 :
        tau=1.272*hugo
    else :
        tau=T

    f2 = (-9.784735 * tau)
    yaxis = np.append(yaxis, x1)
    tauaxis=np.append(tauaxis,tau)

plt.plot(xaxis,yaxis,color="c", linewidth=3,alpha=1,label='x1')
plt.plot(xaxis,tauaxis,color="m", linewidth=3,alpha=0.5,label='τ')
plt.legend()
plt.title('simulation result -2±2i')
plt.show()

