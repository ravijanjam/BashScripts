#!/bin/bash


# Get the data sets via CERN DAS
getDASDataSets(){

		echo "Getting the CERN DAS Data Sets"
	        srchStr=$1
	        year=`sed 's/[a-zA-Z]\+//g' <<< $srchStr`

		dList=`das_client --query="dataset site=T2_US_Vanderbilt*" --limit=0 --format=plain | grep "$srchStr"`

		echo $dList

		`ls temp.json &> /dev/null; if [ $? != 0 ]; then echo "found it"; rm temp.json; fi`
	
		echo "Reading dataset information from CERN DAS for the label: "$srchStr
		for ds in ${dList[@]}
		do
			dsSize=`das_client --query="dataset=$ds | grep dataset.size" --limit=0 --format=plain` 
			echo \"$ds\":$dsSize >> temp.json
			
		done
		cat temp.json | tr "\n" "," | sed 's/^/{/g' | sed 's/,$/}/g' > DataSetInfo_${2}.json
		export dasDataSet=DataSetInfo_${2}.json
		cat DataSetInfo_${2}.json
		echo "dataset", ${dasDataSet}
		rm temp.json
}



# Get the popularity datasetss via Popularity API
getPopularityDataSets(){

	echo "Getting popularity information from the Popularity API, in between $1 and $2"
	startTime=$1
	stopTime=$2
	ulink="https://cmsweb.cern.ch/popdb/popularity/DSStatInTimeWindow/?&tstart=${startTime}&tstop=${stopTime}&sitename=T2_US_Vanderbilt" 
		curl -s --capath ~/.globus/ \
		     -E, --cert ~/.globus/usercert.pem:$PASSWD \
		     --key ~/.globus/userkey.pem ${ulink} 2>/dev/null > DSStatInTimeWindow.json 
}


#echo "variables"
#echo $1 $2 $3 $4
#echo $@


clear
echo "Please Wait... Processing ...."
getDASDataSets $1 $2
getPopularityDataSets $3 $4
python processDDM_DSStatInTimeWindow.py "DSStatInTimeWindow" $dasDataSet $5 $2  
