import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

user='JETPPF'

shot_d=96745
shot_t=99282
shot_dt=99948

ppf.ppfgo()

dt=40
tmin=7.5
tmax=10.5

fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)
fig.suptitle(r'$I_p$=3.5 MA. $B_T$=3.3 T')
'''
#------------------------------------------------------------------------------------- corrente di plasma in funzione del tempo
dda_1='MAGN'
dtype_1='IPLA'

ip_d = ppf.ppfdata(shot_d, dda_1, dtype_1, uid=user)[0]
ip_t = ppf.ppfdata(shot_t, dda_1, dtype_1, uid=user)[0]
ip_dt = ppf.ppfdata(shot_dt, dda_1, dtype_1, uid=user)[0]
ip_time_d = ppf.ppfdata(shot_d, dda_1, dtype_1 , uid=user)[2]-dt
ip_time_t = ppf.ppfdata(shot_t, dda_1, dtype_1 , uid=user)[2]-dt
ip_time_dt = ppf.ppfdata(shot_dt, dda_1, dtype_1 , uid=user)[2]-dt

ip_d_out=-1*1e-6*ip_d #così lo mette in MA e lo rigira
ip_t_out=-1*1e-6*ip_t
ip_dt_out=-1*1e-6*ip_dt

#ax1.set_ylabel(r'$I_p$ (MA)')
ax1.set_title(r'$I_p (MA)$', loc='center', pad=-14,y=1.2)
ax1.plot(ip_time_d, ip_d_out, color ='blue')
ax1.plot(ip_time_t, ip_t_out, color ='darkmagenta')
ax1.plot(ip_time_dt, ip_dt_out, color ='orangered')
#ax1.legend(['D {}'.format(shot_d), 'T {}'.format(shot_t), 'DT {}'.format(shot_dt)])
'''
#-------------------------------------------------------------------------------------- total coupled power in fuzione del tempo
dda_2='ICRH'
dtype_2='PTOT'
dda_3='NBI'
dtype_3='PTOT'

icrh_ptot_d = ppf.ppfdata(shot_d, dda_2, dtype_2, uid=user)[0]
icrh_ptot_t = ppf.ppfdata(shot_t, dda_2, dtype_2, uid=user)[0]
icrh_ptot_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2, uid=user)[0]
icrh_ptot_time_d = ppf.ppfdata(shot_d, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_t = ppf.ppfdata(shot_t, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2 , uid=user)[2]-dt

nbi_ptot_d = ppf.ppfdata(shot_d, dda_3, dtype_3, uid=user)[0]
nbi_ptot_t = ppf.ppfdata(shot_t, dda_3, dtype_3, uid=user)[0]
nbi_ptot_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3, uid=user)[0]
nbi_ptot_time_d = ppf.ppfdata(shot_d, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_t = ppf.ppfdata(shot_t, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_out_d=1e-6*nbi_ptot_d #mette in MW
nbi_ptot_out_t=1e-6*nbi_ptot_t
nbi_ptot_out_dt=1e-6*nbi_ptot_dt

icrh_ptot_d_out=1e-6*icrh_ptot_d
icrh_ptot_t_out=1e-6*icrh_ptot_t
icrh_ptot_dt_out=1e-6*icrh_ptot_dt

#ax1.set_ylabel(r'$P_{NBI}, P_{ICRH}$ (MW)')
ax1.set_title(r'$P_{NBI}, P_{ICRH} (MW)$', loc='center', pad=-14, y=1.2)
ax1.plot(nbi_ptot_time_d, nbi_ptot_out_d, color='blue')
ax1.plot(nbi_ptot_time_t, nbi_ptot_out_t, color='darkmagenta')
ax1.plot(nbi_ptot_time_dt, nbi_ptot_out_dt, color='orangered')
ax1.plot(icrh_ptot_time_d, icrh_ptot_d_out, color='blue')
ax1.plot(icrh_ptot_time_t, icrh_ptot_t_out, color='darkmagenta')
ax1.plot(icrh_ptot_time_dt, icrh_ptot_dt_out, color='orangered')
ax1.set_xlim(tmin, tmax)

#-------------------------------------------------------------------------------------ELMs
dda_4='EDG7'
dtype_4='BE2H'

elm_d = ppf.ppfdata(shot_d, dda_4, dtype_4, uid=user)[0]*1e-13
elm_t = ppf.ppfdata(shot_t, dda_4, dtype_4, uid=user)[0]*1e-13+1
elm_dt = ppf.ppfdata(shot_dt, dda_4, dtype_4, uid=user)[0]*1e-13+2
elm_time_d = ppf.ppfdata(shot_d, dda_4, dtype_4 , uid=user)[2]-dt
elm_time_t = ppf.ppfdata(shot_t, dda_4, dtype_4 , uid=user)[2]-dt
elm_time_dt = ppf.ppfdata(shot_dt, dda_4, dtype_4 , uid=user)[2]-dt

#ax2.set_ylabel(r'$Be_{II} (ph/s/cm^2/sr)$')
ax2.set_title(r'ELMs (a.u.)', loc='center', pad=-14, y=1.2)
ax2.plot(elm_time_d, elm_d, color='blue')
ax2.plot(elm_time_t, elm_t, color='darkmagenta')
ax2.plot(elm_time_dt, elm_dt, color='orangered')
ax2.set_ylim(0,4)

#----------------------------------------------------------------------------------------------radiation
dda_5='BOL4'
dtype_5='TXPN'
'''
rad_d = ppf.ppfdata(shot_d, dda_5, dtype_5, uid=user)[0]
rad_t = ppf.ppfdata(shot_t, dda_5, dtype_5, uid=user)[0]
rad_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5, uid=user)[0]
rad_time_d = ppf.ppfdata(shot_d, dda_5, dtype_5 , uid=user)[2]-dt
rad_time_t = ppf.ppfdata(shot_t, dda_5, dtype_5 , uid=user)[2]-dt
rad_time_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5 , uid=user)[2]-dt

ax3.set_xlabel("time (s)")
ax3.set_ylabel(r'$P_{rad}$') #CAMBIA
ax3.set_title('(d)', loc='left', pad=-14)
ax3.plot(rad_time_d, rad_d, color='blue')
ax3.plot(rad_time_t, rad_t, color='darkmagenta')
ax3.plot(rad_time_dt, rad_dt, color='orangered')

plt.show()
'''
#tentativo real time system
rad_d = getdat('xg/rtss/kb5Ptot', shot_d)[0]*1e-6
rad_t = getdat('xg/rtss/kb5Ptot', shot_t)[0]*1e-6
rad_dt = getdat('xg/rtss/kb5Ptot', shot_dt)[0]*1e-6
rad_time_d = getdat('xg/rtss/kb5Ptot', shot_d)[1]-dt
rad_time_t = getdat('xg/rtss/kb5Ptot', shot_t)[1]-dt
rad_time_dt = getdat('xg/rtss/kb5Ptot', shot_dt)[1]-dt

ax3.set_xlabel("time (s)")
#ax3.set_ylabel(r'$P_{rad TOT} (MW)$') 
ax3.set_title(r'$P_{rad TOT} (MW)$', loc='center', pad=-14, y=1.2)
ax3.plot(rad_time_d, rad_d, color='blue')
ax3.plot(rad_time_t, rad_t, color='darkmagenta')
ax3.plot(rad_time_dt, rad_dt, color='orangered')
ax3.set_ylim(0,30)

plt.show()

#fig.savefig('/home/jnv7243/PLOT/figure/multiplot_poster.pdf', format='pdf')
