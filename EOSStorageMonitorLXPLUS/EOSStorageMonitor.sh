#!/bin/bash

echo `date`  
echo "EOS Heavy Ion Information"  

echo "============================================="  
echo "Submitted from the host", `hostname`
echo "============================================="  

echo "The current EOS directories in /store/hidata"

EOSPATH=/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select

source $EOSPATH \
       ls -ltrh /store/hidata  


echo ; echo ;
echo "=================================================="
source $EOSPATH \
	quota 

<<comment
Rev 1 : This script reads the eos directory from lxplus and writes to a text file which 
shows up in the web page here 
 https://rjanjam.web.cern.ch/rjanjam/EOSStorageMonitor.txt

A cron job is called submitted via acron command. 
For more information on how to run cron job at lxplus look up here 
https://twiki.cern.ch/twiki/bin/view/CMS/CronJobLxplus
comment
