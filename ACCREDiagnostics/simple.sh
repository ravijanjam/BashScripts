#!/bin/bash

info=$(hostname; date)

for i in `cat /usr/local/etc/x86.nodes`; do rsh ${i} echo "from" $info >> /home/janjamrk/ACCREDiagnostics/crontest.out; done


