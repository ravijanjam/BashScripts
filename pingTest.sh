#!/bin/bash

#for i in {1..100};do sleep 0.5; echo $i;done

echo "This script pings the Storage nodes if their visible to the web"

pingServer(){

#	ping se$($1).accre.vanderbilt.edu
	echo "From pingServer" $1 
}

for i in {1..12}
do
	echo "Pinging for 5 secs per SE$i server"
	echo ; echo ; 
	timeout -sHUP 5s ping se$i.accre.vanderbilt.edu
	
#	timeout -sHUP 5s `pingServer i`
	pingServer "functest"
done

:'

This script pings the servers at ACCRE for 5 seconds to check if the servers are connected to the web or not

'


