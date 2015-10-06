#!/bin/bash


filename=$1
collectionName=$2

IFS=$'\n'

if [ $# -ne 2 ]
then

	echo "Insufficient number of arguments provided "
	echo " "; echo " "; 
	echo "to run the script do loopOverAllFiles <yourfile> <Track>"
	
	echo "Track is the collection you want to look for in the dataset"
	exit 1
fi


counter=0
for next in `cat $filename`
do
	let counter=counter+1
	echo "file count: $counter"
	echo "now running edmDumpEvent Content for file : ${next}"
# 	edmDumpEventContent root://xrootd-cms.infn.it/${next} | grep -i TrackCollection
 	edmDumpEventContent ${next} | grep -i ${collectionName}
	echo " "; echo " "; 

	
done
exit 0
