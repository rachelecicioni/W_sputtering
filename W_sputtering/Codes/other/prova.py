import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
tmin=48.0
tmax=49.9

pulse = int(input("Inserisci il run: "))
user='JETPPF'
user_s='jnv7243'
times_imp = np.loadtxt('times_{}.txt'.format(pulse)) #qui prendo i tempi salvati con codice Garzotti
times=times_imp[(times_imp>tmin) & (times_imp<tmax)]

frequenze=[]
for i in range(len(times) - 1):
    frequenze.append(1/(times[i+1]-times[i]))

frequenze.append(0)

user='JETPPF'

ppf.ppfgo()
fig, (ax1, ax2, ax3, ax4, ax5, ax6)=plt.subplots(nrows=6, ncols=1, sharex=False)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]

ax1.plot(wmhd_t,wmhd)
ax1.set_xlim(tmin,tmax)
ax1.set_ylabel("WMHD")
for i in times:
    ax1.axvline(i)

#dens
dens = getdat('xg/rtss/pdlmLid', pulse)[0]
dens_t = getdat('xg/rtss/pdlmLid', pulse)[1]

minor_radius=getdat('gs/bl-minrad<s', pulse)[0]
minor_radius_t=getdat('gs/bl-minrad<s', pulse)[1]
minor_radius_final=np.interp(dens_t, minor_radius_t, minor_radius)

elongation = getdat('gs/bl-elo<s', pulse)[0]
elongation_t = getdat('gs/bl-elo<s', pulse)[1]
elongation_final=np.interp(dens_t, elongation_t, elongation)

dens_final=0.1*dens/(2*minor_radius_final*elongation_final)

ax2.plot(dens_t,dens_final)
ax2.set_xlim(tmin,tmax)
ax2.set_ylabel("dens (e17 m-3)")
for i in times:
    ax2.axvline(i)

#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]

ax3.plot(elm_t,elm)
ax3.set_xlim(tmin,tmax)
ax3.set_ylabel("elm")
ax3.set_ylim(0,1e13)
for i in times:
    ax3.axvline(i)



nearest_values_t=[] #array con tutti i tempi di wmhd relativi ad un ELMs
index_wmhd=[] #array con gli indici di wmhd corripondenti (più vicini) ad un ELMs
for i in times:
    diff=np.abs(wmhd_t-i)
    index=np.argmin(diff)
    nearest_values_t.append(wmhd_t[index])
    index_wmhd.append(index)

drop=[]
for k in index_wmhd:
    min_wmhd=np.min(wmhd[k:k+10])
    drop.append(np.abs((wmhd[k]-min_wmhd)/wmhd[k]))

ax4.plot(nearest_values_t, drop)
ax4.set_ylabel("drop")



nearest_values_t2=[] #array con tutti i tempi di elms relativi ad un ELMs
index_elms=[]
size=[]
for i in times:
    diff=np.abs(elm_t-i)
    index2=np.argmin(diff) #restituisce l'indice dell'elemento (di elms_t) con il tempo più vicino a times
    nearest_values_t2.append(elm_t[index2])
    index_elms.append(index2)
    sub_array=elm[index2-5:index2+5]
    max_value=np.max(sub_array)
    size.append(max_value)




ax5.plot(times, size)
ax6.plot(times,drop)

plt.show()

plt.scatter(size, drop)

plt.show()

print(times)
print(frequenze)
print(drop)




