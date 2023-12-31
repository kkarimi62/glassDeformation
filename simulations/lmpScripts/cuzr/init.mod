# NOTE: This script can be modified for different atomic structures, 
# units, etc. See in.elastic for more info.
#

# Define the finite deformation size. Try several values of this
# variable to verify that results do not depend on it.
variable up equal 1.0e-6
 
# Define the amount of random jiggle for atoms
# This prevents atoms from staying on saddle points
variable atomjiggle equal 1.0e-5

# Uncomment one of these blocks, depending on what units
# you are using in LAMMPS and for output

# metal units, elastic constants in eV/A^3
#units		metal
#variable cfac equal 6.2414e-7
#variable cunits string eV/A^3

# metal units, elastic constants in GPa
units		metal
atom_style      atomic
variable cfac equal 1.0e-4
variable cunits string GPa

# real units, elastic constants in GPa
#units		real
#variable cfac equal 1.01325e-4
#variable cunits string GPa

# Define minimization parameters
variable etol equal 0.0 
variable ftol equal 1.0e-03 #1.0e-08
variable maxiter equal 100000
variable maxeval equal 100000
variable dmax equal 1.0e-2

#--- 
boundary    	p p p
#---


#--- discretization time
variable            dt        equal     0.005         # Time step

#--- thermostat parameters
variable            damp_t    equal     100*${dt}     # Thermostat damping
variable            damp_p    equal     1000*${dt}    # Barostat damping

#--- thermal treatment
variable TdotMelt 	equal 50.0   #--- melting rate
variable Tinit 	equal ${tstart}  #--- init temperature
variable Tfinal equal ${tstop}  #--- final temperature
variable TdotQuench equal 0.002*${TdotMelt}   #--- quench rate
variable Pinit	equal 1.0132  #--- number of time steps
variable tEquilibrate	equal 100*${damp_t}  #--- equilibration time

