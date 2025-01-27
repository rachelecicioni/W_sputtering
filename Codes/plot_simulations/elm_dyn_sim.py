import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['black'])

pulse = 96745
user='jnv7243'
dt=40

ppf.ppfgo()
fig, (ax1, ax2, ax3, ax4)=plt.subplots(nrows=4, ncols=1, sharex=True)
next_value=0
num_seq=int(input("Quante sequenze vuoi plottare?(#):  "))

if num_seq ==1:

    sequenza=input("Inserisci la sequenza: ")

    wmhd= ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenza, uid=user)[0]
    wmhd_t = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenza, uid=user)[2]-dt
    ax3.plot(wmhd_t, wmhd*1e-6, label=sequenza) #Plasma energy in MJ
    ax3.set_ylabel(r'$E_p(MJ)$')
    

    elm = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=sequenza, uid=user)[0]
    elm_t = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=sequenza, uid=user)[2]-dt
    ax1.plot(elm_t, elm)
    ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$')
    

#----------------------------------------------------------------------------------------------conteggio elms
    qth=(np.max(elm[2:])+np.min(elm[2:]))/2 #treshold value to consider the elm an elm
    qth=qth*0.98 #percentuale per abbassare qth
    print("qth: ", qth)
    print(elm)
    if qth==0: #qth is equal to zero if chi_elm is constant
        qth=np.max(elm)
    tempi=[] #array con i tempi corrispondenti ad un elm
    elms=[] #array con il conteggio degli elms (1,2,3...)
    indici=[] #qui ho gli indici delle liste corrispondenti agli elms
    count=0
    condition_met = False  # Variabile di controllo
    for index, q in enumerate(elm[5:], start=5): #index conta gli indici in elm, q invece ivalori. Lo start è una funzione specifica della funzione enumerate
        if q > qth and not condition_met: #not condition_met significa che condition_met deve essere falsa per fare l'istruzione di if. Questo if viene fatto solo al primo giro
            count = count + 1
            elms.append(count)
            tempi.append(elm_t[index])
            indici.append(index)
            condition_met = True
        if q > qth and elm_t[index]-tempi[count-1]>0.005: #to avoid double conting of the same elm
            count = count + 1 
            elms.append(count)
            tempi.append(elm_t[index])
            indici.append(index)
 #--------------------------------------------------------------------------------------------------------
    print(indici)
    print(wmhd)
    if len(tempi)>1: #if there are more than one elm
        coefficients = np.polyfit(tempi, elms, 1)
        m_r = coefficients[0]  
        q_r = coefficients[1]

        ax2.scatter(tempi, elms, label='count ELMs')
        ax2.set_ylabel('ELMs (a.u.)')

        x_interpolation = np.linspace(min(tempi), max(tempi), 100)
        y_interpolation = m_r * x_interpolation + q_r
        ax2.plot(x_interpolation, y_interpolation, 'r-', label='Retta di interpolazione')

        condizione=False   #calcolo dei drop
        massimi=[]
        minimi=[]
        for i, value in enumerate(indici):
            if i < len(indici)-1:
                next_value=indici[i+1]
                if not condizione:
                    massimi.append(max(wmhd[0:value]))
                    condizione=True
                if condizione:
                    massimi.append(max(wmhd[value:next_value]))  
                    minimi.append(min(wmhd[value:next_value]))
        minimi.append(min(wmhd[next_value:]))

        drop=[]
        dropabs=[]
        for i, value in enumerate(massimi):
            drop.append((massimi[i]-minimi[i])/massimi[i])
            dropabs.append(massimi[i]-minimi[i])
            dropabs[i]=dropabs[i]*1e-6
            print(massimi[i])
            print(minimi[i])
        dropabs=dropabs
        print(dropabs)
        ax4.scatter(tempi,dropabs, label=r'$\Delta E_p (MJ)')
        ax4.set_ylabel(r'$\Delta E_p (MJ)$')
        ax4.set_xlabel('time (s)')
        drop_medio= np.mean(drop)
        dropabs_medio=np.mean(dropabs)
        print(str(sequenza) + "\t f: " + str(m_r) + "\t" + str(q_r) + "\t" + str(drop_medio) + "\t DE(J): " + str(dropabs_medio*1e6))
      
    elif len(tempi)==1: #if there is one elm
        print(str(sequenza) + "\t" + "one elm" + "\t" + "one elms" + "\t" + "one elms")
    else: #if no elm
        print(str(sequenza) + "\t" + "no elms" + "\t" + "no elms" + "\t" + "no elms")
    plt.show()

