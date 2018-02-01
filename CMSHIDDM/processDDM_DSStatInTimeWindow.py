import sys, json, subprocess, math, re

# Data Set 
def perDataSetAccess(popDatInfo, dasDataInfo, mList, tagName):

	print "Results for the dsName: ", popDatInfo + ".json"

	''' Type of Popularity API used, if this changes, the logic in this function will have to change as the output json formatting changes and hence the web page formatting
	'''
	if popDatInfo=="DSStatInTimeWindow":

		popDat = json.load(open(popDatInfo + ".json", "r"))
		dasDat = json.load(open(dasDataInfo, "r"))


		''' Output json file '''
		infile = open("Info_" + tagName +".json", "w")

		global cc1
		cc1=0
		obj = {}

		rStr = mList

		dsTotal=0
		naccTotal=0
		totcpuTotal=0
		nusersTotal=0

		# Loop over dataasets from DAS
		for dk, dv in dasDat.iteritems():
			# Loop over datasets from Popularity API
			for info in popDat["DATA"]:

				# Check if the sub string found in Popularity datasets
				if len(re.compile(rStr, re.I).findall(info["COLLNAME"]))>0:

					# Check if the dataset name in DAS datasets matches with the Popularity datasets
					if len(re.compile(dk, re.I).findall(info["COLLNAME"]))>0:

						cc1 = cc1+1

						''' Convert to tera bytes '''
						datasetSize = math.floor(float(dv)*1000/1024/1024/1024/1024)/1000

						# Creating the object defintion 
						obj[cc1] = {"COLLNAME":dk, "DATASET_SIZE":datasetSize, "NACC":0, "TOTCPU":0, "NUSERS":0}

						# When matched populated into the obj
						obj[cc1]["TOTCPU"] = info["TOTCPU"]
						obj[cc1]["NACC"] = info["NACC"]
						obj[cc1]["NUSERS"] = info["NUSERS"]

						# For aggregate stats
						dsTotal += datasetSize
						naccTotal += info["NACC"]
						totcpuTotal +=  info["TOTCPU"]
						nusersTotal +=  info["NUSERS"]

		dsTotal = math.floor(dsTotal*1000)/1000
		print "Aggregate stats of the data sets: ", cc1, dsTotal, naccTotal, nusersTotal, totcpuTotal 
		obj["totalStats"] = {"COLLNAME":0, "DATASET_SIZE":dsTotal, "NACC":naccTotal, "TOTCPU":totcpuTotal, "NUSERS":nusersTotal}

		#print "the final obj:", obj
		infile.write(json.dumps(obj))
		infile.close()
		print "\n\n"


perDataSetAccess(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
