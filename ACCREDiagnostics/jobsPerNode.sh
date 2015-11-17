#!/bin/bash


rm JobsPerNode.csv
echo "Node, Jobs, freeMemory" > JobsPerNode.csv

START=$(date +%s)
echo "========================================================================"
echo "This script gets the number of jobs running per node, free memory and Node information "
echo "and writes to the file JobsPerNode.csv"
echo "which can be found in the same directory"
echo ;
echo "The script takes about ~3min to run, go grab a coffee"
echo "or run in the background, as it has to query all the nodes"
echo "========================================================================"

nodeCount=`cat /usr/local/etc/x86.nodes | wc -l `

zeroJobs=0
echo "Started at `date`"
echo "Running .... please wait"
for i in `cat /usr/local/etc/x86.nodes` 
do 
		nodeSearch=`squeue | grep $i | wc -l`
		freeMemory=`rsh $i free -m -g | awk 'FNR == 2 {print $3}'`
		echo $i, ${nodeSearch},  ${freeMemory} >> JobsPerNode.csv
		echo -n .
		if [ ${nodeSearch} -eq 0 ]; then

			let zeroJobs=zeroJobs+1
			echo $i, >> temp

		fi 
done

END=$(date +%s)
DIFF=$(( $END - $START ))

echo "It took ${DIFF} seconds to run this script"
echo "to loop over ${nodeCount} nodes"
echo "Nodes with NO Jobs on them ${zeroJobs}"
echo "the list of idle nodes are ", `cat temp`
rm temp


:'

To Do :
P | (01) Count all the nodes that are not reachable, this can be
      problem when plotting, so exclude them in the JobsPerNode list
      based on the error i.e. add a condition in the if statement

'
