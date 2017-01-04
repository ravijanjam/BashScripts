#!/bin/bash

arr=("a" "b" "c" "d" "e" "f")
arr_size=${#arr[@]}
seq={1..$(( $arr_size-1 ))}
echo "Array Size: " $arr_size 

for i in $( eval echo $seq )
do
	
	low=${arr[$(( i-1 ))]}
	hi=${arr[$(( i ))]}
	echo $hi "to" $low
done
