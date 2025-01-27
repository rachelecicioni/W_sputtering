import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat
plt.rcParams['lines.linewidth'] = 1.0 
n=25 #font size
n2=20

x=[]
y=[]

xs=[]
ys=[]

isotopo=input("Inserisci isotopo(D/T/DT): ")
user_color = (input("Inserisci il colore(blue/orange/magenta): "))


with open('dAf{}.txt'.format(isotopo), 'r') as file:
    for line in file:
        line = line.strip()  # Rimuovi spazi bianchi iniziali e finali
        if line:  # Assicurati che la linea non sia vuota
            parts = line.split()  # Dividi la linea in parti usando gli spazi come delimitatori
            x.append(float(parts[0]))  # Aggiungi la parte prima come dato di x (convertito in float)
            y.append(float(parts[1]))  # Aggiungi la parte seconda come dato di y (convertito in float)

if isotopo=="DT":
    with open('dAf{}s.txt'.format(isotopo), 'r') as file:
        for line in file:
            line = line.strip()  # Rimuovi spazi bianchi iniziali e finali
            if line:  # Assicurati che la linea non sia vuota
                parts = line.split()  # Dividi la linea in parti usando gli spazi come delimitatori
                xs.append(float(parts[0]))  # Aggiungi la parte prima come dato di x (convertito in float)
                ys.append(float(parts[1]))  # Aggiungi la parte seconda come dato di y (convertito in float)

with open('punto{}.txt'.format(isotopo), 'r') as file:
    for line in file:
        line = line.strip()  # Rimuovi spazi bianchi iniziali e finali
        if line:  # Assicurati che la linea non sia vuota
            parts = line.split()  # Dividi la linea in parti usando gli spazi come delimitatori
            px=(float(parts[0]))  # Aggiungi la parte prima come dato di x (convertito in float)
            py=(float(parts[1]))  # Aggiungi la parte seconda come dato di y (convertito in float)
y=np.array(y)         
y=y*1e-6
ys=np.array(ys)
ys=ys*1e-6
py=np.array(py)
py=py*1e-6
plt.plot(x, y, marker='o', markersize=6, linestyle='', color=user_color, label='Simulated points (n.s.)')  #togliere se  ho DT
#plt.plot(xs, ys, marker='o', markersize=6, linestyle='', color='orangered', label='Simulated points (s.)') #togliere se ho D o  T
plt.plot(px, py, marker='o', markersize=6, linestyle='', color='black', label='Experimental point')
plt.axhline(y=py, color='black', linestyle='--')
plt.axvline(x=px, color='black', linestyle='--')
plt.xlabel('frequency f (Hz)', fontsize=14)  # Etichetta asse x
plt.ylabel(r'size $\overline{\Delta E_p}$ (MJ)', fontsize=14)  # Etichetta asse y
#plt.title('Deuterium+Tritium', color=user_color)  # Titolo del grafico
#plt.xticks(fontsize=n2)
#plt.yticks(fontsize=n2)
plt.xlim(0,200)
plt.ylim(0,0.15)
#plt.legend()  # Mostra la legenda
plt.grid(True)  # Attiva la griglia

# Mostra il grafico
plt.show()