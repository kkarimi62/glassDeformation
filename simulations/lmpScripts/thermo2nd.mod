#--- output thermodynamic variables
variable varStep equal step
#variable varPress equal press
variable varTemp equal temp
variable varTime equal v_varStep*${dt}
#variable varXy	 equal	xy
#variable varLy	 equal	ly
variable varVol	 equal	vol
#variable varPe	 equal	pe
#variable varPxx	 equal	pxx
#variable varPyy	 equal	pyy
#variable varPzz	 equal	pzz
#variable varPxy	 equal	pxy
#variable varSxy	 equal	-v_varPxy*${cfac}
#variable varSzz	 equal	-v_varPzz*${cfac}
#variable varExy	 equal	v_varXy/v_varLy		
#variable varEzz	 equal	v_varTime*${GammaDot}		
variable ntherm  equal	10 #ceil(${Nstep}/${nthermo})
variable varn	 equal	v_ntherm

#-----------------
#--- fix swap
#-----------------
#if "${varStep} == 0" then &
#	"variable    swap_attempt equal 0" &
#	"variable    swap_accept  equal 0"
#variable 	stop	equal	${ntype}-1
##
#label       outer
#variable 	itype 	loop 	${stop}
#label       inner
#variable 	start	equal	${itype}+1
#variable	jtype	loop	${start} ${ntype}
#variable	count	equal   (${itype}-1)*${ntype}+${jtype}	
#variable    swap_attempt equal ${swap_attempt}+f_${count}[1]
#variable    swap_accept  equal ${swap_accept}+f_${count}[2]
#next 		jtype
#jump        ${INC}/thermo2nd.mod		inner
#label       break
#next		itype
#jump        ${INC}/thermo2nd.mod		outer
#label       break
variable    swap_attempt equal f_2[1]+f_3[1]+f_4[1]+f_5[1]+f_8[1]+f_9[1]+f_10[1]+f_14[1]+f_15[1]+f_20[1]
variable    swap_accept  equal f_2[2]+f_3[2]+f_4[2]+f_5[2]+f_8[2]+f_9[2]+f_10[2]+f_14[2]+f_15[2]+f_20[2]


#-----------------------------
#--- compute & dump variables
variable 	   var_swap_attempt equal v_swap_attempt
variable 	   var_swap_accept  equal v_swap_accept
#compute thermo_temp0 bulk temp
#variable varTemp equal c_thermo_temp0



fix extra all print ${varn} "${varStep} ${varTime} ${varTemp} ${varVol} ${var_swap_accept} ${var_swap_attempt}" screen no title "step time temp vol swap_accept swap_attempt" file ${thermoFile}

thermo 100
thermo_style custom step temp pe press vol v_swap_accept v_swap_attempt
thermo_modify norm no

