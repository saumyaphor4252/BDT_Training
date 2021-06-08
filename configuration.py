# example of configuration file

import os

configDir = os.path.expandvars("/afs/cern.ch/user/s/ssaumya/Projects/WW_Analysis_Work/WW_Cuts_Optimization/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WW/FullRunII/Cuts_Optimization_ttbar/") #change the path to where following files are

tagName = ''

# luminosity to normalize to (in 1/fb)
lumi = 41.5

# file with list of variables
#variablesFile = os.path.join(configDir,'variables.py')

# file with list of cuts
cutsFile = os.path.join(configDir,'cuts_BDT.py' )

# file with list of samples
samplesFile = os.path.join(configDir,'samples_BDT.py' )

# structure file for datacard
structureFile = os.path.join(configDir,'structure.py')

# file with TTree aliases
#aliasesFile = os.path.join(configDir,'aliases.py')

