#!/bin/bash

if [ $# == 1 ]
then 
grep "TimeModule>" $1 > temp

echo "==== Time Per Module ===="
./TimePerModule -n temp
echo "========================"

else 
	echo "================================================="
	echo "This script will estimate the Time Per Module,"
	echo "based on the output log file produced from cmsRun"
	echo "================================================="
	echo ; echo ; echo ;
	echo "To run this script "
	echo "=================================================="
	echo "./PbPb2015TimingStudy.sh <LogFileWithTimingInfo> "
	echo "=================================================="
fi 

