#!/bin/bash	


counter=1

for i in `cat /usr/local/etc/x86.nodes`
	do 
	#rsh ${i} ~/ACCREDiagnostics/hello.sh $i 
	tstamp=$(date +%h%d_%H%M%S)
	echo "Logging into gateway : $i and writing a file 10MB" 
	#rsh ${i} fallocate -l 10M test_${tstamp}.dump 
	#rsh ${i} fallocate -l 1K test.dump 
	date
	rsh ${i} /gpfs22/home/janjamrk/ACCREDiagnostics/hello.sh ${i} \
	     >>	 /gpfs22/home/janjamrk/ACCREDiagnostics/test.sh
	let counter=${counter}+1
	echo ${counter}
	
done
