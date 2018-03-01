#!/bin/bash

# Remove the file into which the
# results are populated 
rm fileInfo.dat


# Recipe Used to Calculate Julian Date
# http://aa.usno.navy.mil/faq/docs/JD_Formula.php
gJD=0
GenJulianDate(){

	gJD=0
	#echo "Inside julian: "
	#echo $1

	# Break down date 
	sDt=(`echo "$1" | sed -n 's/\([0-9]\+\)-\([0-9]\+\)-\([0-9]\+\)/\1 \2 \3/p'`)

	dd=`sed 's/0\+\([1-9]\+\)/\1/g' <<< ${sDt[2]}`
	mm=`sed 's/0\+\([1-9]\+\)/\1/g' <<< ${sDt[1]}`
	yy=${sDt[0]}


	#echo ${sDt[@]}
	#echo "Month: " $mm

	jd=$(($dd - 32075 + 1461 * ($yy + 4800 - (14 - $mm) / 12) / 4 + 367 * ($mm - 2 + ((14 - $mm) / 12) * 12) / 12 - 3 * (($yy + 4900 - (14 - 9) / 12) / 100) / 4))


	#echo "julian date: "$jd

	#echo ;
	#echo $jd
	gJD=$jd

	#echo "end of GenJulianDate"
}


# Check date format
checkDate(){

	# Start Date
	sD=$1

	# End Date
	eD=$2
	GenJulianDate $sD
	sjD=$gJD

	GenJulianDate $eD
	ejD=$gJD

	if [[ $ejD -gt $sjD ]]
	then
		#echo "yes"
		echo 1
	else
		echo -e "\e[5m\e[91m Ending date is before the starting date......!!\e[0m"
		echo ;
		exit 1
	fi

}

func1(){

	# Path from where the directories would be searched recursively
	iPath=`sed -n 's/iPath=\(.*\)/\1/p' <<< $1`
	iPath=`echo $iPath | sed 's/\s/\\\|/g'`

	echo "Initial path: "$iPath

	# Get the start and end date
	sD=`sed -n 's/sDate=\(.*\)/\1/p' <<< $3`
	eD=`sed -n 's/eDate=\(.*\)/\1/p' <<< $4`


	# At this point, date check happens, if it's a failure, the program stops
	checkDate $sD $eD	

	GenJulianDate $sD
	sjD=$gJD

	GenJulianDate $eD
	ejD=$gJD

	echo "from julian dates "$sjD, $ejD

	# List of directories to be excluded from the search
	eExcl=`sed -n 's/eExcl=\(.*\)/\1/p' <<< $2`
	eExcl=`echo $eExcl | sed 's/\s/\\\|/g'`
	echo $eExcl

	# Check if there are no excluded directories provided
	if [[ -z "$eExcl" ]] 
	then 

		# Get list of all directories recursively after filtering the excluded directories
		dl=`ls -R ${iPath} | grep ":$" | sed 's/://g'`
		echo "if" 

	else

		# Get list of all directories recursively after filtering the excluded directories
		dl=`ls -R ${iPath} | grep -i -v ${eExcl} | grep ":$" | sed 's/://g'`

	fi

	#echo $dl


	# Loop over all the directory list
	for dir in $dl
	do
		echo "Path: "$dir

		# Get the file list count
		fc=`ls $dir/*.* 2> /dev/null | wc -l`

		# Initialize array for extension type
		declare -A earr

		# Check if Empty
		if [[ "$fc" == "0" ]]
		then
			echo "no files, probably a directory" $fc

		else

			# Get list of files in the current directory
			arr=`ls -ltrh $dir | awk '{print $9}' | sed -n 's/\(.*\)\.\(.*\)/\2/p' | tr "\n" "," | sed 's/,$//g'`
			#echo "array list:$arr"


			# Check if the folder date fits in the required 
			fDate=`ls -R --full-time -d $dir | awk '{print $6}'`

			GenJulianDate $fDate
			cjD=$gJD

			#echo "date info[current, start, end]: " $cjD, $sjD, $ejD
			k1=$(( $cjD - $sjD ))
			k2=$(( $ejD - $cjD ))

			if [[ $k1 -ge 0 && $k2 -ge 0 ]]	
			then

				# Find the unique file extensions per directory
				ext=`python findIdentical1.py $arr | sed 's/,\|\[\|\]//g' | tr "'" " "`
				
				#echo $dir
				#echo $ext

				# Loop over extensions
				for e in $ext
				do

					# Counter for files 
					cc=0

					# Count the number of files and the size
					fDat=(`ls -lt $dir/*.$e 2> /dev/null | awk '{sum+=$5}END{print NR, sum/1024/1024}'`)

					let cc=cc+${fDat[0]}

					#echo ${fDat[1]} MB
					#echo "cc: "$cc
						

					# File count by extension
					ec=`ls $dir/*.$e | wc -l`
					earr[$e]=$ec
					echo "$e:${fDat[0]}, size:${fDat[1]} MB" | tr "\n" "\t"

				done
		
		echo ;
			fi
		fi

		echo ;

	done
}


# Unit tests for check date
#checkDate 2018-02-01 2017-02-15
#checkDate 2012-02-01 2016-02-15

# Unit tests for GenJulianDate
#GenJulianDate 2018-02-01

func1 iPath="/store/"  \
      eExcl="data relval group" \
      sDate=2012-01-01 \
      eDate=2017-02-15 \

#dExcl="LC_MESSAGES bokadia" \

