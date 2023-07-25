if __name__ == '__main__':
    import sys
    import os
    import numpy as np
    #---
    lnums = [ 35, 101   ]
    string=open('simulations.py').readlines() #--- python script
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

         }

    #--- 
    count = 0
    for key_age in Age:
            #---	
            #---	densities
                inums = lnums[ 0 ] - 1
                string[ inums ] = "\t7:\'shear/glassCo5Cr2Fe40Mn27Ni26/age%s\',\n"%(key_age) #--- change job name
            #---
                inums = lnums[ 1 ] - 1
                string[ inums ] = "\t\'p3\':\' traj.dump 100 %s data_aged.dat\',\n"%(key_age)
            #---

                sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
                os.system( 'python junk%s.py'%count )
                os.system( 'rm junk%s.py'%count )
                count += 1
