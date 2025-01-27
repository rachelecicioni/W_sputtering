import matplotlib.pyplot as plt
import eproc as ep
from jetto_tools.binary import *
from scipy import signal 
import ppf
plt.rcParams['lines.linewidth'] = 1.0
n=16 #font size
n2=14
dt=40
tmin=47.9-dt
tmax=50.0-dt
tstart=48.0-dt
tstop=49.986-dt

pulse = 96745
user='jnv7243'
ppf.ppfgo()

trand='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep2423/seq#5/tran'
trandts='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep2223/seq#4/tran'
trant='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep1523/seq#2/tran'

fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)

elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=886, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=886, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=896, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=896, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=947, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=947, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue', label = 'D')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=847, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=847, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='orangered')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=859, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=859, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='orangered')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=925, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=925, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='orangered', label= 'DT(s.)')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=834, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=834, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='darkmagenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=851, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=851, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='darkmagenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=912, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=912, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='darkmagenta', label='T')
ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$', fontsize=n)
ax1.tick_params(axis='both', labelsize=n2)
ax1.set_xlim(9.68,9.85)
ax1.set_ylim(0,1.5)


dato2="ZLEVSN_2"

resultd=ep.time(trand, dato2)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato2)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

resultdts=ep.time(trandts, dato2)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax2.plot(td,yd, color='blue')   
ax2.plot(tdts,ydts, color='orangered')
ax2.plot(tt,yt, color='darkmagenta')
ax2.set_ylabel("Tungsten \n core content \n (a.u.)", fontsize=n)
ax2.tick_params(axis='both', labelsize=n2)
ax2.set_ylim(0.5*1e18, 1.5*1e18)

dato3="ZRADSN_2"

resultd=ep.time(trand, dato3)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato3)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

resultdts=ep.time(trandts, dato3)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax3.plot(td,yd, color='blue')   
ax3.plot(tdts,ydts, color='orangered')
ax3.plot(tt,yt, color='darkmagenta')
ax3.set_ylabel("Tungsten \n core radiation \n (MW)", fontsize=n)
ax3.set_xlabel("time (s)", fontsize=n)
ax3.tick_params(axis='both', labelsize=n2)
ax3.set_ylim(5,20)


plt.show()
