from backports import configparser
def makeOAR( EXEC_DIR, node, core, tpartitionime, PYFIL, argv):
    #--- parse conf. file
    confParser = configparser.ConfigParser()
    confParser.read('config.ini')
    #--- set parameters
    confParser.set('parameters','itime0','0')
    confParser.set('parameters','itime','2000000')
    confParser.set('input files','path',argv)
    confParser.set('Spline','deg_f','100')
    #
    pylib_directory = os.path.expanduser('~/Project/git/glassDeformation/python')
    confParser.set('python library path','path',pylib_directory)
    #--- write
    confParser.write(open('config.ini','w'))	
    #--- set environment  variables

    someFile = open( 'oarScript.sh', 'w' )
    print('#!/bin/bash\n',file=someFile)
#     print('EXEC_DIR=%s\n module load python/anaconda3-2019.10-tensorflowgpu'%( EXEC_DIR ),file=someFile)
    print('module load python/anaconda3-2018.12\nsource /global/software/anaconda/anaconda3-2018.12/etc/profile.d/conda.sh\nconda activate gnnEnv2nd\n\n',file=someFile)
    if convert_to_py:
        print('ipython3 py_script.py\n',file=someFile)
    else:	 
        print('jupyter nbconvert --execute $EXEC_DIR/%s --to html --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.allow_errors=True;ls output.html'%(PYFIL), file=someFile)
    someFile.close()										  
#
if __name__ == '__main__':
    import os
#
    runs	 = [0] #,1,2] #range(3)
    jobname  = {
                '1':'ElasticityT300/Co5Cr2Fe40Mn27Ni26/itime0', 
                '2':'MlTrain/Co5Cr2Fe40Mn27Ni26/itime0/Angular', 
                '3':'PairCrltnT300/Co5Cr2Fe40Mn27Ni26', 
                '4':'VorAnlT300/Co5Cr2Fe40Mn27Ni26', 
                '5':'D2minAnalysisT300/Co5Cr2Fe40Mn27Ni26', 
                '7':'annealing/glassCo5Cr2Fe40Mn27Ni26', 
                '8':'shear/glassCo5Cr2Fe40Mn27Ni26/age0/itime0', 
                '9':'cxy/glassCo5Cr2Fe40Mn27Ni26/age0/itime0', #'hmodu/glassCo5Cr2Fe40Mn27Ni26/age0/df0', 
                }['9']
    DeleteExistingFolder = True
    readPath = os.getcwd() + {
                                '1':'/../testRuns/Preparation/ElasticityT300/Co5Cr2Fe40Mn27Ni26/itime0',
                                '2':'/../testRuns/glassCo5Cr2Fe40Mn27Ni26',
                                '3':'/../testRuns/Preparation/CuZrNatom32KT300Tdot1E-1Sheared',
                                '4':'/../testRuns/granular/silviaData/DATA_GRAINS/seed1_1001',
                                '7':'/../simulations/annealing/glassCo5Cr2Fe40Mn27Ni26',
                                '8':'/../simulations/shear/glassCo5Cr2Fe40Mn27Ni26/age0',
                            }['8'] #--- source
    EXEC_DIR = '.'     #--- path for executable file
    durtn = '23:59:59'
    mem = '64gb'
    partition = ['parallel','cpu2019','bigmem','single'][2] 
    argv = "%s"%(readPath) #--- don't change! 
    PYFILdic = { 
        0:'ElasticConstants.ipynb',
        1:'analyzePlasticity.ipynb',
        2:'test2nd.ipynb',
        3:'junk.ipynb',
        }
    keyno = 1
    convert_to_py = True
#---
#---
    PYFIL = PYFILdic[ keyno ] 
    #--- update argV
    if convert_to_py:
        os.system('jupyter nbconvert --to script %s --output py_script\n'%PYFIL)
        PYFIL = 'py_script.py'
    #---
    if DeleteExistingFolder:
        os.system( 'rm -rf %s' % jobname ) # --- rm existing
    # --- loop for submitting multiple jobs
    for counter in runs:
        print(' i = %s' % counter)
        writPath = os.getcwd() + '/%s/Run%s' % ( jobname, counter ) # --- curr. dir
        os.system( 'mkdir -p %s' % ( writPath ) ) # --- create folder
#        os.system( 'cp utility.py LammpsPostProcess2nd.py OvitosCna.py %s' % ( writPath ) ) #--- cp python module
        makeOAR( writPath, 1, 1, durtn, PYFIL, argv+"/Run%s"%counter) # --- make oar script
        os.system( 'chmod +x oarScript.sh; mv oarScript.sh %s; cp config.ini %s;cp %s/%s %s' % ( writPath, writPath, EXEC_DIR, PYFIL, writPath ) ) # --- create folder & mv oar scrip & cp executable
        jobname0 = jobname.split('/')[0]
        print(jobname)
        os.system( 'sbatch --partition=%s --mem=%s --time=%s --job-name %s.%s --output %s.%s.out --error %s.%s.err \
                            --chdir %s -c %s -n %s %s/oarScript.sh'\
                           % ( partition, mem, durtn, jobname0, counter, jobname0, counter, jobname0, counter \
                               , writPath, 1, 1, writPath ) ) # --- runs oarScript.sh!


