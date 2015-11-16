#!/bin/bash


if [ $# -ne 1 ]; then
echo "Generates a dummy CSV file, set ranges accordingly for the \
      the parameters for which you would like to generate data "

echo "NOTE : It takes a pretty long time to generate....."

echo ;
echo "The script spits out the time it took in generating data"


echo "======================================================================="
echo "Please run the script by providing the number of data points you would \	
	like to genereate | ./generateCSVData.sh 50 "
echo "======================================================================="

elif [ $1 -ge 1 ]; then 

echo "Deleting the CSV Data file"
rm CSVData.csv

# Passing header into the csv file
echo "Height, Weight, Grade" > CSVData.csv

START=$(date +%s)

count=0
while [ 1 ]
do
	height=${RANDOM}
	weight=${RANDOM}
	
	if [ ${height} -le  6 ] &&  [ ${weight} -le 200 ]; then
		echo ${height}, ${weight} >> CSVData.csv
		let count=count+1
	fi 

	# Generate the number of values 
	if [ ${count} -eq $1 ]; then
		break;
	fi 
done 
#echo ${height}, ${weight}
END=$(date +%s)
DIFF=$(( $END - $START ))

echo "It took ${DIFF} seconds of time to run this script"
fi 
