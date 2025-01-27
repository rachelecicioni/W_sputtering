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

trand='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep2423/seq#6/tran'
trandts='/home/jnv7243/cmg/catalog/edge2d/jet/96745/oct0223/seq#4/tran'
trant='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep1523/seq#3/tran'

fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)

elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=889, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=889, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=905, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=905, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=938, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=938, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=948, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=948, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue', label = 'D')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=907, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=907, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='orange')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=977, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=977, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='orange', label= 'DT(n.s.)')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=835, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=835, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=867, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=867, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=914, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=914, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='magenta', label='T')
ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$')
ax1.set_title('(a)', loc='left', pad=-14)
ax1.legend()

dato2="YLDT_2"

moltd=ep.time(trand, 'GAMIT')
myd=np.array(moltd.yData)

resultd=ep.time(trand, dato2)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

moltt=ep.time(trant, 'GAMIT')
myt=np.array(moltt.yData)

resultt=ep.time(trant, dato2)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

moltdts=ep.time(trandts, 'GAMIT')
mydts=np.array(moltdts.yData)

resultdts=ep.time(trandts, dato2)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax2.plot(td,-yd*myd, color='blue')
ax2.plot(tdts,-ydts*mydts, color='orange')
ax2.plot(tt,-yt*myt, color='magenta')
ax2.set_title('(b)', loc='left', pad=-14)
ax2.set_ylabel("W sputtering source (a.u.)")

dato3="FZBND_2"

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
ax3.plot(tdts,ydts, color='orange')
ax3.plot(tt,yt, color='magenta')
ax3.set_xlabel("time (s)")
ax3.set_title('(c)', loc='left', pad=-14)
ax3.set_ylabel(r"W core boundary flux ($s^{-1}$)")

plt.show()
