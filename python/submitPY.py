if __name__ == '__main__':
    import sys
    import os
    import numpy as np
    #---
    lnums = [ 41, 50, 8   ]
    glass = 'Co5Cr2Fe40Mn27Ni26 CoNiCrFe CoNiCrFeMn CoNiFe'.split()[3]
    
    
    string=open('python.py').readlines() #--- python script
    Age ={
           0:0,
             1:1,
             2:2,
             3:3,
             4:4,
             5:5,
             6:6,
             7:7,
             8:8,
             9:9,
             10:10,
         }
    
    #--- timestpes
    ndump =100;GammaXY=0.2;dt=1e-3;GammaDot=1.0e-04;
    Nstep=np.floor(GammaXY/dt/GammaDot);Nevery=np.ceil(Nstep/ndump)
    Times = dict(zip(range(ndump+1), np.arange(0,Nstep+Nevery,Nevery,dtype=int)))

    DF={0:128,1:256,2:512}
    
    #--- 
    count = 0
    for key_age in Age:
#          for key_d in DF:
         if 1: #for key_t in Times:
#             if key_t % 2 == 0:
            #---	
            #---	densities
                inums = lnums[ 0 ] - 1
                string[ inums ] = "\t\'10\':\'shear/glass%s/age%s\',\n"%(glass,key_age) #--- change job name
#                string[ inums ] = "\t\'10\':\'cluster/glass%s/age%s/itime%s\',\n"%(glass,key_age,key_t) #--- change job name
            #---
                inums = lnums[ 1 ] - 1
                string[ inums ] = "\t\'8\':\'/../simulations/shear/glass%s/age%s\',\n"%(glass,key_age) #--- change job name
            #---
                inums = lnums[ 2 ] - 1
                string[ inums ] = "    confParser.set(\'parameters\',\'itime\',\'%d\')\n"%(1960000) #Times[key_t]) #--- change job name
#               string[ inums ] = "    confParser.set(\'Spline\',\'deg_f\',\'%d\')\n"%(DF[key_d]) #--- change job name
            #---
                sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
                os.system( 'python3 junk%s.py'%count )
                os.system( 'rm junk%s.py'%count )
                count += 1
