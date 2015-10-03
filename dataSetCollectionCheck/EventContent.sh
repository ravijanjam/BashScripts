#!/bin/bash


if [ $# -ne 1 ]
then 
	echo "Please provide an argument with the command"
	echo "To run the command, do \" EventContent.sh Track\""
	echo "This will check for the collection in all the datasets MinBias, PAHighPt and PromptReco"
	exit 1

fi

next=(/store/hidata/HIRun2013/PAMinBiasUPC/RECO/28Sep2013-v1/10000/001397FC-462D-E311-A034-782BCB3BCADD.root \
      /store/hidata/HIRun2013/PAHighPt/RECO/28Sep2013-v1/10000/0006E29D-F02B-E311-8A9D-003048CB7A80.root \
      /store/hidata/HIRun2013/PAHighPt/RECO/PromptReco-v1/000/209/846/00000/ECAC9C4B-095F-E211-9B60-00237DDBE0E2.root \
      /store/hidata/HIRun2013/PAMinBiasUPC/RECO/PromptReco-v1/000/209/846/00000/800F8DAF-095F-E211-829B-001D09F24763.root \
      /store/himc/Fall10/Hydjet_Bass_MinBias_2760GeV/GEN-SIM-RECODEBUG/START39_V7HI-v1/0002/46B060AD-C9FA-DF11-B18A-485B3919F121.root 
      /store/user/davidlw/PPMinBias/PP2013_FlowCorr_PromptReco_MB_Gplus_v2/e1306249b702130f95e9f12ead4695ee/pp_MB_100_1_HW4.root  
      )


echo "You are looking for the collection named : " $1

for next in ${next[*]}
do
	let counter=counter+1
	echo "file count: $counter"
	echo "now running edmDumpEvent Content for file : ${next}"
# 	edmDumpEventContent root://xrootd-cms.infn.it/${next} | grep -i $1
 	edmDumpEventContent ${next} | grep -i $1
	echo " "; echo " "; 

	
done
exit 0
