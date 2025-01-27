import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 0.8
dt=40.0
tmin=47.9-dt
tmax=50.0-dt
tstart=48.0-dt
tstop=49.986-dt
t2D=48.36-dt
t2T=49.27-dt
t2DT=48.52-dt

#valori Te_ped, ne_ped
ne_ped=5.33*1e19 #m-3
Te_ped=750#eV

#info spari 
pulse=96745
user='JETPPF'
user_sim='jnv7243'
title='D 96745'

ppf.ppfgo()
fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)
fig.suptitle(title, fontsize=11)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]-dt

ax1.plot(wmhd_t,wmhd, color='blue')
ax1.set_xlim(tmin,tmax)
ax1.set_ylabel(r'$E_p$ (J)')

#Te_ped
ax2.set_xlim(tmin,tmax)
ax2.axhline(Te_ped, linestyle='dashed', color='blue')
ax2.set_ylabel(r'$T_{e,ped} (eV)$')

#ne_ped
ax3.set_xlim(tmin,tmax)
ax3.axhline(ne_ped, linestyle='dashed', color='blue')
ax3.set_ylabel(r'$n_{e,ped} (m^{-3})$')
ax3.set_xlabel('time (s)')

num_seq=int(input("Quante sequenze vuoi plottare?(#):  "))

if num_seq==1:

    sequenza=input("Inserisci la sequenza (numero): ")

    wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenza, uid=user_sim) #in J
    ax1.plot(wmhd[2]-dt, wmhd[0], label=sequenza )

    Te_ped = ppf.ppfdata(pulse, 'JST', 'TEBA', seq=sequenza, uid=user_sim) #in eV
    ax2.plot(Te_ped[2]-dt, Te_ped[0], label=sequenza )
    mean_Te=np.mean(Te_ped[0])
    ax2.axhline(mean_Te) 

    ne_ped = ppf.ppfdata(pulse, 'JST', 'NEBA', seq=sequenza, uid=user_sim) #in m-3
    ax3.plot(ne_ped[2]-dt, ne_ped[0], label=sequenza )
    mean_ne=np.mean(ne_ped[0])
    ax3.axhline(mean_ne)
    plt.legend()
    plt.show()



else:
    sequenze=[]
    for  i in range(num_seq):
        elemento=input("Inserisci  la {}^ sequenza (numero): ".format(i+1))
        sequenze.append(elemento)

    for i in range(num_seq):
        wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenze[i], uid=user_sim)
        ax1.plot(wmhd[2]-dt, wmhd[0], label=sequenze[i]  )
        

        Te_ped = ppf.ppfdata(pulse, 'JST', 'TEBA',seq=sequenze[i], uid=user_sim)
        ax2.plot(Te_ped[2]-dt, Te_ped[0], label=sequenze[i] )
        mean_Te=np.mean(Te_ped[0])
        ax2.axhline(mean_Te)

        ne_ped = ppf.ppfdata(pulse, 'JST', 'NEBA',seq=sequenze[i], uid=user_sim)
        ax3.plot(ne_ped[2]-dt, ne_ped[0], label=sequenze[i] )
        mean_ne=np.mean(ne_ped[0])
        ax3.axhline(mean_ne)
    plt.legend()
    plt.show()

