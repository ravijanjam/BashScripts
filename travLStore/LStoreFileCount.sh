#!/bin/bash

rm fileInfo.dat

# Global Counter for all the files
gc=0

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

func16(){
	
	#rExt: desired extention list
	#dSch: don't search in these directories

	# Get the start and end date
	sD=`sed -n 's/sDate=\(.*\)/\1/p' <<< $3`
	eD=`sed -n 's/eDate=\(.*\)/\1/p' <<< $4`

	# At this point, date check happens, if it's a failure, the program stops
	checkDate $sD $eD	

	GenJulianDate $sD
	sjD=$gJD

	GenJulianDate $eD
	ejD=$gJD

	#echo "[Start, End] (Normal, Julian) Date : "$sD, $eD, $sjD, $ejD


	# Directory to start from, make sure you have a backslash
	iPath=`sed -n 's/iPath=\(.*\)/\1/p' <<< $5`

	# Excluded list, feel free to use a star for a more general match
	#dExcl="MyMacros ppRef_crab_projects ChargedParticles_v6"
	dExcl=`sed -n 's/dExcl=\(.*\)/\1/p' <<< $2`
	dExcl=`echo $dExcl | sed 's/\s/\\\|/g'`

	echo "Folders excluded from the list: " $2
	echo ;
	
	# Extension list to include 
	rExt=`sed -n 's/rExt=\(.*\)/\1/p' <<< $1`

	echo "Extensions included: " $rExt
	#rExt="txt py pyc"

	# Obtain the list of directories and exclude those that are not needed
	dl=`ls -R ${iPath} | grep ":$" | grep -i -v "${dExcl}" | sed 's/://g'`
	#echo $dl


	# Loop over folders
	for dfile in ${dl}
	do
			echo ;

			nfiles=`ls $dfile/*.* 2> /dev/null | wc -l`


			# Check if the folder date fits in the required 
			fDate=`ls -R --full-time -d $dfile | awk '{print $6}'`
			#fDate=`ls -R --full-time -d $dfile | awk '{print $6, NR}'`
			#echo "fDate: "$fDate
			GenJulianDate $fDate
			cjD=$gJD

			#echo "date info[current, start, end]: " $cjD, $sjD, $ejD

			k1=$(( $cjD - $sjD ))
			k2=$(( $ejD - $cjD ))

			# Check if current date is in between the start date and end date
			if [[ $k1 -ge 0 && $k2 -ge 0 ]]	
			then
				#echo "yes"

				# Counter for matched files
				cc=0

				# Loop over chosen file extensions
				for ext in ${rExt}
				do
					# Count the number of files and the size
					fDat=(`ls -lt $dfile/*.$ext 2> /dev/null | awk '{sum+=$5}END{print NR, sum/1024/1024}'`)

					if [[ ${fDat[0]} > 0 ]]
					then
						echo "In the directory: "$dfile >> fileInfo.dat
						echo -e "\t\t files extension, count, size: $ext, ${fDat[0]}, ${fDat[1]} MB" >> fileInfo.dat
						echo "" >> fileInfo.dat
						let cc=cc+${fDat[0]}
						let gc=gc+cc; 
					fi
				done
					#echo -e "\t\tTotal number of files with the matched extension set: "$cc
			else
				echo ;
			fi

	#echo "Total number of files: "$nfiles
	done

}

# This order matters
func16 rExt="gz" \
       dExcl="data" \
       sDate=2012-01-01 \
       eDate=2018-02-15 \
       iPath="/store/user/"
       #iPath="/store/data/Run2013A"
       #iPath="~/CMSSW_7_4_0/"
       #iPath="/store/data/Run2015E/"
       #iPath="/store/"
       #iPath="/store/user/"
       #iPath="/store/data/Run2015E/"
       #iPath="/store"

echo "Total number of files: "$gc >> fileInfo.dat
echo -e "Open the file: \e[1mfileInfo.dat\e[25m in the current directory to check the results"
