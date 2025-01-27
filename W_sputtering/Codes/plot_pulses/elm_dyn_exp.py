import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
dt=40
tstart=48.0-dt
t2D=48.36-dt
t2T=49.27-dt
t2DT=48.52-dt

pulse = int(input("Inserisci il run: "))
user_color = (input("Inserisci il colore(blue/orange/magenta): "))
isotopo=input("Inserisci isotopo(D/T/DT): ")
tmax_in=float(input("inserisci t2(isotopo): "))
tmax=tmax_in-dt
user='JETPPF'
user_s='jnv7243'
times_imp = np.loadtxt('times_{}.txt'.format(pulse))-dt #qui prendo i tempi salvati con codice Garzotti
times=times_imp[(times_imp>tstart) & (times_imp<tmax)]
title = f"{isotopo} {pulse}"

user='JETPPF'

ppf.ppfgo()
fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)
fig.suptitle(title, fontsize=11, color=user_color)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]-dt


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

#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]-dt

ax1.plot(elm_t,elm,color=user_color)
ax1.set_xlim(tstart-0.025,tmax+0.025)
ax1.set_ylabel(r'$Be_{II} (ph/s/cm^2/sr)$')
ax1.set_ylim(0,1e13)
for i in times:
    ax1.axvline(i, color='dimgrey', linewidth=0.8)
ax1.axvline(tstart, color='green', linestyle='dashed')
ax1.axvline(tmax, color='red', linewidth=1.0)
ax1.set_title('(a)', loc='left', pad=-14)


nearest_values_t=[] #array con tutti i tempi di wmhd relativi ad un ELMs
index_wmhd=[]
for i in times:
    diff=np.abs(wmhd_t-i)
    index=np.argmin(diff)
    nearest_values_t.append(wmhd_t[index])
    index_wmhd.append(index)

drop=[]
for k_corr, k_succ in zip(index_wmhd, index_wmhd[1:]):
    min_wmhd=np.min(wmhd[k_corr:k_succ])
    drop.append(np.abs(wmhd[k_corr]-min_wmhd))
drop.append(0)

"""
ax4.plot(nearest_values_t, drop)
ax4.set_ylabel("drop")
"""

drop_rel=[]
drop_abs=[]
for k_corr, k_succ in zip(index_wmhd, index_wmhd[1:]):
    min_wmhd=np.min(wmhd[k_corr:k_succ])
    drop_rel.append(np.abs((wmhd[k_corr]-min_wmhd))/wmhd[k_corr])
    drop_abs.append(np.abs(wmhd[k_corr]-min_wmhd))
drop_rel.append(0)
#drop_abs.append(0)

media=np.mean(drop_rel[:-1])
media_dropabs=np.mean(drop_abs[:-1])
print(drop_rel[:-1])
print("Il drop relativo medio è:  ", media)
print("Il drop assoluto medio è:  ", media_dropabs)

for i in range(len(drop_abs)):
    drop_abs[i] = drop_abs[i] * 1e-6

ax2.scatter(nearest_values_t[:-2], drop_abs[:-1], marker='o', s=20, color=user_color)
ax2.set_ylabel(r'${\Delta E_p}$ (MJ)')
ax2.set_title('(b)', loc='left', pad=-14)

elms=[]
count=0
for i in times:
    count=count+1
    elms.append(count)
ax3.scatter(times,elms, marker='o', s=20, color=user_color)

m, q = np.polyfit(times, elms, 1)
fit_line = m * times + q

ax3.plot(times,fit_line, color='dimgrey',linewidth=0.8)
ax3.set_ylabel(' ELMs (a.u.)')
ax3.set_xlabel('time (s)')
ax3.set_title('(c)', loc='left', pad=-14)

print("La frequenza è: ", m)


plt.show()

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







