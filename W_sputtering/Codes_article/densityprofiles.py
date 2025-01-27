import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['black'])

user='vzotta'
pulse=96745
sequenza=1044

ppf.ppfgo()

dt=40

densBe = ppf.ppfdata(pulse, 'JST', 'NIMP2', seq=sequenza, uid=user)[0]
densBe_t = ppf.ppfdata(pulse, 'JST', 'NIMP2', seq=sequenza, uid=user)[2]
plt.plot(densBe_t, densBe)
plt.show()