#!/bin/bash

declare -a pTHat=(10 20 30 50 80 120 170 230 300 380 10000)

declare -a procSwitchLabels=( Inelastic \
			NSD \
			HardQCDSelectionGluon \
			HardQCDSelectionQuark \
			HardQCDAll)


declare -a pdfSetLabels=(GRV94L-LO \
			CTEQ5L-LO \
			MRST-LO\(2007\) \
			MRST-LO\(2008\) \
			MRST-LO\(2008-CentralMember\) \
			MRST-NLO\(2008-CentralMember\) \
			CTEQ6L-NLO \
			CTEQ6L1-LO \
			CTEQ66.00 \
			CT09MC1-LO \
			CT09MC2-NLO \
			CT09MCS-NLO \
			NNPDF2.3-QCD+QED-LO13 \
			NNPDF2.3-QCD+QED-LO14 \
			NNPDF2.3-QCD+QED-NLO \
			NNPDF2.3-QCD+QED-NNLO \
			)



function appendQuotes2FilesInCurrentDir(){

		list=`ls | awk '{print "\""$1"\","}' | sed '$s/,$//g' | sed 's/\"/\\\"/g'`

		echo -e "List of files with quotes added and trailing comma removed in current directory\n\n"
		echo ${list}

		echo -e "\n\n====Before Replacement====="
		cat test.c

		perl -p -e "s/replaceVar1/$list/g" test.c > testTemp.c

		echo -e "====After Replacement======\n\n"
		cat testTemp.c
		echo "====After Replacement - orig======"
		cat test.c
}

function varReplace(){

	echo "=== before rep-orig ==="
	cat test.c
	echo "======================="

	### Replace inside the file ###
	cat test.c | perl -p -e "s/replaceVar1/$1/"  
	echo "=== after rep-orig ===="
	cat test.c
	echo "======================="

}

case $1 in 
	1)
		listOfFiles=`ls`
		echo "option $1"
		echo ${listOfFiles} | sed -i 's/\w//g'
		;;

	2)
		echo "option $1"
		echo "Append quotes and remove the last comma per Process"
		echo "Outputs will be of the form \"File1.xyz\", \"File2.abc\""
		echo "==================================================="

		for pr in ${procSwitchLabels[@]}
		do
			echo $pr
			echo -e "=====================================================================\n"
			files=`ls OutputRootFiles/*$pr*.root`
			list=`ls OutputRootFiles/*$pr*.root | awk '{print "\""$1"\","}' | sed '$s/,$//g'`
			echo ${list}
			echo -e "======================================================================\n\n\n"

		done
			### Replace inside the file ###
			sed "s/replaceVar1/"$list"/"  test.c

		;;


	3)
		 appendQuotes2FilesInCurrentDir
		 ;;

	4)
		echo -e "Replacing data passed to a variable in bash manually into a placeholder variable in an external file"
		files=\"3\",\"5\"
		varReplace ${files}
		;;

	5)
		echo "option $1"

		echo -e "\n\n\nAppend quotes and remove the last comma per Process"
		echo "Outputs will be of the form \\\"File1.xyz\\\", \\\"File2.abc\\\""
		echo "==================================================="
		echo -e "\n\n\n"

		for pr in ${procSwitchLabels[@]}
		do
			echo $pr
			echo -e "=====================================================================\n"
			files=`ls OutputRootFiles/*$pr*.root`
			list=`ls OutputRootFiles/*$pr*.root | awk '{print "\""$1"\","}' | sed '$s/,$//g' | sed 's/\"/\\\"/g'`
			echo ${list}
			echo -e "======================================================================\n\n\n"

		done
		;;
		
	*) 
		echo "nothing"
		break
esac
