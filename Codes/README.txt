#plot_pulses

@multiplot.py
Multiplot dei tre spari di riferimento. 
Figura 3.1 tesi.

@multiplot_poster.py
multiplot con corrente di plasma, Paux, ELMs, radiation per il poster.

@singleplot.py
codice di prova durante il lavoro. Simile a multiplot.py

@elm_dyn_exp.py 
Dinamica degli ELMs sperimentali. Inserendo un run sperimentale e il tempo massimo (t2 nella tesi con +40s, 48.36 #96745, 49.27 #99282, 48.52 #99948) dà: ELMs sperimentali, drop di energia, retta frequenza. Nel terminale stampa drop energia relativo, drop energia assoluto, frequenza. Per farlo funzionare è necessario avere nella stessa cartella i files times_(sim).txt che sono i tempi degli ELMs sperimentali mettendo un valore di threshold al segnale bolometrico. 
Figure 3.6,3.7,3.8 tesi.

@elm_times.py
Plotta degli spari sperimentali: ELMs, energia, densità elettronica con t1, t2, tstart, tstop.
Figure 3.3,3.4,3.5 tesi.

----------------------------------------------------------------------------------------------
&trovare i tempi per times
1. dalla cartella in cui si  trova il porgramma elm_frequency.pro scrivi idl (piccolo)
timesel33 = 49.0; rad


2. copia questo codice:
res3check = elm_frequency(99948, (48.0), (50.0), 0.35,2e-3, /plot)
i due tempi sono quelli in cui vuoi calcolare la frequenza, il secondo valore è la percentuale di soglia per considerare un picco un ELM.


3. poi questo:
print,res3check
------------------------------------------------------------------------------------------------

#plot_simulations

@elm_dyn_sim.py
Dinamica degli ELMs simulati. Inserendo il/i numeri  della sequenza delle simulazioni dà: chi_ELM, retta di interpolazione per la frequenza, energia, drop assoluto energia.
Nel terminale stampa: numero sequenza \tab coefficiente angolare della retta (frequenza) \tab termine noto retta \tab drop relativo energia \tab drop assoluto energia.
Figura 3.9 tesi.

@elm_dyn_sim2.py
è la seconda versione in cui lavora con massimi e minimi locali. Versione più accurata.

@modelD.py @modelT.py @modelDT.py
Plot per mostrare il modello ottenuto per conoscere a priori i parametri di scan.

@plot1ns.py @plot2ns.py @plot3ns.py
Plotta chi_ELM, W sputtering source and W flux per i tre isotopi nel caso DT-non segregato.
Plotta contenuto e densità di W DT-non segregato.
Figura 4.2, 4.4, 4.6 tesi.

@plot1s.py @plot2s.py @plot3s.py
Plotta chi_ELM, W sputtering source and W flux per i tre isotopi nel caso DT-segregato con parte evidenziata per le slides + singolo ELM.
Plotta contenuto e densità di W DT- segregato.
Figura 4.1, 4.3, 4.5 tesi. 


-------------------------------------------------------------------------------------------------
#pulses_vs_sim

@dA_f_points.py
In grafici drop_abs vs frequenza mette il punto sperimentale con i punti simulati. 
Figure 3.10,3.11,3.12 tesi.

@simvsdata.py
Plotta un run sperimentale  e una o più simulazioni pr vedere un eventuale match con il dato sperimentale. 
figure 3.14,3.15,3.16,3.17,3.18 tesi.

-------------------------------------------------------------------------------------------------
#plot_slides

@elm_exp_slides.py
Doppio plot: segnale spettroscopico con fase evidenziata; andamento degli ELMs e energia.

@plot2s_slides.py
(vedi plot_2s ma modificato per le slides)

-------------------------------------------------------------------------------------------------
#other

@calcolo_medie.py
calcola il p_medio che serve per la pagina di pencil per NBI.

@elmphase.py
Stampa su terminale i tempi in cui la condizione per la scelta della fase degli ELMs è soddisfatta.

-------------------------------------------------------------------------------------------------
#plot_eproc

@myeproc.py
Plotta il dato di output di edge2d inserito da terminale.

@myeproc_menu.py
Plotta il dato di output di edge2d inserito da terminale con menu per inserire anche la sequenza di interesse confrontandolo per i tre isotopi.

@noimp.py
confronta gli spari con solo W e W+Be





