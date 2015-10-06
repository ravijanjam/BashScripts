#!/bin/bash

echo "To add quotes to each line in the file assuming"

if [ "$#" != "1" ];
then 
	echo "Please give a an input file"
	exit 1
fi

chr="\""
file=$1
cp $file $file."_backup"
while read -r line
do
 echo "${chr}$line${chr}"
done <$file > newfile
mv newfile $file
