import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

fig, ((ax1, ax2), (ax3,ax4))=plt.subplots(nrows=2, ncols=2)
fig.suptitle('D', fontsize=11)

chi=[]
alpha=[]
file_name='/home/jnv7243/TESI/Codes_article/chi_alpha.txt'
with open(file_name) as file:
    line1=file.readline().strip()
    line2=file.readline().strip()
    chi=np.fromstring(line1, sep=' ')
    alpha=np.fromstring(line2, sep=' ')

print(len(chi))
print(chi)
print(len(alpha))
print(alpha)

for i in range(len(chi)):
    file_path='/home/jnv7243/TESI/Codes_article/chi/{}.txt'.format(chi[i])
    print(file_path)
    x=np.loadtxt(file_path, delimiter=' ', usecols=0)
    y=np.loadtxt(file_path, delimiter=' ', usecols=1)
    ax1.plot(x,y,marker='o', label='$\chi_{{ELM}}$={}'.format(chi[i]))

    x=np.loadtxt(file_path, delimiter=' ', usecols=0)
    y=np.loadtxt(file_path, delimiter=' ', usecols=2)
    ax2.plot(x,y,marker='o', label='$\chi_{{ELM}}$={}'.format(chi[i]))

ax1.set_xlabel(r'$\alpha_c (a.u.)$')  
ax1.set_ylabel('f (Hz)')  
ax1.legend()
ax1.axhline(y=38.7, color='black', linestyle='--') #valore di f per #96745
ax1.grid(True)  

ax2.set_xlabel(r'$\alpha_c (a.u.)$')  
ax2.set_ylabel(r'$\overline{\Delta E_p}$ (J)')  
ax2.legend()  
ax2.axhline(y=74609, color='black', linestyle='--') #valore di deltaE per #96745
ax2.grid(True)  

for i in range(len(alpha)):
    file_path='/home/jnv7243/TESI/Codes_article/alpha/{}.txt'.format(alpha[i])
    x=np.loadtxt(file_path, delimiter=' ', usecols=0)
    y=np.loadtxt(file_path, delimiter=' ', usecols=1)
    ax3.plot(x,y,marker='o', label=r'$\alpha_C$={}'.format(alpha[i]))

    x=np.loadtxt(file_path, delimiter=' ', usecols=0)
    y=np.loadtxt(file_path, delimiter=' ', usecols=2)
    ax4.plot(x,y,marker='o', label=r'$\alpha_C$={}'.format(alpha[i]))


ax3.set_xlabel(r'$\chi_{ELM}$')  
ax3.set_ylabel('f (Hz)')
ax3.legend()
ax3.axhline(y=38.7, color='black', linestyle='--') #valore di f per #96745
ax3.grid(True)  

ax4.set_xlabel(r'$\chi_{ELM}$')  
ax4.set_ylabel(r'$\overline{\Delta E_p}$ (J)')   
ax4.legend()  
ax4.axhline(y=74609, color='black', linestyle='--') #valore di deltaE per #96745
ax4.grid(True)  


plt.show()
    