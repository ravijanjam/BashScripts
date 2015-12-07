#!/bin/bash

dasQuery=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/cms/das_client/v02.05.00-flmnjk/bin/das_client.py 


$dasQuery --query="dataset run=263005" --limit=0 | grep -v -i superbunnies | grep -E -i '(minimumbias2|hardprobes)'

echo "Runs 263261 Prompt Reco released for HIHardProbes, MinimumBias3, MinimumBias4 "
$dasQuery --query="run dataset=/HIHardProbes/HIRun2015-PromptReco-v1/AOD" --limit=0 | grep -E 263261
$dasQuery --query="run dataset=/HIMinimumBias3/HIRun2015-PromptReco-v1/AOD" --limit=0 | grep -E 263261
$dasQuery --query="run dataset=/HIMinimumBias4/HIRun2015-PromptReco-v1/AOD" --limit=0 | grep -E 263261

echo "Runs 253005 Prompt Reco release status for HIHardProbes, HIMinimumBias2"
$dasQuery --query="run dataset=/HIHardProbes/HIRun2015-PromptReco-v1/AOD" --limit=0 | grep -E 263005
$dasQuery --query="run dataset=/HIMinimumBias2/HIRun2015-PromptReco-v1/AOD" --limit=0 | grep -E 263005


echo " \
263261 HIMinimumBias3, HIMinimumBias4, HIHardProbes \
263005 HIMinimumBias2, HIHardProbes \
"


