import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

fig, ((ax1, ax2), (ax3,ax4))=plt.subplots(nrows=2, ncols=2)
fig.suptitle('T', fontsize=11)

xmin_L=1.9
xmax_L=2.6
x_L= np.linspace(xmin_L, xmax_L, 100)

x8=[2.0,2.4]
y8=[65117,75108]
ax1.plot(x8, y8, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='b')

x9=[2.0,2.1,2.2,2.3]
y9=[80988,90145,86670,80614]
ax1.plot(x9, y9, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.9$')
m, q = np.polyfit(x9, y9, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='y')

x1=[2.0,2.1,2.2]
y1=[84675,99570,101972]
ax1.plot(x1, y1, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=1.0$')
m, q = np.polyfit(x1, y1, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='r')

ax1.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax1.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax1.set_title('')  # Titolo del grafico
ax1.legend()  # Mostra la legenda
ax1.grid(True)  # Attiva la griglia

ax1.axhline(y=93715, color='black', linestyle='--')

x8=[2.0,2.4]
y8=[83.4484,35.9726]
ax2.plot(x8, y8, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='b')

x9=[2.0,2.1,2.2,2.3]
y9=[68.26,55.0,51.4308,32.160]
ax2.plot(x9, y9, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.9$')
m, q = np.polyfit(x9, y9, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='y')

x1=[2.0,2.1,2.2]
y1=[70.9091,54.4424,46.7391]
ax2.plot(x1, y1, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=1.0$')
m, q = np.polyfit(x1, y1, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='r')

ax2.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax2.set_ylabel('f (Hz)')  # Etichetta asse y
ax2.set_title('')  # Titolo del grafico
ax2.legend()  # Mostra la legenda
ax2.grid(True)  # Attiva la griglia

ax2.axhline(y=33.5, color='black', linestyle='--')

xmin=0.5
xmax=1.55
x = np.linspace(xmin, xmax, 100)

x20=[0.8,0.9,1.0]
y20=[65117,80988,84675]
ax3.plot(x20, y20, marker='o', linestyle='', color='b', label=r'$\alpha_c$=2.0')
m, q = np.polyfit(x20, y20, 1)
y = m*x+ q 
ax3.plot(x,y, color='b')

x21=[0.9,1.0]
y21=[90145,99570]
ax3.plot(x21, y21, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.1')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax3.plot(x,y, color='y')

x22=[0.9,1.0]
y22=[86670,101972]
ax3.plot(x22, y22, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.2')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax3.plot(x,y, color='r')


ax3.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax3.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax3.set_title('')  # Titolo del grafico
ax3.legend()  # Mostra la legenda
ax3.grid(True)  # Attiva la griglia

ax3.axhline(y=93715, color='black', linestyle='--')

x20=[0.8,0.9,1.0]
y20=[83.4484,68.26,70.9091]
ax4.plot(x20, y20, marker='o', linestyle='', color='b', label=r'$\alpha_c$=2.0')
m, q = np.polyfit(x20, y20, 1)
y = m*x+ q 
ax4.plot(x,y, color='b')

x21=[0.9,1.0]
y21=[55.0,54.4424]
ax4.plot(x21, y21, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.1')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax4.plot(x,y, color='y')

x22=[0.9,1.0]
y22=[51.4308,46.7391]
ax4.plot(x22, y22, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.2')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax4.plot(x,y, color='r')

ax4.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax4.set_ylabel('f (Hz)')  # Etichetta asse y
ax4.set_title('')  # Titolo del grafico
ax4.legend()  # Mostra la legenda
ax4.grid(True)  # Attiva la griglia

ax4.axhline(y=33.5, color='black', linestyle='--')

# Mostra il grafico
plt.show()