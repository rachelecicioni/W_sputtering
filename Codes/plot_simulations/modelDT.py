import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

fig, ((ax1, ax2), (ax3,ax4))=plt.subplots(nrows=2, ncols=2)
fig.suptitle('DT', fontsize=11)

xmin_L=1.9
xmax_L=2.7
x_L= np.linspace(xmin_L, xmax_L, 100)

x4=[2.1,2.2,2.3,2.4]
y4=[21246,25282,32806,35123]
ax1.plot(x4, y4, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.4$')
m, q = np.polyfit(x4, y4, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='b')

x5=[2.1,2.2,2.3,2.4]
y5=[32337,35661,44880,45157]
ax1.plot(x5, y5, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.5$')
m, q = np.polyfit(x5, y5, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='y')

x6=[2.2,2.3,2.4]
y6=[52545,57930,62630]
ax1.plot(x6, y6, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=0.6$')
m, q = np.polyfit(x6, y6, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='r')

x7=[2.0,2.1,2.2,2.3]
y7=[52441,62623,65283,64050]
ax1.plot(x7, y7, marker='o', linestyle='', color='aqua', label=r'$\chi_{ELM}=0.7$')
m, q = np.polyfit(x7, y7, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='aqua')

x8=[2.2,2.3,2.4]
y8=[82916,88076,99287]
ax1.plot(x8, y8, marker='o', linestyle='', color='limegreen', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax1.plot(x_L,y, color='limegreen')

ax1.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax1.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax1.set_title('')  # Titolo del grafico
ax1.legend()  # Mostra la legenda
ax1.grid(True)  # Attiva la griglia

ax1.axhline(y=64042, color='black', linestyle='--')

x4=[2.1,2.2,2.3,2.4]
y4=[121.33,105.9,87.65,75.56]
ax2.plot(x4, y4, marker='o', linestyle='', color='b', label=r'$\chi_{ELM}=0.4$')
m, q = np.polyfit(x4, y4, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='b')

x5=[2.1,2.2,2.3,2.4]
y5=[103.228,79.105,65.5,57.549]
ax2.plot(x5, y5, marker='o', linestyle='', color='y', label=r'$\chi_{ELM}=0.5$')
m, q = np.polyfit(x5, y5, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='y')

x6=[2.2,2.3,2.4]
y6=[61.6,54.3803,50.3811]
ax2.plot(x6, y6, marker='o', linestyle='', color='r', label=r'$\chi_{ELM}=0.6$')
m, q = np.polyfit(x6, y6, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='r')

x7=[2.0,2.1,2.2,2.3]
y7=[85.8898,76.34,57.17,60.2650]
ax2.plot(x7, y7, marker='o', linestyle='', color='aqua', label=r'$\chi_{ELM}=0.7$')
m, q = np.polyfit(x7, y7, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='aqua')

x8=[2.2,2.3,2.4]
y8=[49.69,42.25,34]
ax2.plot(x8, y8, marker='o', linestyle='', color='limegreen', label=r'$\chi_{ELM}=0.8$')
m, q = np.polyfit(x8, y8, 1)
y = m*x_L+ q 
ax2.plot(x_L,y, color='limegreen')

ax2.set_xlabel(r'$\alpha_c (a.u.)$')  # Etichetta asse x
ax2.set_ylabel('f (Hz)')  # Etichetta asse y
ax2.set_title('')  # Titolo del grafico
ax2.legend()  # Mostra la legenda
ax2.grid(True)  # Attiva la griglia

ax2.axhline(y=35.2, color='black', linestyle='--')

xmin=0.3
xmax=1.1
x = np.linspace(xmin, xmax, 100)

x21=[0.4,0.5,0.7]
y21=[21246,32337,62623]
ax3.plot(x21, y21, marker='o', linestyle='', color='b', label=r'$\alpha_c$=2.1$')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax3.plot(x,y, color='b')

x22=[0.4,0.5,0.6,0.7,0.8]
y22=[25282,35661,52545,65283,82916]
ax3.plot(x22, y22, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.2$')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax3.plot(x,y, color='r')

x23=[0.4,0.5,0.6,0.7,0.8]
y23=[32806,44880,57930,64050,88076]
ax3.plot(x23, y23, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.3$')
m, q = np.polyfit(x23, y23, 1)
y = m*x+ q 
ax3.plot(x,y, color='y')

x24=[0.4,0.5,0.6,0.8]
y24=[35123,45157,62630,99287]
ax3.plot(x24, y24, marker='o', linestyle='', color='aqua', label=r'$\alpha_c$=2.4$')
m, q = np.polyfit(x24, y24, 1)
y = m*x+ q 
ax3.plot(x,y, color='aqua')

ax3.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax3.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  # Etichetta asse y
ax3.set_title('')  # Titolo del grafico
ax3.legend()  # Mostra la legenda
ax3.grid(True)  # Attiva la griglia

ax3.axhline(y=64042, color='black', linestyle='--')

x21=[0.4,0.5,0.7]
y21=[121.33,103.228,76.34]
ax4.plot(x21, y21, marker='o', linestyle='', color='b', label=r'$\alpha_c$=2.1')
m, q = np.polyfit(x21, y21, 1)
y = m*x+ q 
ax4.plot(x,y, color='b')

x22=[0.4,0.5,0.6,0.7,0.8]
y22=[105.9,79.105,61.6,57.17,49.69]
ax4.plot(x22, y22, marker='o', linestyle='', color='r', label=r'$\alpha_c$=2.2')
m, q = np.polyfit(x22, y22, 1)
y = m*x+ q 
ax4.plot(x,y, color='r')

x23=[0.4,0.5,0.6,0.7,0.8]
y23=[87.65,65.5,54.3803,60.2650,42.25]
ax4.plot(x23, y23, marker='o', linestyle='', color='y', label=r'$\alpha_c$=2.3')
m, q = np.polyfit(x23, y23, 1)
y = m*x+ q 
ax4.plot(x,y, color='y')

x24=[0.4,0.5,0.6,0.8]
y24=[75.56,57.549,50.3811,34]
ax4.plot(x24, y24, marker='o', linestyle='', color='aqua', label=r'$\alpha_c$=2.4')
m, q = np.polyfit(x24, y24, 1)
y = m*x+ q 
ax4.plot(x,y, color='aqua')

ax4.set_xlabel(r'$\chi_{ELM} (m^2/s)$')  # Etichetta asse x
ax4.set_ylabel('f (Hz)')  # Etichetta asse y
ax4.set_title('')  # Titolo del grafico
ax4.legend()  # Mostra la legenda
ax4.grid(True)  # Attiva la griglia

ax4.axhline(y=35.2, color='black', linestyle='--')


# Mostra il grafico
plt.show()