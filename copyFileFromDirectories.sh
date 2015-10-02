#!/bin/bash

for i in $( ls ); 
	do 
	   echo item: $i;
	   cp $i/*500000* ./; 
   	done


# Script to copy file containing the name 500000 in each of the directory to the current directory
