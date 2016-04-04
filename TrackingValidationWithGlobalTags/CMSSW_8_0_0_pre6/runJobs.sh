#!/bin/bash

eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/r/rjanjam/TrackStuff/CMSSW_8_0_0_pre6/src/140.53_RunHI2011+RunHI2011+RECOHID11+HARVESTDHI 

filepath=`pwd`

echo "Running over the global tag: " $1

echo $filepath

cmsDriver.py test \
	--conditions $1 \
	-s RAW2DIGI,L1Reco,RECO,ALCA:SiStripCalZeroBias+SiStripCalMinBias+TkAlMinBiasHI+TkAlUpsilonMuMuHI+TkAlZMuMuHI+TkAlMuonIsolatedHI+TkAlJpsiMuMuHI+HcalCalMinBias,DQM \
	--process reRECO \
	-n 1000 \
	--data \
	--eventcontent RECO,DQM \
	--runUnscheduled \
	--scenario HeavyIons \
	--datatier RECO,DQMIO \
	--repacked \
	--filein filelist:step1_dasquery.log \
	--lumiToProcess step1_lumiRanges.log \
	--fileout file:step2_pre1_$1_1000Events.root
