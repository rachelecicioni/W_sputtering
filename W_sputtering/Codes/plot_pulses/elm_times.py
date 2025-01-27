import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
import h5py
plt.rcParams['lines.linewidth'] = 1.0
dt=40
tmin=47.9-dt
tmax=50.1-dt
tstart=48.0-dt
tstop=49.986-dt
t2D=48.36-dt
t2T=49.27-dt
t2DT=48.52-dt


pulse = int(input("Inserisci il run: "))
user_color = (input("Inserisci il colore(blue/orange/magenta): "))
isotopo=input("Inserisci isotopo(D/T/DT): ")
user='JETPPF'
title = f"{isotopo} {pulse}"

ppf.ppfgo()
fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)
fig.suptitle(title, fontsize=11, color=user_color)
times_imp = np.loadtxt('times_{}.txt'.format(pulse))-dt #qui prendo i tempi salvati con codice Garzotti
times=times_imp[(times_imp>tmin) & (times_imp<tmax)]

#elm
elm = ppf.ppfdata(pulse, 'EDG8', 'Tw1i', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG8', 'Tw1i', uid=user)[2]-dt

ax1.plot(elm_t,elm, color=user_color)
ax1.set_xlim(tmin,tmax)
ax1.set_ylabel(r'$W_{I} (ph/s/cm^2/sr)$')
#ax1.set_ylim(0,1e13)
for i in times:
    ax1.axvline(i, color='dimgrey', linewidth=0.8)
ax1.axvline(tstart, color='green', linestyle='dashed')
ax1.axvline(tstop, color='red', linestyle='dashed')
ax1.axvline(t2T, color='red', linewidth=1.0)
ax1.set_title('(a)', loc='left', pad=-14)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]-dt

ax2.plot(wmhd_t,wmhd*1e-6,color=user_color)
ax2.set_xlim(tmin,tmax)
ax2.set_ylabel(r'$E_p$ (MJ)')
for i in times:
    ax2.axvline(i, color='dimgrey', linewidth=0.8)
ax2.axvline(tstart, color='green', linestyle='dashed')
ax2.axvline(tstop, color='red', linestyle='dashed')
ax2.axvline(t2T, color='red', linewidth=1.0)
ax2.set_title('(b)', loc='left', pad=-14)


#dens
dens = getdat('xg/rtss/pdlmLid', pulse)[0]
dens_t = getdat('xg/rtss/pdlmLid', pulse)[1]-dt

minor_radius=getdat('gs/bl-minrad<s', pulse)[0]
minor_radius_t=getdat('gs/bl-minrad<s', pulse)[1]-dt
minor_radius_final=np.interp(dens_t, minor_radius_t, minor_radius)

elongation = getdat('gs/bl-elo<s', pulse)[0]
elongation_t = getdat('gs/bl-elo<s', pulse)[1]-dt
elongation_final=np.interp(dens_t, elongation_t, elongation)

dens_final=0.1*dens/(2*minor_radius_final*elongation_final)

ax3.plot(dens_t,dens_final, color=user_color)
ax3.set_xlim(tmin,tmax)
ax3.set_ylabel(r'$n_e \cdot 10^{19}(m^{-3})$')
ax3.set_xlabel('time (s)')
for i in times:
    ax3.axvline(i, color='dimgrey', linewidth=0.8)
ax3.axvline(tstart, color='green', linestyle='dashed')
ax3.axvline(tstop, color='red', linestyle='dashed')
ax3.axvline(t2T, color='red', linewidth=1.0)
ax3.set_title('(c)', loc='left', pad=-14)


plt.show()
