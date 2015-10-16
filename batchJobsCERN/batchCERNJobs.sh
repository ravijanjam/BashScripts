#!/bin/sh

cd /afs/cern.ch/user/initial/username/scratch0/CMSSW_x_y_z/src/.../.../test

cd /afs/cern.ch/user/r/rjanjam/CMSSW_7_5_0_pre5/

eval `scramv1 runtime -sh`
#cmsRun aConfigFile.cfg
echo "Hello World" 


# Submit the job using the command 
# bsub -R "pool > ^C000" -q 1nw -J job1 < yourScript.sh

# Check the status using and get the JobID
# bjobs
