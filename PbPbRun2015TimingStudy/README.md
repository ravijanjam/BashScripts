<snippet>
  <content>
# ${1:PbPb 2015 Timing Study }
Scripts provided here help estimate the Timing Per Module for Timing Study at 
Vanderbilt Tier2

Information for this study is documented in the links below : 
https://twiki.cern.ch/twiki/bin/viewauth/CMS/PbPb2015PeriphReReco75Xpp
https://indico.cern.ch/event/503314/contribution/17/attachments/1235228/1813177/CMS-HIWest-ppRereco-WeiLi-02262016.pdf


## Usage
0. Login to your local cluster or lxplus CERN

1. cmsrel CMSSW_7_5_8_patch3
2. cd CMSSW_7_5_8_patch3
3. cd src
4. git clone <url of this repository>
5. cmsenv 
6. cmsRun step3_RAW2DIGI_L1Reco_RECO.py 1>output.stderr 2>output.stdout
7. ./PbPbRun2015TimingStudy.sh output.stdout > TimePerModule.txt
8. cat TimePerModule.txt

An example TimePerModule_eg.txt is in the same directory. 
cat TimePerModule_eg.txt and scroll to the bottom for Timing Information summary
</content>
  <tabTrigger>readme</tabTrigger>
</snippet>
