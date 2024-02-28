import os
glass = 'Co5Cr2Fe40Mn27Ni26 CoNiCrFe CoNiCrFeMn CoNiFe'.split()[3]
for age in [0,1,2,3,4,5,9,10]:
	folder='shear/glass%s/age%s/Run2'%(glass,age)
	os.system('mkdir -p %s'%folder)
	os.system('scp arc:~/Project/git/glassDeformation/simulations/%s/thermo-shear.txt %s'%(folder,folder))

