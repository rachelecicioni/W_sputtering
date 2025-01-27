import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 

user='JETPPF'
pulse = 99948

ppf.ppfgo()
ptot_1 = ppf.ppfdata(pulse, 'NBI4', 'PTOT', uid=user)[0]
ptot_t = ppf.ppfdata(pulse, 'NBI4', 'PTOT', uid=user)[2]
somma1=sum(ptot_1)
print(somma1)
media_1=somma1/len(ptot_1)
print(len(ptot_1))
plt.plot(ptot_t,ptot_1)
plt.show()

print(media_1)

ppf.ppfgo()
ptot_2 = ppf.ppfdata(pulse, 'NBI8', 'PTOT', uid=user)[0]
media_2 = np.mean(ptot_2)

print(media_2)
