from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'Bfinder_Bp_withcuts_MC2016'
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
config.Data.inputDataset ='/BuToJpsiK_BMuonFilter_SoftQCDnonD_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM'
config.Data.splitting ='FileBased'     #'LumiBased' for data
config.Data.unitsPerJob = 2

# set here the path of a storage area you can write to
config.Data.outLFNDirBase = '/store/user/bfontana/Bfinder_Bp_MC2016/'
#config.Data.lumiMask='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt' Json file for data

config.Data.publication= False
config.Data.outputDatasetTag='Pincopallino_Bp'
############## 

#config.Data.ignoreLocality = True

config.section_("Site")

# set here a storage site you can write to
config.Site.storageSite = 'T2_PT_NCG_Lisbon'
