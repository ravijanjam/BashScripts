## CMS Heavy Ion Dynamic Data Management Inventory

To identify the data sets used by CMS Heavy Ion, since HI Data Sets are not part of *Dynamic Data Management(DDM)* system used by CMS worldwide.

* Do grid-proxy-init from inside a CMSSW directory.

* Apply permissions to bash scripts in this directory, `chmod 700 *.sh`

* Change the options in the bash script `genDDM.sh`, with arguments as shown below:

```./ACCRE_DDM.sh DASDataSetQuery JSONTag startDate endDate queryFilter```

| KeyWord | Explanation |
| ---- | ---- |
| `DASDataSetQuery`| The CERN Data Aggregation System data sets query string, fetching the results for Vanderbilt Tier 2 computing cluster |
| `startDate`| beginnning date since when the usage of data sets should be counted for |
| `endDate`| ending date until when the usage of data sets should be counted for |
| `queryFilter`| Which data sets should be searched for and matched by Popularity API and DAS Query |
| `JSONTag` | An identifier for unique identification of JSON output files per query |

The script [**genDDM.sh**](https://github.com/ravijanjam/BashScripts/blob/master/CMSHIDDM/genDDM.sh) contains a list of examples. 

* Copy the webpage, `CMSHIDynamicDataManagement.html, Info_<JSONTag1>.json,..., Info_<JSONTagn>.json` and put it on a web server with appropriate permissions.

* Core Dependencies: `das_client` binary for querying CERN Data Aggregation System(DAS), Popularity API based


## References
Requires CERN Grid Certificate and PEM to access the information

[Popularity Data Sets](https://twiki.cern.ch/twiki/bin/view/Main/DataPopularity)

[CERN Data Aggregation System(DAS)](https://cmsweb.cern.ch/das/)

