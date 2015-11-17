#!/bin/bash

if [ $# -ne 1 ]
then


START=$(date +%s)
echo "========================================================================"
echo "This script gets the number of jobs running per node, free memory and Node information "
echo "and writes to the file JobsPerNode.csv"
echo "which can be found in the same directory"
echo ;
echo "The script takes about ~3min to run, go grab a coffee"
echo "or run in the background, as it has to query all the nodes"

echo "To run the script, just do the following"
echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
echo "./jobsPerNode.sh s"
echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
echo "========================================================================"

elif [ $1 == 's' ]
then

rm JobsPerNode.csv
echo "Node, Jobs, freeMemory" > JobsPerNode.csv

nodeCount=`cat /usr/local/etc/x86.nodes | wc -l `
zeroJobs=0

clear;
echo "Started at `date`"
echo "Running .... please wait"
echo "===================================================================="
echo "The script takes about ~3min to run, go grab a coffee"
echo "or run in the background, as it has to query ${nodeCount} nodes"
echo "===================================================================="
echo ;

loopCount=1
for i in `cat /usr/local/etc/x86.nodes` 
do 
		nodeSearch=`squeue | grep $i | wc -l`
		freeMemory=`rsh $i free -m -g | awk 'FNR == 2 {print $3}'`
		echo $i, ${nodeSearch},  ${freeMemory} >> JobsPerNode.csv
		echo  "Querying into :" $i. 
		echo  "Completed so far : ${loopCount} "

		tput cuu1 # move up by one line
		tput cuu1 # move up by one line
		#tput el # clear the line

		if [ ${nodeSearch} -eq 0 ]; then

			let zeroJobs=zeroJobs+1
			echo $i, >> temp

		fi 
		let loopCount=loopCount+1
done

END=$(date +%s)
DIFF=$(( $END - $START ))

echo "COMPLETED, please check your local directory for the file"
echo "JobsPerNode.csv"
echo "============================================"
echo "It took ${DIFF} seconds to run this script"
echo "to loop over ${nodeCount} nodes"
echo "Nodes with NO Jobs on them ${zeroJobs}"
echo "the list of idle nodes are ", `cat temp`
echo "============================================"
rm temp
fi

<<comment
To Do :
P | (01) Count all the nodes that are not reachable, this can be
      problem when plotting, so exclude them in the JobsPerNode list
      based on the error i.e. add a condition in the if statement

P | (02) Webpage : Implement the feature where nodes with same number 
         of jobs are highlighted, a csv file generated
comment
