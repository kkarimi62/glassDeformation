#--- output thermodynamic variables
variable varStep equal step
variable varPress equal press
variable varTemp equal temp
variable varTime equal v_varStep*${dt}
variable varXy	 equal	xy
variable varLy	 equal	ly
variable varVol	 equal	vol
variable varPe	 equal	pe
variable varPxx	 equal	pxx
variable varPyy	 equal	pyy
variable varPzz	 equal	pzz
variable varPxy	 equal	pxy
variable varSxy	 equal	-v_varPxy*${cfac}
variable varSzz	 equal	-v_varPzz*${cfac}
variable varExy	 equal	v_varXy/v_varLy		
variable varEzz	 equal	0.0 #v_varTime*${GammaDot}		
variable ntherm  equal	10 #ceil(${Nstep}/${nthermo})
variable varn	 equal	v_ntherm
fix extra all print ${varn} "${varStep} ${varTime} ${varExy} ${varTemp} ${varPe} ${varPress} ${varSxy} ${varVol}" screen no title "step time exy temp pe press sxy vol" file ${thermoFile}

thermo 100
thermo_style custom step temp pe press xy vol 
thermo_modify norm no

