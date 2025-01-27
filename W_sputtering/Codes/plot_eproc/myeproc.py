import matplotlib.pyplot as plt
import eproc as ep
from jetto_tools.binary import *
from scipy import signal 
plt.rcParams['lines.linewidth'] = 1.0
dt=40
tmin=47.9-dt
tmax=50.0-dt
tstart=48.0-dt
tstop=49.986-dt

dato=input("Inserisci il dato: ")
titley=input("inserisci nome asse y: ")



trand='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep2423/seq#6/tran'
trandt='/home/jnv7243/cmg/catalog/edge2d/jet/96745/oct0223/seq#4/tran'
trant='/home/jnv7243/cmg/catalog/edge2d/jet/96745/sep1523/seq#3/tran'

if dato=="YLDT_2":

    moltd=ep.time(trand, 'GAMIT')
    myd=np.array(moltd.yData)

    resultd=ep.time(trand, dato)
    td=np.array(resultd.xData)-dt
    yd=np.array(resultd.yData)

    moltt=ep.time(trant, 'GAMIT')
    myt=np.array(moltt.yData)

    resultt=ep.time(trant, dato)
    tt=np.array(resultt.xData)-dt
    yt=np.array(resultt.yData)

    moltdt=ep.time(trandt, 'GAMIT')
    mydt=np.array(moltdt.yData)

    resultdt=ep.time(trandt, dato)
    tdt=np.array(resultdt.xData)-dt
    ydt=np.array(resultdt.yData)


    plt.plot(td,-yd*myd, color='blue', label='D')
    plt.plot(tdt,-ydt*mydt, color='orange', label='DT (n.s.)')
    plt.plot(tt,-yt*myt, color='magenta', label='T')
    plt.xlabel("time (s)")
    plt.ylabel(titley)

    plt.legend()

    plt.show()

else:

    resultd=ep.time(trand, dato)
    td=np.array(resultd.xData)-dt
    yd=np.array(resultd.yData)

    resultt=ep.time(trant, dato)
    tt=np.array(resultt.xData)-dt
    yt=np.array(resultt.yData)

    resultdt=ep.time(trandt, dato)
    tdt=np.array(resultdt.xData)-dt
    ydt=np.array(resultdt.yData)

    resultdts=ep.time(trandts, dato)
    tdts=np.array(resultdts.xData)-dt
    ydts=np.array(resultdts.yData)

    plt.plot(td,yd, color='blue', label='D')   
    plt.plot(tdt,ydt, color='orange', label='DT (n.s.)')
    plt.plot(tt,yt, color='magenta', label='T')
    plt.xlabel("time (s)")
    plt.ylabel(titley)
    plt.legend()

    plt.show()