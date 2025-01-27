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
n=16 #font size
n2=14

pulse = 96745
user='jnv7243'
ppf.ppfgo()

trand='/home/jnv7243/cmg/catalog/edge2d/jet/96745/jul1124/seq#3/tran'
trant='/home/jnv7243/cmg/catalog/edge2d/jet/96745/aug0124/seq#1/tran'

fig, (ax1, ax2, ax3, ax4)=plt.subplots(nrows=4, ncols=1, sharex=True)

elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=1198, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=886, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=1214, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=1214, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue', label = 'D')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=1221, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=1221, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='green', label='D con Ni')
ax1.set_ylabel(r'$\chi_{ELM}  (m^2/s)$')
ax1.tick_params(axis='both')



#ax1.set_title('(a)', loc='left', pad=-14)
#ax1.set_xlim(9.68,9.86)
#ax1.set_ylim(0,1.5)
#ax1.legend()

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

ax2.plot(td,-yd*myd, color='blue')
ax2.plot(tt,-yt*myt, color='green')
ax2.set_ylabel("Tungsten \n sputtering source (a.u.)")
ax2.tick_params(axis='both')
ax2.set_xlabel('time (s)')


dato3="FZBND_2"

resultd=ep.time(trand, dato3)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato3)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

ax3.plot(td,yd, color='blue')   
ax3.plot(tt,yt, color='black')
ax3.set_xlabel("time (s)")
ax3.tick_params(axis='both')
ax3.set_ylabel("Tungsten core \n boundary flux \n ($s^{-1}$)")
#ax3.set_ylim(-0.5*1e19, 1.5*1e19)

dato4="ZLEVSN_2"

resultd=ep.time(trand, dato4)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

resultt=ep.time(trant, dato4)
tt=np.array(resultt.xData)-dt
yt=np.array(resultt.yData)

ax4.plot(td,yd, color='blue')   
ax4.plot(tt,yt, color='black')
ax4.set_ylabel("W core \n content (a.u.)")

plt.show()
'''
trand='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep2423/seq#5/tran'
trandts='/home/jnv7243/cmg/catalog/edge2d/jet/96745/oct0623/seq#1/tran'

fig, (ax1, ax2)=plt.subplots(nrows=2, ncols=1, sharex=True)

elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=886, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=886, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='deepskyblue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=896, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=896, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='deepskyblue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=947, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=947, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='deepskyblue', label = 'D (W+Be)')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=889, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=889, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=905, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=905, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=948, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=948, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue')
elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=938, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=938, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue', label= 'D (W)')
ax1.set_title(r'$\chi_{ELM} (m^2/s)$', loc='center')
ax1.set_xlim(9.75,9.80)


dato2="YLDT_2"
dato2a="YLDT"

moltd=ep.time(trand, 'GAMIT')
myd=np.array(moltd.yData)

resultd=ep.time(trand, dato2)
td=np.array(resultd.xData)-dt
yd=np.array(resultd.yData)

moltdts=ep.time(trandts, 'GAMIT')
mydts=np.array(moltdts.yData)

resultdts=ep.time(trandts, dato2a)
tdts=np.array(resultdts.xData)-dt
ydts=np.array(resultdts.yData)

ax2.plot(td,-yd*myd, color='deepskyblue')
ax2.plot(tdts,-ydts*mydts, color='blue')
ax2.set_title("W sputtering source (a.u.)", loc='center')
ax2.set_xlabel("time (s)")

plt.show()
'''
