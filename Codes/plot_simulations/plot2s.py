import matplotlib.pyplot as plt
import eproc as ep
from jetto_tools.binary import *
from scipy import signal 
import ppf
plt.rcParams['lines.linewidth'] = 1.0
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

fig, (ax1, ax2, ax3, ax4, ax5)=plt.subplots(nrows=5, ncols=1, sharex=True)

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
ax1.plot(elm_t, elm, color='black')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=859, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=859, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='black')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=925, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=925, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='black', label= 'DT(s.)')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=834, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=834, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=851, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=851, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=912, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=912, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta', label='T')
ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$')
ax1.set_title('(a)', loc='left', pad=-14)
ax1.legend()

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
ax2.plot(tdts,ydts, color='black')
ax2.plot(tt,yt, color='magenta')
ax2.set_title('(b)', loc='left', pad=-14)
ax2.set_ylabel("W core \n content (a.u.)")

dato3="ZTOTAL_2"

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
ax3.plot(tdts,ydts, color='black')
ax3.plot(tt,yt, color='magenta')
ax3.set_title('(c)', loc='left', pad=-14)
ax3.set_ylabel("W core+edge \n content (a.u.)")


dato4="ZCONTE_2"

resultd=ep.time(trand, dato4)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato4)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

resultdts=ep.time(trandts, dato4)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax4.plot(td,yd, color='blue')   
ax4.plot(tdts,ydts, color='black')
ax4.plot(tt,yt, color='magenta')
ax4.set_ylabel("W content (a.u.)")
ax4.set_title('(d)', loc='left', pad=-14)


dato5="ZBND_2"

resultd=ep.time(trand, dato5)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato5)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

resultdts=ep.time(trandts, dato5)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax5.plot(td,yd, color='blue')   
ax5.plot(tdts,ydts, color='black')
ax5.plot(tt,yt, color='magenta')
ax5.set_ylabel("W core boundary \n density ($m^{-3}$)")
ax5.set_title('(e)', loc='left', pad=-14)
ax5.set_xlabel("time (s)")


plt.show()
