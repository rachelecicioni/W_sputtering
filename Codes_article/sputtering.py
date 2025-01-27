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
n=8 #font size
n2=8

pulse = 96745
user='jnv7243'
ppf.ppfgo()

tranbew='/home/jnv7243/cmg/catalog/edge2d/jet/96745/jun0724/seq#1/tran'
tranbewni='/home/jnv7243/cmg/catalog/edge2d/jet/96745/jun2024/seq#2/tran'

fig, (ax1, ax2, ax3, ax4, ax5)=plt.subplots(nrows=5, ncols=1, sharex=True)

elm = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1114, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1114, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='green', label = 'Be')
elm = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1153, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1153, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='blue', label = 'Be+W')
elm = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1179, uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=1179, uid=user)[2]-dt
ax1.plot(elm_t, elm, color='red', label= 'Be+W+Ni')
ax1.set_title('(a) XEBA', loc='left', pad=-14)
ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$', fontsize=n)
#ax1.set_xlim(9.68,9.86)
#ax1.set_ylim(0,1.5)
ax1.legend()

dato2="YLDT_2"

molt=ep.time(tranbewni, 'GAMIT')
my=np.array(molt.yData)

result=ep.time(tranbewni, dato2)
t=np.array(result.xData)-dt
y=np.array(result.yData)

ax2.plot(t,-y*my, color='black')
ax2.set_title('(b) -GAMIT*YLDT_2', loc='left', pad=-14)
ax2.set_ylabel("W \n sputtering source \n (a.u.)", fontsize=n)
ax2.tick_params(axis='both', labelsize=n2)
#ax2.set_ylim(0,2.5*1e21)


dato3="FZBND_2"

result=ep.time(tranbewni, dato3)
t=np.array(result.xData)-dt
y=np.array(result.yData)
  
ax3.plot(t,y, color='black')
ax3.set_xlabel("time (s)", fontsize=n)
ax3.tick_params(axis='both', labelsize=n2)
ax3.set_title('(c) FZBND_2', loc='left', pad=-14)
#ax3.set_ylim(-0.5*1e19, 1.5*1e19)
ax3.set_ylabel("W core \n boundary flux \n ($s^{-1}$)", fontsize=n)

dato4="ZLEVSN_2"

result=ep.time(tranbewni, dato4)
t=np.array(result.xData)-dt
y=np.array(result.yData)
  
ax4.plot(t,y, color='black')
ax4.set_xlabel("time (s)", fontsize=n)
ax4.tick_params(axis='both', labelsize=n2)
ax4.set_title('(d) ZLEVSN_2', loc='left', pad=-14)
#ax3.set_ylim(-0.5*1e19, 1.5*1e19)
ax4.set_ylabel("W core \n content \n (a.u.)", fontsize=n)


dato5="ZRADSN_2"

result=ep.time(tranbewni, dato5)
t=np.array(result.xData)-dt
y=np.array(result.yData)
  
ax5.plot(t,y, color='black')
ax5.set_xlabel("time (s)", fontsize=n)
ax5.tick_params(axis='both', labelsize=n2)
ax5.set_title('(e) ZRADSN_2', loc='left', pad=-14)
#ax3.set_ylim(-0.5*1e19, 1.5*1e19)
ax5.set_ylabel("W core \n radiation \n (MW)", fontsize=n)

plt.show()