import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 0.8
tmin=47.9
tmax=50.0
tstart=48.0
tstop=49.986

pulse = int(input("Inserisci il run: "))

times_imp = np.loadtxt('times_{}.txt'.format(pulse)) #qui prendo i tempi salvati con codice Garzotti
times=times_imp[(times_imp>tmin) & (times_imp<tmax)]
print(times)
differenze=[]
for i in range(len(times)-1):
    diff=times[i+1]-times[i]
    differenze.append(diff)

for i in range(len(differenze)-1):
    media=np.mean(differenze[:i])
    media_next=np.mean(differenze[i:])
    if differenze[i+1]>2*media: # and media_next>2*media: #da inserire solo per D e T
        print(i)
        print(times[i])
        

