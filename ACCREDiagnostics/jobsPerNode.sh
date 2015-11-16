#!/bin/bash


rm JobsPerNode.csv
echo "Node, Jobs, freeMemory" > JobsPerNode.csv

START=$(date +%s)
echo "This scripts get the number of jobs running per node"
echo "and writes to the file JobsPerNode.csv"
echo "which can be found in the same directory"

nodeCount=`cat /usr/local/etc/x86.nodes | wc -l `

zeroJobs=0
for i in `cat /usr/local/etc/x86.nodes` 
do 
		nodeSearch=`squeue | grep $i | wc -l`
		freeMemory=`rsh $i free -m -g | awk 'FNR == 2 {print $3}'`
		echo $i, ${nodeSearch},  ${freeMemory} >> JobsPerNode.csv
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


