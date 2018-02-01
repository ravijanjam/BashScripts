#!/bin/bash

echo "Please provide your PEM password:"
read -s pssd 

export PASSWD=$pssd

rm *.json

## Put the list of datasets here ## 
#./ACCRE_DDM.sh PARun2016C "2016" 2016-09-1 2017-09-1 "Bias10|Bias11"
./ACCRE_DDM.sh Run2015E "HIRun2015" 2016-09-1 2017-09-1 "Run2015"
#./ACCRE_DDM.sh HIRun2015 "2015" 2016-09-1 2017-09-1 "Onia"
#./ACCRE_DDM_dev.sh HIRun2013 "2013" 2016-09-1 2018-03-1 "28Sep2013"
./ACCRE_DDM.sh HIRun2013 "HI2013" 2016-09-1 2018-03-1 "2013"
#./ACCRE_DDM.sh HIRun2016 "HI2016" 2016-09-1 2018-03-1 "PARun2016C" 


# List of json files
jfiles=`ls Info_*.json | sed -n 's/\(\w\+.json\)/"\1",/p' | tr "\n" "\t" | sed 's/,\s\{0,\}$//g'`
echo $jfiles

cp `pwd`/CMSHIDynamicDataManagement_Template.html `pwd`/CMSHIDynamicDataManagement.html

sed -i "s/dataSetList/$jfiles/g" `pwd`/CMSHIDynamicDataManagement.html

rm DataSetInfo*.json
