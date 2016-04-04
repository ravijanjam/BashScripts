# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: test --conditions 80X_dataRun2_v0 -s RAW2DIGI,L1Reco,RECO,ALCA:SiStripCalZeroBias+SiStripCalMinBias+TkAlMinBiasHI+TkAlUpsilonMuMuHI+TkAlZMuMuHI+TkAlMuonIsolatedHI+TkAlJpsiMuMuHI+HcalCalMinBias,DQM --process reRECO -n 1000 --data --eventcontent RECO,DQM --runUnscheduled --scenario HeavyIons --datatier RECO,DQMIO --repacked --filein filelist:step1_dasquery.log --lumiToProcess step1_lumiRanges.log --fileout file:step2_pre1_80X_dataRun2_v0_1000Events.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('reRECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreamsHeavyIons_cff')
process.load('DQMOffline.Configuration.DQMOfflineHeavyIons_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( ('/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0011F55A-8F13-E111-A987-003048F118C6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0227BDCE-8B13-E111-86E2-003048F117F6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0229B820-9713-E111-A59F-0025B32035A2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/024F4CC2-9013-E111-AF6D-003048D2BC30.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/027E07AB-A413-E111-9AAE-BCAEC5329705.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0448B42B-9213-E111-838A-001D09F252DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/04B91CB8-9513-E111-ABB9-003048F110BE.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/04E17BE3-9713-E111-88CB-003048D37666.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/06444B4E-9413-E111-BF8A-00215AEDFCCC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0666C213-9013-E111-9EFA-003048D374F2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/069A61EB-9E13-E111-8E9A-BCAEC5329730.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/06C43B00-9513-E111-9183-002481E0D90C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/08028785-9D13-E111-A921-0025901D627C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/089CC0F6-9913-E111-9558-0025B32034EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0AC81316-9013-E111-AD10-003048F118C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0E213363-8A13-E111-BB14-001D09F24D4E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0EB17B74-9B13-E111-9DEC-003048F117B4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1025427C-9D13-E111-B4DF-003048F1110E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/123B0315-9013-E111-BDAA-003048F024DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/129A5F0E-9013-E111-A0CA-002481E0CC00.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/147F6F84-9113-E111-B68C-003048F024DC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/148D3DC0-A113-E111-9BDC-00237DDC5CB0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/16CEB115-9013-E111-B669-003048F118C4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/16DB826D-9613-E111-8A58-003048F117EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/184D8C81-9113-E111-AE83-0025901D623C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/18DB53C1-A113-E111-86AD-0025901D5DF4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1ACECD9A-9F13-E111-B120-001D09F29321.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1AD6866F-9613-E111-897E-BCAEC518FF5F.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1C029583-9113-E111-BF16-002481E0D958.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1C0AFE20-9713-E111-8739-003048F01E88.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1C49FFC1-A113-E111-9F89-BCAEC5364C4B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1C7B4E1E-9713-E111-A59F-002481E0DEC6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1C95E95C-8F13-E111-B08E-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/1E36EF6D-9413-E111-9D92-003048F11942.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/204F391F-9713-E111-89B0-003048F024DC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/20AE6F28-A313-E111-A372-003048F117EC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/224874BD-9013-E111-84C2-BCAEC518FF65.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/24C51908-9513-E111-85B0-003048F117EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/24CC53FE-9413-E111-A7A3-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/28654CEB-9E13-E111-860C-001D09F24FEC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/28B9FD38-8D13-E111-BCB9-002481E0D958.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/28E6BC82-9D13-E111-B8DB-BCAEC532972D.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/2A1E9F6D-9613-E111-9EAA-BCAEC53296F4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/2AB9886B-9613-E111-911A-BCAEC532970B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/2CD1436E-9613-E111-AE0B-0025901D5D7E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/2EC73521-9013-E111-9A55-003048F24A04.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/301FB1B9-9513-E111-A20A-0025B3203898.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/30A85F2B-9213-E111-9DAA-0019B9F581C9.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/32819C76-A213-E111-884C-003048D2C0F2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/32D97F20-9013-E111-BC87-003048F11114.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3420ED49-8D13-E111-8CB5-0025B32036D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/34273747-9413-E111-B853-003048D2BC30.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/346B6064-9B13-E111-B384-BCAEC53296FB.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/34C59FAD-9A13-E111-AF34-BCAEC53296FB.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/360E846E-9613-E111-8FE0-BCAEC5329708.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/36C2D9D3-9013-E111-AD68-00237DDC5C24.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3A01D1AD-9F13-E111-A0C6-BCAEC5329728.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3A230AF4-9913-E111-83DA-003048CFB40C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3A9790B2-9513-E111-8D32-003048F118AC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3C3E18BE-9513-E111-BC8C-002481E0D958.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3CB5A1D4-A113-E111-BAB2-BCAEC518FF74.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3CBA0B48-9713-E111-9B89-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3CE864E6-9E13-E111-86A6-BCAEC532970B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3E04962B-9213-E111-8DCC-001D09F24353.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3E460DBF-9013-E111-9D0E-003048D2BE06.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/3E7F2618-9013-E111-9369-BCAEC518FF89.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/40B915D8-8B13-E111-96CB-003048F01E88.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/40C969C4-9013-E111-A12E-003048F1C424.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/40F46ABB-9A13-E111-A197-003048F024C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/40FD2016-8B13-E111-ADAB-002481E0D90C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/421D7073-9E13-E111-9BF9-BCAEC5329726.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/427F0BC5-9013-E111-87A2-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/44601829-9C13-E111-B2EF-002481E0DEC6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/44948380-8C13-E111-B959-003048F24A04.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/44D5C2DB-9713-E111-8FBB-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/44D78F3A-8D13-E111-B555-003048F118C4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/46A104CE-8B13-E111-AE73-0025B32445E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/482DB686-A213-E111-B918-0025901D5D78.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/48447B2C-A313-E111-9877-003048F118C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4A297A4B-9913-E111-B06F-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4A82CFEC-9913-E111-B49E-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4A8DEDDE-9713-E111-B5D7-003048F1C420.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4C9B1FE8-8D13-E111-9C0D-003048F024FE.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4CCA116E-9613-E111-8EB8-0025B3203898.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4E4E391A-9C13-E111-9A96-E0CB4E553651.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4E536A5A-8F13-E111-AB89-001D09F29597.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/4EA3E2C0-A113-E111-BD05-0025901D5C88.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5019CB12-9013-E111-9CAF-002481E0D7D8.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/504BECA5-A413-E111-B8FB-BCAEC5329723.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/505E7A60-8F13-E111-A265-001D09F2B2CF.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/522689BD-9013-E111-ABCC-00237DDC5CB0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5271FEF3-9913-E111-8A96-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/527A09E2-9713-E111-B5AB-0025B32036D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/567FD96E-9613-E111-BB61-002481E0E56C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/581AE6FF-9713-E111-9918-002481E0D7C0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/588C2C9A-9F13-E111-BC64-001D09F241F0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5A1B9081-9113-E111-9152-BCAEC5329707.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5A4F4D14-9013-E111-852B-00237DDC5CB0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5A79CC2C-9213-E111-BD3F-001D09F24D4E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5AA16E1E-8B13-E111-A3A6-0025B32445E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5AE811A7-A413-E111-90C6-BCAEC518FF63.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5C07AC6D-9613-E111-B073-003048F1BF68.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5C732F3C-8D13-E111-9ADA-003048D2BEAA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5CB40C6F-9613-E111-8FE0-003048F024DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5E77BBDB-9713-E111-BF68-002481E0E56C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5E7BE4C2-A113-E111-90B1-E0CB4E55365D.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/5EB689D0-8B13-E111-8A8B-003048F024C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6003A07C-9D13-E111-8C42-0025901D624A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/606EE0AB-9A13-E111-B4DE-003048F118AA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/60C5A710-9013-E111-B7D3-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/60D6A82E-9713-E111-AECE-003048F117F6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/622EBBEC-9E13-E111-8662-001D09F24353.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/64E889AC-9A13-E111-81E7-003048F118C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/64F2DA18-9713-E111-8D74-003048CF94A6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6689457F-9113-E111-9866-00237DDC5C24.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/66AA0A7E-9D13-E111-98E8-003048F024DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/66B07EDC-9213-E111-A41F-001D09F297EF.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/66F257BE-9013-E111-BBDA-003048673374.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/68B20A62-9B13-E111-A849-BCAEC532970A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6A01C6CE-8B13-E111-B2E8-002481E0D83E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6A07788E-9113-E111-BA27-003048F118C4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6ADA3F71-A013-E111-8F45-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6C851AC7-9513-E111-BD43-0025901D5C86.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6E28ECB9-9513-E111-834B-BCAEC53296F4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6E709E2C-9213-E111-AE55-001D09F297EF.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6E74A7B2-9513-E111-A676-002481E0CC00.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6E86B8BC-9013-E111-868B-003048CF99BA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6E9EDAE7-9E13-E111-AA32-003048CF99BA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/6EB0EFC4-9A13-E111-8056-BCAEC53296F7.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/70295FDD-9213-E111-A4DE-001D09F2841C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/70A4661F-9713-E111-93D5-003048F117B6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/70D937C0-9013-E111-ABA6-003048F11942.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/70F3E9C4-A113-E111-90FE-0025B3244166.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7281B1E8-9E13-E111-8EA9-BCAEC5329714.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/74471F7F-9113-E111-9178-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/744A49AD-9A13-E111-BC8A-003048F024F6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7482A0CD-9513-E111-8381-003048F118AA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/74924C7F-9113-E111-B7C4-00215AEDFCCC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/74951C03-9513-E111-98EC-002481E0D7C0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/74C3FF72-A013-E111-A2E1-003048CF99BA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/74E25DED-9913-E111-A468-001D09F29146.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/763613EC-9E13-E111-A0C7-001D09F2512C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/76A3E4DC-9713-E111-9BE8-003048F11942.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/76F04E21-9713-E111-A044-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/76FC9CDF-9713-E111-8122-003048F117EC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/78181ED9-8B13-E111-9D47-003048CFB40C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7843586E-9613-E111-B027-003048F1BF66.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/78D5DF19-8B13-E111-8820-002481E0D83E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7A4B8B4C-9413-E111-A68B-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7A56E298-9F13-E111-862A-0019B9F72F97.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7C15CF80-9113-E111-99D7-00237DDC5BBC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7C29CC98-9F13-E111-9F29-001D09F2525D.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7C45CA4D-9913-E111-93A0-003048D2C0F2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7C69E6CA-9513-E111-9900-BCAEC532971F.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7CCD3E60-9E13-E111-91F7-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7CD07CB9-9513-E111-AFEE-003048F118C6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7E9446B6-9A13-E111-8335-003048F117B4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/7EE0B35D-8F13-E111-8E5C-001D09F28F25.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/82571A4F-9413-E111-BEFB-003048F117B6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8638C659-8F13-E111-8444-001D09F2AF96.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/864DE780-9113-E111-80EB-003048F118C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8653515E-9913-E111-A55F-003048F118E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8659D323-9C13-E111-86BB-BCAEC518FF44.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/866D719B-9F13-E111-8F55-001D09F24303.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/882ED7BD-9013-E111-9B92-002481E0D90C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/885946BF-9013-E111-A421-0025B320384C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8864B044-A513-E111-973B-BCAEC53296F5.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8890322A-9E13-E111-A3A8-BCAEC5329700.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/889E4361-A713-E111-9930-E0CB4E553651.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8A11C3CE-8B13-E111-93E5-003048F11C58.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8A445CDD-9713-E111-868E-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8C191FBE-9013-E111-87C3-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8CAD8224-9C13-E111-815E-00237DDBE41A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8E1A07F2-A813-E111-B4F4-003048F117F6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/8E2C301E-9713-E111-99F6-003048F11942.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9077C7DE-9713-E111-B6C8-002481E0D90C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/907CE513-9013-E111-AC1C-E0CB4E4408D5.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9093766F-A013-E111-BEAA-BCAEC5329718.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/92FEFA6E-9613-E111-83CA-00237DDC5AF6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/941A622D-9E13-E111-AAF2-0025901D624A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9444572C-9E13-E111-B216-BCAEC5329728.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/94E4ADE6-8D13-E111-AFAD-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/967A245E-8F13-E111-B19F-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9865FF7A-9113-E111-8609-0025B32034EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/98734F5B-8F13-E111-8ECE-001D09F2B30B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9A48DD04-9513-E111-816B-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9A8CE881-9113-E111-A413-BCAEC5329729.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9AB71B2B-9E13-E111-B6B4-BCAEC5329718.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9C3BDA27-A313-E111-9F4E-003048F1183E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9CB660F3-9E13-E111-98DF-BCAEC518FF8A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/9ED33B1A-9713-E111-BB7E-00237DDC5CB0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A01E6B3E-8D13-E111-8F80-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A09E532B-9213-E111-8780-001D09F290CE.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A0E100C4-9513-E111-B5D8-BCAEC518FF5F.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A238E184-A013-E111-A6EA-0025901D6272.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A29CC0ED-9913-E111-ACE3-001D09F253D4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A2B2A529-8B13-E111-A1EB-00237DDC5AF6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A45849BF-9013-E111-864D-003048F11114.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A47252E0-9713-E111-891C-00237DDC5AF6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A4918673-A213-E111-B39A-003048CF99BA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A4A2F770-A013-E111-B7D0-BCAEC5329708.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A4C4EDD9-9213-E111-B430-001D09F24353.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/A6908913-9513-E111-9C98-003048F11112.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AA2FF857-8F13-E111-BE64-0025B32036D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AA764B45-9913-E111-B757-003048F117EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AAFB6F22-9013-E111-B2D3-0025B32034EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AC58B6EB-9E13-E111-827B-003048F024C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AE143486-8C13-E111-BEB1-003048F118C6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AE4D8673-A013-E111-8B61-0025901D5DB8.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AE93BC1E-9713-E111-A7E1-003048D37666.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/AEF9C59E-9D13-E111-A1EE-002481E0D90C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B0312FD7-A313-E111-B6AE-BCAEC518FF74.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B0BDAC76-9B13-E111-8B1B-003048F118C2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B23B0FD9-9213-E111-916C-003048D2BEA8.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B4732EC1-A113-E111-BF5F-002481E0DEC6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B61EC01E-9713-E111-884E-003048F11C58.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B6BA8358-9413-E111-A56A-001D09F25460.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B83B88BB-9513-E111-AF03-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/B87BE4F9-8D13-E111-8972-002481E0D958.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BA99AC96-9F13-E111-9DAD-001D09F2512C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BAC56978-A213-E111-A3E6-00237DDBE41A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BC6B8610-8C13-E111-8B0A-003048673374.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BC718044-9413-E111-85AD-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BCA35047-9913-E111-9F20-BCAEC5364C42.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BCD92B6B-9613-E111-B192-BCAEC5329720.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BE27C81E-9713-E111-A4D3-003048F24A04.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BE6828D7-9713-E111-9DDD-003048F024DC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BE76F32B-9213-E111-853F-001D09F2512C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BEB85E45-9913-E111-BF37-BCAEC532971F.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/BEB8B1A5-A413-E111-B6FF-BCAEC532971E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C00FB480-9113-E111-8778-003048F118C6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C010B3D7-A313-E111-ADB2-BCAEC532971C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C0666C13-9013-E111-8463-002481E0DEC6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C06FB760-9413-E111-85F5-003048D2C0F2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C07422E8-8D13-E111-B698-003048F1BF66.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C074567E-9113-E111-B935-0025B32036D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C095941E-9713-E111-8F03-003048F11DE2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C0AC5796-9F13-E111-850E-0025B320384C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C2B38886-A213-E111-8839-0025901D5DB2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C45AB8BF-9513-E111-BB02-BCAEC5329708.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C646B5F3-9913-E111-B0BA-003048F117EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C67BD3D7-A313-E111-8978-E0CB4E4408E7.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C69802BD-9513-E111-A099-BCAEC518FF89.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C6EE54FC-9913-E111-A2BC-003048CF94A8.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C853421E-9713-E111-8687-002481E0D958.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C8BD8CC5-8B13-E111-B5F5-00237DDC5AF6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C8C0DA15-9013-E111-B38E-00237DDBE41A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/C8FCDB2D-9013-E111-A155-0025B3203898.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CC450A99-9F13-E111-B325-001D09F2B30B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCA5CF4C-9913-E111-96FD-003048F118AC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCA76445-A513-E111-8C31-BCAEC532972E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCAFD8C2-A113-E111-9999-0025901D6272.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCCA7776-A213-E111-BB1D-003048F1183E.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCE808D7-9713-E111-A486-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CCEA9617-9013-E111-A725-0025B3244166.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CE26EBBB-9013-E111-93AB-003048F024DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CE7D5A89-9D13-E111-BC2D-003048F117EA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CE9FD02C-9E13-E111-A3B4-BCAEC518FF5A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/CEC65680-9D13-E111-AD81-003048D2BED6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D002D92D-A313-E111-B22D-BCAEC5364CFB.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D0BC2619-9C13-E111-8F11-003048F117EC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D2205AD2-A813-E111-9AFA-003048CF99BA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D243CCA5-A413-E111-9F96-BCAEC53296F7.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D2894901-9513-E111-9695-003048F1C424.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D2CF5301-9F13-E111-8895-001D09F25041.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D4E6CA6F-A013-E111-AE3E-0025B3244166.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D660DE95-9F13-E111-AA87-003048F11112.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/D858D447-9913-E111-BADA-00237DDBE49C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/DA04852C-9213-E111-81D8-001D09F253D4.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/DC16AC16-9513-E111-8BD2-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/DCDDEEE1-9213-E111-953C-003048D373F6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/DCEC64BE-9513-E111-9073-003048F024DA.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/DE38B970-9613-E111-B9F3-BCAEC5364C62.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E00DA2E6-8D13-E111-8617-003048F11CF0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E076F689-8C13-E111-8833-001D09F23C73.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E0845AB9-9513-E111-A07A-BCAEC518FF63.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E0B227C8-9513-E111-99D3-BCAEC532970B.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E22E1165-9B13-E111-B9E7-E0CB4E4408D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E26D5483-8C13-E111-8840-002481E0D7D8.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E299AA7C-9D13-E111-92B7-003048F118AC.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E4529DFF-9413-E111-AA0A-002481E0DEC6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E4B34770-9613-E111-AB98-BCAEC518FF63.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E8C377AA-A413-E111-8641-BCAEC5364C6C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EA45231A-9713-E111-85B9-0025B320384C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EA897F17-9513-E111-910B-003048F118C6.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EAA78B18-9C13-E111-AA0E-0025901D625A.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EE727C47-9913-E111-95F6-003048F024E0.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EE761546-9913-E111-A9DD-002481E0D790.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/EE999C9A-9F13-E111-8AA7-003048D2BC62.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F27C9614-9013-E111-BF68-BCAEC5329707.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F293D080-9113-E111-AFC9-E0CB4E4408D1.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F2A3BF25-9813-E111-859D-003048F11C58.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F2AD777E-9113-E111-8534-0025B32036E2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F48CC680-8C13-E111-ACA5-003048F118D2.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F6DF5921-9013-E111-96DE-00237DDBE49C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F81D2D71-9B13-E111-BCC2-003048F24A04.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F884AF4D-9413-E111-B8C8-002481E0E56C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F8D0E5CC-A113-E111-AA9D-00237DDC5C24.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/F8FB0781-9113-E111-9D9B-00237DDBE49C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/FAD10422-A313-E111-A816-BCAEC532971C.root', 
        '/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/FE6DE36B-8F13-E111-B683-002481E0DEC6.root' ) ),
    lumisToProcess = cms.untracked.VLuminosityBlockRange("182124:1-182124:268435455"),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test nevts:1000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step2_pre1_80X_dataRun2_v0_1000Events.root'),
    outputCommands = process.RECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2_pre1_80X_dataRun2_v0_1000Events_inDQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.ALCARECOStreamHcalCalMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalMinBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('ALCARECOHcalCalMinBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('ALCARECOHcalCalMinBias.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_gtDigisAlCaMB_*_*', 
        'keep HBHERecHitsSorted_hbhereco_*_*', 
        'keep HORecHitsSorted_horeco_*_*', 
        'keep HFRecHitsSorted_hfreco_*_*', 
        'keep HFRecHitsSorted_hfrecoMBspecial_*_*', 
        'keep HBHERecHitsSorted_hbherecoNoise_*_*', 
        'keep HORecHitsSorted_horecoNoise_*_*', 
        'keep HFRecHitsSorted_hfrecoNoise_*_*')
)
process.ALCARECOStreamSiStripCalMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalMinBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('SiStripCalMinBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SiStripCalMinBias.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOSiStripCalMinBias_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*')
)
process.ALCARECOStreamSiStripCalZeroBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalZeroBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('SiStripCalZeroBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SiStripCalZeroBias.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOSiStripCalZeroBias_*_*', 
        'keep *_calZeroBiasClusters_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep *_TriggerResults_*_*')
)
process.ALCARECOStreamTkAlJpsiMuMuHI = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlJpsiMuMuHI')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlJpsiMuMuHI')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlJpsiMuMuHI.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlJpsiMuMuHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*')
)
process.ALCARECOStreamTkAlMinBiasHI = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBiasHI')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMinBiasHI')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMinBiasHI.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMinBiasHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*', 
        'keep *_offlineBeamSpot_*_*')
)
process.ALCARECOStreamTkAlMuonIsolatedHI = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolatedHI')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMuonIsolatedHI')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMuonIsolatedHI.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlMuonIsolatedHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*')
)
process.ALCARECOStreamTkAlUpsilonMuMuHI = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlUpsilonMuMuHI')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlUpsilonMuMuHI')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlUpsilonMuMuHI.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlUpsilonMuMuHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*')
)
process.ALCARECOStreamTkAlZMuMuHI = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMuHI')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlZMuMuHI')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlZMuMuHI.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_ALCARECOTkAlZMuMuHI_*_*', 
        'keep L1AcceptBunchCrossings_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep *_hiSelectedVertex_*_*')
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMuonIsolatedHI_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlUpsilonMuMuHI_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlJpsiMuMuHI_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalZeroBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlZMuMuHI_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOHcalCalMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMinBiasHI_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_v0', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.dqmoffline_step = cms.Path(process.DQMOfflineHeavyIons)
process.dqmofflineOnPAT_step = cms.Path(process.DQMOfflineHeavyIons)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)
process.ALCARECOStreamHcalCalMinBiasOutPath = cms.EndPath(process.ALCARECOStreamHcalCalMinBias)
process.ALCARECOStreamSiStripCalMinBiasOutPath = cms.EndPath(process.ALCARECOStreamSiStripCalMinBias)
process.ALCARECOStreamSiStripCalZeroBiasOutPath = cms.EndPath(process.ALCARECOStreamSiStripCalZeroBias)
process.ALCARECOStreamTkAlJpsiMuMuHIOutPath = cms.EndPath(process.ALCARECOStreamTkAlJpsiMuMuHI)
process.ALCARECOStreamTkAlMinBiasHIOutPath = cms.EndPath(process.ALCARECOStreamTkAlMinBiasHI)
process.ALCARECOStreamTkAlMuonIsolatedHIOutPath = cms.EndPath(process.ALCARECOStreamTkAlMuonIsolatedHI)
process.ALCARECOStreamTkAlUpsilonMuMuHIOutPath = cms.EndPath(process.ALCARECOStreamTkAlUpsilonMuMuHI)
process.ALCARECOStreamTkAlZMuMuHIOutPath = cms.EndPath(process.ALCARECOStreamTkAlZMuMuHI)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.pathALCARECOTkAlMuonIsolatedHI,process.pathALCARECOTkAlUpsilonMuMuHI,process.pathALCARECOTkAlJpsiMuMuHI,process.pathALCARECOSiStripCalZeroBias,process.pathALCARECOTkAlZMuMuHI,process.pathALCARECOSiStripCalMinBias,process.pathALCARECOHcalCalMinBias,process.pathALCARECOTkAlMinBiasHI,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.RECOoutput_step,process.DQMoutput_step,process.ALCARECOStreamHcalCalMinBiasOutPath,process.ALCARECOStreamSiStripCalMinBiasOutPath,process.ALCARECOStreamSiStripCalZeroBiasOutPath,process.ALCARECOStreamTkAlJpsiMuMuHIOutPath,process.ALCARECOStreamTkAlMinBiasHIOutPath,process.ALCARECOStreamTkAlMuonIsolatedHIOutPath,process.ALCARECOStreamTkAlUpsilonMuMuHIOutPath,process.ALCARECOStreamTkAlZMuMuHIOutPath)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

