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
n=25 #font size
n2=20

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

plt.figure(figsize=(12,6))
plt.plot(elm_t,elm, color=user_color)
plt.xlim(tmin,tmax)
plt.xlabel('time(s)', fontsize=n)
plt.axvline(tstart, color='green', linestyle='dashed')
plt.axvline(tstop, color='red', linestyle='dashed')
plt.axvline(t2DT, color='red', linewidth=1.0)
plt.ylabel(r'$Be_{II} (ph/s/cm^2/sr)$', fontsize=n)
plt.ylim(0,1e13)
plt.xticks(fontsize=n2)
plt.yticks(fontsize=n2)
plt.fill_between(elm_t, 1e13,  where=(elm_t >= tstart) & (elm_t <= t2DT), color='yellow', alpha=0.5)
plt.title('DT #99948', color=user_color, fontsize=n)


'''
elm2 = ppf.ppfdata(99950, 'EDG7', 'BE2H', uid=user)[0]
elm_t2 = ppf.ppfdata(99950, 'EDG7', 'BE2H', uid=user)[2]-dt

ax2.plot(elm_t2,elm2, color='black')
ax2.set_xlim(tmin,tmax)
ax2.set_xlabel('time(s)')
ax2.set_ylabel(r'$Be_{II} (ph/s/cm^2/sr)$')
ax2.set_title('Hybrid scenario #99950')
'''

plt.show()

fig, (ax1, ax2)=plt.subplots(nrows=2, ncols=1, sharex=True)
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]-dt


ax1.plot(elm_t,elm,color=user_color)
ax1.set_xlim(tstart-0.025,t2DT+0.025)
ax1.set_ylabel(r'$Be_{II} (ph/s/cm^2/sr)$', fontsize=n)
ax1.set_ylim(0,7*1e12)
for i in times:
    ax1.axvline(i, color='dimgrey', linewidth=0.8)
ax1.axvline(tstart, color='green', linestyle='dashed')
ax1.axvline(t2DT, color='red', linewidth=1.0)
ax1.tick_params(axis='both', labelsize=n2)
ax1.set_title('Deuterium+Tritium', fontsize=n, color=user_color)

wmhd = getdat('xg/rtss/wmhd', pulse)[0]*1e-6
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]-dt

ax2.plot(wmhd_t,wmhd,color=user_color)
ax2.set_xlim(tstart-0.025,t2DT+0.025)
ax2.set_ylabel(r'$E_p$ (MJ)',fontsize=n)
ax2.set_xlabel('time (s)', fontsize=n)
for i in times:
    ax2.axvline(i, color='dimgrey', linewidth=0.8)
ax2.set_ylim(3,8)
ax2.tick_params(axis='both', labelsize=n2)
ax2.axvline(tstart, color='green', linestyle='dashed')
ax2.axvline(t2DT, color='red', linewidth=1.0)


plt.show()