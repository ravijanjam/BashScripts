
#!/bin/bash

echo "The goal of this script is to get the memory information on the node in which cms jobs are running"

nCMSJobs=`sacct -a | grep -w cms |wc -l`
nCMSRunningJobs=`sacct -a | grep -w cms | grep -w  RUNNING |wc -l`
nCMSPendingJobs=`sacct -a | grep -w cms | grep -w  PENDING |wc -l`

echo "The number of CMS jobs as of the moment" ${nCMSJobs}
echo "The number of Running CMS jobs as of the moment" ${nCMSRunningJobs}
echo "The number of Pending CMS jobs as of the moment" ${nCMSPendingJobs}


#<<comment
clear;
query=`sacct -a | grep -w cms | awk '{print $1}'`
for i in ${query}
do
	temp=`scontrol show job $i | grep -iw nodelist`
	echo -ne $i, ${temp}\\r
done
