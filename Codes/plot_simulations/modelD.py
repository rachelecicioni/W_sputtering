import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

fig, ((ax1, ax2), (ax3,ax4))=plt.subplots(nrows=2, ncols=2)
fig.suptitle('D', fontsize=11)

xmin_L=1.8
xmax_L=2.3
x_L= np.linspace(xmin_L, xmax_L, 100)

x5=[2.0,2.2]
y5=[33643,40376]
ax1.plot(x5, y5, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.5$')
m, q = np.polyfit(x5, y5, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='b')

x7=[1.9,2.0,2.1,2.2,2.3]
y7=[52667,58650,65862,70098,76729]
ax1.plot(x7, y7, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=0.7$')
m, q = np.polyfit(x7, y7, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='r')

x8=[1.9,2.0,2.1]
y8=[63176,70817,77854]
ax1.plot(x8, y8, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='y')

x9=[1.9,2.0,2.1]
y9=[74901,80921,87533]
ax1.plot(x9, y9, marker='o', linestyle='', color='aqua', label=r'$\chi_{ELM}=0.9$')
m, q = np.polyfit(x9, y9, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='aqua')

x1=[1.9,2.0,2.1]
y1=[88449,96400,105583]
ax1.plot(x1, y1, marker='o', linestyle='', color='limegreen', label=r'$\chi_{ELM}=1.0$')
m, q = np.polyfit(x1, y1, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='limegreen')

ax1.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax1.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax1.set_title('')  # Titolo del grafico
ax1.legend()  # Mostra la legenda
ax1.grid(True)  # Attiva la griglia

ax1.axhline(y=74609, color='black', linestyle='--')

x5=[2.0,2.2]
y5=[123.1240,88.54]
ax2.plot(x5, y5, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.5$')
m, q = np.polyfit(x5, y5, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='b')

x7=[1.9,2.0,2.1,2.2,2.3]
y7=[105.90,86.72,67.49,50.11,33.7]
ax2.plot(x7, y7, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=0.7$')
m, q = np.polyfit(x7, y7, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='r')

x8=[1.9,2.0,2.1]
y8=[92.97,76.149,61.49]
ax2.plot(x8, y8, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='y')

x9=[1.9,2.0,2.1]
y9=[85.36,69.14,55.92]
ax2.plot(x9, y9, marker='o', linestyle='', color='aqua', label=r'$\chi_{ELM}=0.9$')
m, q = np.polyfit(x9, y9, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='aqua')

x1=[1.9,2.0,2.1]
y1=[69.3588,56.0925,42.9290]
ax2.plot(x1, y1, marker='o', linestyle='', color='limegreen', label=r'$\chi_{ELM}=1.0$')
m, q = np.polyfit(x1, y1, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='limegreen')

ax2.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax2.set_ylabel('f (Hz)')  # Etichetta asse y
ax2.set_title('')  # Titolo del grafico
ax2.legend()  # Mostra la legenda
ax2.grid(True)  # Attiva la griglia

ax2.axhline(y=38.7, color='black', linestyle='--')

xmin=0.5
xmax=1.4
x = np.linspace(xmin, xmax, 100)

x19=[0.7,0.8,0.9]
y19=[52667,63176,74901]
ax3.plot(x19, y19, marker='o', linestyle='', color='b', label=r'$\alpha_c$=1.9')
m, q = np.polyfit(x19, y19, 1)
y = m*x+ q 
ax3.plot(x,y, color='b')

x20=[0.5,0.7,0.8,0.9,1.0]
y20=[33643,58650,70817,80921,88449]
ax3.plot(x20, y20, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.0')
m, q = np.polyfit(x20, y20, 1)
y = m*x+ q 
ax3.plot(x,y, color='r')

x21=[0.7,0.8,0.9,1.0]
y21=[65862,77854,87533,96400]
ax3.plot(x21, y21, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.1')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax3.plot(x,y, color='y')

x22=[0.5,0.7,1.0]
y22=[40376,70098,105583]
ax3.plot(x22, y22, marker='o', linestyle='', color='aqua', label=r'$\alpha_c$=2.2')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax3.plot(x,y, color='aqua')


ax3.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax3.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax3.set_title('')  # Titolo del grafico
ax3.legend()  # Mostra la legenda
ax3.grid(True)  # Attiva la griglia

ax3.axhline(y=74609, color='black', linestyle='--')

x19=[0.7,0.8,0.9]
y19=[105.90,92.97,85.36]
ax4.plot(x19, y19, marker='o', linestyle='', color='b', label=r'$\alpha_c$=1.9')
m, q = np.polyfit(x19, y19, 1)
y = m*x+ q 
ax4.plot(x,y, color='b')

x20=[0.5,0.7,0.8,0.9,1.0]
y20=[123.1240,86.72,76.149,69.14,69.3588]
ax4.plot(x20, y20, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.0')
m, q = np.polyfit(x20, y20, 1)
y = m*x+ q 
ax4.plot(x,y, color='r')

x21=[0.7,0.8,0.9,1.0]
y21=[67.49,61.49,55.92,56.0925]
ax4.plot(x21, y21, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.1')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax4.plot(x,y, color='y')

x22=[0.5,0.7,1.0]
y22=[88.54,50.11,42.9290]
ax4.plot(x22, y22, marker='o', linestyle='', color='aqua', label=r'$\alpha_c$=2.2')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax4.plot(x,y, color='aqua')

ax4.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax4.set_ylabel('f (Hz)')  # Etichetta asse y
ax4.set_title('')  # Titolo del grafico
ax4.legend()  # Mostra la legenda
ax4.grid(True)  # Attiva la griglia

ax4.axhline(y=38.7, color='black', linestyle='--')

# Mostra il grafico
plt.show()