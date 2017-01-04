#!/bin/bash

begin=5
end=75

diff=$(( $end- $begin ))

echo $begin, $end, $diff

for i in $( eval echo {$begin..$end})
do

	echo $i
done

