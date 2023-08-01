if __name__ == '__main__':
    import sys
    import os
    import numpy as np
    #---
    lnums = [ 39, 48   ]
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
         }

    #--- 
    count = 0
    for key_age in Age:
            #---	
            #---	densities
                inums = lnums[ 0 ] - 1
                string[ inums ] = "\t\'8\':\'shear/glassCo5Cr2Fe40Mn27Ni26/age%s\',\n"%(key_age) #--- change job name
            #---
                inums = lnums[ 1 ] - 1
                string[ inums ] = "\t\'8\':\'/../simulations/shear/glassCo5Cr2Fe40Mn27Ni26/age%s\',\n"%(key_age) #--- change job name
            #---
                sfile=open('junk%s.py'%count,'w');sfile.writelines(string);sfile.close()
                os.system( 'python3 junk%s.py'%count )
#                os.system( 'rm junk%s.py'%count )
                count += 1
