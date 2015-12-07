#!/bin/bash

dasQuery=/cvmfs/cms.cern.ch/slc6_amd64_gcc472/cms/das_client/v02.05.00-flmnjk/bin/das_client.py 


echo "RunNo, dataSetname, events(millions), lumis, size(GB)" > priorityRun.csv

#for RunNo in 262694 262695 262703 262726 262735
for RunNo in 262694
do
dataSetList=`$dasQuery --query="dataset run=$RunNo | grep dataset.name" --limit=0`
#echo "dataSet" $dataSetList
#<<comment
	for dataSet in $dataSetList
	do
	START=$(date +%s)
	#nevents=`$dasQuery --query="dataset dataset=$dataSet | grep dataset.nevents" --limit=0`
	#nlumis=`$dasQuery --query="dataset dataset=$dataSet | grep dataset.nlumis" --limit=0`
	nsize=`$dasQuery --query="dataset dataset=$dataSet | grep dataset.size" --limit=0`

	#nameOfDataSet=`echo $dataSet | sed 's/\/HIRun2015-v1\/RAW//; s/\///'`
	#nsize1=`echo "scale=3; $nsize/1000000000" | bc`
	#nevents1=`echo "scale=3; $nevents/1000000" | bc`
	#nlumis1=`echo "scale=3; $nlumis/10" | bc`
	let nsize+=nsize
	#echo -e $RunNo,$nameOfDataSet,$nevents1, $nlumis, $nsize1 #>> priorityRuns.csv
#stuff=($i $nameOfDataSet $nevents) 
	done
	END=$(date +%s); DIFF=$(( $END - $START ))
	nsize1=`echo $scale=4; $nsize/1048576 | bc`
	echo "Took $DIFF seconds for $RunNo"
	echo "Size of dataset in Run No $RunNo : $nsize1"
#comment
done


