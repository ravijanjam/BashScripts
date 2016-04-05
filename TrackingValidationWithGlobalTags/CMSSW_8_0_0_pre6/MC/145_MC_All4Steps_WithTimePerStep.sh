#!/bin/bash

globalTag=auto:run2_mc_HIon
nEvents=1
echo -e "Running the 4 steps with the information : " Global Tag- ${globalTag}, "\t Number of Events-" ${nEvents}

STARTTIME=$(date +%s)
startTime=$(date +%s)
echo "Running step 1"
cmsDriver.py Hydjet_Quenched_MinBias_5020GeV_cfi  --conditions auto:run2_mc_HIon --scenario HeavyIons -n ${nEvents} --era Run2_HI --eventcontent RAWSIM --relval 2000,1 -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --fileout file:step1.root  > step1_HydjetQ_MinBias_5020GeV+HydjetQ_MinBias_5020GeV+DIGIHI+RECOHI+HARVESTHI.log  2>&1
endTime=$(date +%s)
timeDiff=$(( $endTime - $startTime ))
echo -e "It took $timeDiff seconds to run step 1\n\n"
  

startTime=$(date +%s)
echo "Running step 2"
  cmsDriver.py step2  --conditions ${globalTag} --scenario HeavyIons -n ${nEvents} --era Run2_HI --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --beamspot NominalHICollision2015 --filein file:step1.root  --fileout file:step2.root  > step2_HydjetQ_MinBias_5020GeV+HydjetQ_MinBias_5020GeV+DIGIHI+RECOHI+HARVESTHI.log  2>&1
endTime=$(date +%s)
timeDiff=$(( $endTime - $startTime ))
echo -e "It took $timeDiff seconds to run step 2\n\n"
   

startTime=$(date +%s)
echo "Running step 3"
   cmsDriver.py step3  --conditions ${globalTag} -s RAW2DIGI,L1Reco,RECO,VALIDATION,DQM -n ${nEvents} --era Run2_HI --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  --scenario HeavyIons --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --beamspot NominalHICollision2015 --filein file:step2.root  --fileout file:step3.root  > step3_HydjetQ_MinBias_5020GeV+HydjetQ_MinBias_5020GeV+DIGIHI+RECOHI+HARVESTHI.log  2>&1
endTime=$(date +%s)
timeDiff=$(( $endTime - $startTime ))
echo -e "It took $timeDiff seconds to run step 3\n\n"

startTime=$(date +%s)
echo "Running step 4"
    cmsDriver.py step4  --conditions ${globalTag} -s HARVESTING:validationHarvesting+dqmHarvesting -n ${nEvents} --era Run2_HI --scenario HeavyIons --beamspot NominalHICollision2015 --filetype DQM --mc  --filein file:step3_inDQM.root --fileout file:step4.root  > step4_HydjetQ_MinBias_5020GeV+HydjetQ_MinBias_5020GeV+DIGIHI+RECOHI+HARVESTHI.log  2>&1
endTime=$(date +%s)
timeDiff=$(( $endTime - $startTime ))
echo -e "It took $timeDiff seconds to run step 4\n\n"

echo "====================================================================="
echo -e " It took $(( $endTime - $STARTTIME)) seconds to run all the 4 steps"
