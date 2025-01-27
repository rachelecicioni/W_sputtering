function elm_frequency, shot, tstart, tend, threshold, delay, plot=plot
; Finds ELM frequency in time interval [tstart,tend] using BeII emission.
; threshold is the relative value of the signal above which an ELM is detected
; delay is the minimum acceptable delay between ELMs
; set iplot=1 if a plot of ELM number versus ELM time is required
;Read BeII signal
 ppfread,shot=shot,dda='EDG7',dtype='BE2H',t=t_E,data=E,ierr=ierr
; ppfread,shot=shot,dda='EDG8',dtype='TBEO',t=t_E,data=E,ierr=ierr
if ierr eq 0 then begin
;Restrict to [tstart,tend]
   E=   E(where(t_E  le tend and t_E  ge tstart))
 t_E= t_E(where(t_E  le tend and t_E  ge tstart))
;Find ELMs
 fracE=threshold & dE=delay
 iELM=where(E-total(E)/n_elements(E) ge max(E-total(E)/n_elements(E))*fracE)
 iELM=iELM(where(iELM-shift(iELM,1) ne 1))
 tELM=t_E(iELM) & tELM=[tELM(0),tELM(where(tELM-shift(tELM,1) ge dE))]
 print,transpose(telm)
;Linear interpolation
 afit=linfit(tELM,findgen(n_elements(tELM))+1,sigma=sigma)
 freq = afit[1]
 print, afit
 err  = 3*sigma[1]
;Plotting to chek if keyword plot is set
  if keyword_set(plot) then begin
   !p.multi = [0,1,2]
   plot,t_E,E,title=string(shot,format='(i6)'),xrange=[tstart,tend],xstyle=1
   for i=0,n_elements(tELM)-1 do oplot,[tELM(i),tELM(i)],[-1e20,1e20],linestyle=2
   plot,tELM,findgen(n_elements(tELM))+1,psym=4,xrange=[tstart,tend],xstyle=1
   oplot,tELM,afit(1)*tELM+afit(0),linestyle=2
   !p.multi = [0,1,1]
   print, tELM
  endif
endif else begin
 freq = -999
 err  =  0
endelse
;Return ELM times
 return, [tELM,FREQ, ERR]
end
