#!/bin/bash

dasQuery=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/cms/das_client/v02.05.00-flmnjk/bin/das_client.py

ds=(
/ppForward/Run2015E-PromptReco-v1/AOD \
/SingleMuHighPt/Run2015E-ZMM-PromptReco-v1/RAW-RECO \
/MuPlusX/Run2015E-PromptReco-v1/AOD \
/MinimumBias1/Run2015E-PromptReco-v1/AOD \
/JetHT/Run2015E-PromptReco-v1/RECO \
/JetHT/Run2015E-PromptReco-v1/AOD \
/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM \
/Hydjet_Quenched_MinBias_5020GeV/StoreResults-HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI_RAW_6da45e4e90741bc03dbd9aec5f36c050-v1/USER \
/HighPtPhoton30AndZ/Run2015E-PromptReco-v1/RECO \
/HighPtPhoton30AndZ/Run2015E-PromptReco-v1/AOD \
/HighPtLowerPhotons/Run2015E-PromptReco-v1/AOD \
/HighPtLowerJets/Run2015E-PromptReco-v1/AOD \
/HighPtJet80/Run2015E-PromptReco-v1/RECO \
/HighPtJet80/Run2015E-PromptReco-v1/AOD \
/HighPtJet80/Run2015E-HighPtJet-PromptReco-v1/RAW-RECO \
/HighMultiplicity/Run2015E-PromptReco-v1/AOD \
/HIPhoton40AndZ/HIRun2015-ZEE-PromptReco-v1/AOD \
/HIPhoton40AndZ/HIRun2015-Photon-PromptReco-v1/AOD \
/HIOniaTnP/Run2015E-PromptReco-v1/AOD \
/HIOniaPeripheral30100/HIRun2015-OniaPeripheral-PromptReco-v1/RECO \
/HIOniaCentral30L2L3/HIRun2015-OniaCentral-PromptReco-v1/RECO \
/HIOnia/Run2015E-PromptReco-v1/AOD \
/HIHardProbes/HIRun2015-SingleTrack-PromptReco-v1/AOD \
/HIHardProbes/HIRun2015-HighPtJet-PromptReco-v1/RAW-RECO \
/HIHardProbes/HIRun2015-D0Meson-PromptReco-v1/RECO \
/HIHardProbes/HIRun2015-BJet-PromptReco-v1/AOD \
/HIForward/HIRun2015-PromptReco-v1/AOD \
/HIForward/HIRun2015-OniaUPC-PromptReco-v1/RAW-RECO \
/HIEWQExo/HIRun2015-ZMM-PromptReco-v1/RAW-RECO \
/FullTrack/Run2015E-PromptReco-v1/AOD \
/DoubleMu/Run2015E-Onia-PromptReco-v1/RECO \
/BTagCSV/Run2015E-PromptReco-v1/AOD
)

for i in ${ds[@]}
do
	echo $i
	echo "===============================================================================" 
	$dasQuery --query="site dataset=$i | grep site.dataset_fraction, site.name" --limit=0
	echo "===============================================================================" 
done

