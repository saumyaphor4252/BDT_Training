#!/usr/bin/env python

from __future__ import print_function
import os
from ROOT import gROOT, TFile, TChain, TCut

# import models
#import preselections

isDEV=False

# Load configuration
with open("configuration.py") as handle:
    exec handle

samples={}
structure={}
cuts={}

for f in [samplesFile, structureFile, cutsFile]:
    with open(f) as handle:
        exec handle


# Reduce sample files for fast dev
for sampleName, sample in samples.items():
    if sampleName not in ['ggWW','WW','top']:
        samples.pop(sampleName)
        continue

    if isDEV:
        if len(sample['name']) > 2:
            sample['name'] = sample['name'][0:1]
    else :
        sample['name'] = sample['name']

# Define data to be loaded
#with open("./preselections.py") as handle:
#    exec handle

#cut="(({0}) && ({1}))".format(supercut,preselections['ALL'])
#cut="(({0}))".format(preselections['ALL'])
cut="(({0}))".format(supercut)
mvaVariables = [
   'mll',
   'PuppiMET_pt',
   'Alt$(CleanJet_pt[0],0)',
   'Alt$(CleanJet_pt[1],0)',
   'Alt$(CleanJet_eta[0],0)',
   'Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]],-2)',
   'Alt$(CleanJet_eta[1],0)',
   'mT2',
   'mjj',
   'pt1',
   'pt2',
   'mth',
   'dphilmet',
   'dphilmet1',
   'mtw1',
   'mtw2',
   'dphijet1met',  
   'dphilljet',
   'mindetajl',
   'detajj',
   'dphijj',
   'pTWW', 
   'njet'
]

