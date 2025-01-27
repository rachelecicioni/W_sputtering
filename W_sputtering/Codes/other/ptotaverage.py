import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

pulse = 105489
user='JETPPF'

ppf.ppfgo()

ptot4=ppf.ppfdata(pulse, 'NBI4', 'PTOT', uid=user)[0]
ptot4_t=ppf.ppfdata(pulse, 'NBI4', 'PTOT', uid=user)[2]

plt.plot(ptot4_t, ptot4)
plt.show()

ptot8=ppf.ppfdata(pulse, 'NBI8', 'PTOT', uid=user)[0]
ptot8_t=ppf.ppfdata(pulse, 'NBI8', 'PTOT', uid=user)[2]

plt.plot(ptot8_t, ptot8)
plt.show()

def index(array, valore):
    differenze = np.abs(array - valore)
    indice_piu_vicino = np.argmin(differenze)
    
    return indice_piu_vicino

min4=index(ptot4_t,48.09)
max4=index(ptot4_t, 49.15)

ptot4=ptot4[min4:max4]

print(min4)
print(max4)

min8=index(ptot8_t,48.46)
max8=index(ptot8_t, 50.79)

ptot8=ptot8[min8:max8]

print(min8)
print(max8)

nbi4=np.mean(ptot4)
nbi8=np.mean(ptot8)

print(nbi4)
print(nbi8)