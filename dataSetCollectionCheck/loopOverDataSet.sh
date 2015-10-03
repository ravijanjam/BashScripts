#!/bin/bash

filename=$1
IFS=$'\n'

if [ $# -ne 1 ]
then

	echo "Insufficient number of arguments provided "
	echo "to run the script do loopOverAllFiles yourfile.txt"
	exit 1
fi


counter=0
for next in `cat $filename`
do
	let counter=counter+1
	echo "file count: $counter"
	echo "now running edmDumpEvent Content for file : ${next}"
# 	edmDumpEventContent root://xrootd-cms.infn.it/${next} | grep -i TrackCollection
 	edmDumpEventContent ${next} | grep -i TrackCollection
	echo " "; echo " "; 

	
done
exit 0
