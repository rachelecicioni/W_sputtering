import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
dt=40
tmin=47.9-dt
tmax=50.1-dt
tstart=48.0-dt
tstop=49.986-dt
t2D=48.36-dt
t2T=49.27-dt
t2DT=48.52-dt
n=14 #font size
n2=14
#IMPORTANTE: CAMBIARE IL TEMPO IN BASE ALL'ISOTOPO NEL CODICE
pulse = int(input("Inserisci il run: "))
user_color = (input("Inserisci il colore(blue/orange/magenta): "))
isotopo=input("Inserisci isotopo(D/T/DT): ")
user='JETPPF'


ppf.ppfgo()
times_imp = np.loadtxt('times_{}.txt'.format(pulse))-dt #qui prendo i tempi salvati con codice Garzotti
times=times_imp[(times_imp>tmin) & (times_imp<tmax)]


#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]-dt

plt.plot(elm_t,elm, color=user_color)
plt.xlim(tmin,tmax)
plt.title(r'$Be_{II} (ph/s/cm^2/sr)$', loc='center')
plt.axvline(tstart, color='green', linestyle='dashed')
plt.axvline(tstop, color='red', linestyle='dashed')
plt.axvline(t2D, color='red', linewidth=1.0)
plt.ylim(0,6*1e12)
plt.fill_between(elm_t, 1e13,  where=(elm_t >= tstart) & (elm_t <= t2D), color='yellow', alpha=0.5)

for i in times:
    if i < t2D:
        plt.axvline(x=i, color='dimgrey', linewidth=0.8)


plt.show()

wmhd = getdat('xg/rtss/wmhd', pulse)[0]*1e-6
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]-dt

plt.plot(wmhd_t,wmhd,color=user_color)
plt.xlim(tstart-0.025,t2D+0.025)
plt.title(r'$E_p$ (MJ)', loc='center')
plt.xlabel('time (s)')
for i in times:
    plt.axvline(i, color='dimgrey', linewidth=0.8)
plt.ylim(3,7)
plt.axvline(tstart, color='green', linestyle='dashed')
plt.axvline(t2D, color='red', linewidth=1.0)


plt.show()