else:
    sequenze=[]
    #gaps=[]
    for i in range(num_seq):
        elemento=input("Inserisci l'elemento {}: ".format(i+1))
        sequenze.append(elemento)

    for i in range(num_seq):
        wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenze[i], uid=user)
        wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenze[i], uid=user)[0]
        wmhd_t = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenze[i], uid=user)[2]
        ax3.plot(wmhd[2], wmhd[0], label=sequenze[i] )
        ax3.set_ylabel(r'$E_p(MJ)$')
        ax3.legend()

        elm = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=sequenze[i], uid=user)[0]
        elm_t = ppf.ppfdata(pulse, 'JST', 'XEBA',seq=sequenze[i], uid=user)[2]
        ax1.plot(elm_t, elm)
        ax1.set_ylabel(r'$\chi_{ELM} (m^2/s)$')

        tempi=[]
        elms=[]
        count=0
        condition_met = False  # Variabile di controllo
        indici=[]
        for index, q in enumerate(elm[5:], start=5):
            if q > qth and not condition_met:
                count = count + 1
                elms.append(count)
                tempi.append(elm_t[index])
                indici.append(index)
                condition_met = True
            if q > qth and elm_t[index]-tempi[count-1]>0.005:
                count = count + 1
                elms.append(count)
                tempi.append(elm_t[index])
                indici.append(index)

        if len(tempi)>1:
            coefficients = np.polyfit(tempi, elms, 1)
            m_r = coefficients[0]  
            q_r = coefficients[1]

            ax2.scatter(tempi, elms, label='count ELMs')
            ax2.set_ylabel('count ELMs (a.u.)')


            x_interpolation = np.linspace(min(tempi), max(tempi), 100)
            y_interpolation = m_r * x_interpolation + q_r
            ax2.plot(x_interpolation, y_interpolation, 'r-', label='Retta di interpolazione')
        

            condizione=False   #calcolo dei drop
            massimi=[]
            minimi=[]
            for z, value in enumerate(indici):
                if z < len(indici)-1:
                    next_value=indici[z+1]
                    if not condizione:
                        massimi.append(max(wmhd[0:value]))
                        condizione=True
                    if condizione:
                        massimi.append(max(wmhd[value:next_value]))  
                        minimi.append(min(wmhd[value:next_value]))
            minimi.append(min(wmhd[next_value:]))

            drop=[]
            dropabs=[]
            for w, value in enumerate(massimi):
                drop.append((massimi[w]-minimi[w])/massimi[w])
                dropabs.append(massimi[w]-minimi[w])
            ax4.scatter(tempi,dropabs, label=r'$\Delta E_p (J)')
            ax4.set_ylabel(r'$\Delta E_p abs (J)$')
            ax4.set_xlabel('time (s)')
            drop_medio= np.mean(drop)   
            dropabs_medio=np.mean(dropabs)     
            print(str(sequenze[i]) + "\t f: " + str(m_r) + "\t" + str(q_r) + "\t" + str(drop_medio) + "\t DE (J): " + str(dropabs_medio*1e6))
                  
        elif len(tempi)==1:
            print(str(sequenze[i]) + "\t" + "one elm" + "\t" + "one elms" + "\t" + "one elms")
        else:
            print(str(sequenze[i]) + "\t" + "no elms" + "\t" + "no elms" + "\t" + "no elms")

    plt.show()






