from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'Bfinder_2015Data_RunD_3unitsPerJob_1'
# request name is the name of the folder where crab log is saved

config.General.workArea = 'crab3_projects'
config.General.transferOutputs = True
config.General.transferLogs = True #False


config.section_('JobType')
# set here the path of your working area
config.JobType.psetName = 'Bfinder_pp_80x_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['bfinder.root']
config.JobType.allowUndistributedCMSSW = True

config.section_('Data')
config.Data.inputDataset = '/Charmonium/Run2015D-16Dec2015-v1/AOD'
config.Data.splitting = 'LumiBased'     #'FileBased' for MC
config.Data.runRange = '254227-258434'
config.Data.unitsPerJob = 3

# set here the path of a storage area you can write to
config.Data.outLFNDirBase = '/store/user/bfontana/Bfinder_Data2015_RunD/'
config.Data.lumiMask='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_MuonPhys.txt' 

config.Data.publication= False
config.Data.outputDatasetTag='X'
############## 

#config.Data.ignoreLocality = True

config.section_("Site")

# set here a storage site you can write to
config.Site.storageSite = 'T2_PT_NCG_Lisbon'
