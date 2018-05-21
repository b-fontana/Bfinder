from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.requestName = 'Bfinder_Bs_withcuts_MC2016'
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
config.Data.inputDataset ='/BsToJpsiPhi_BMuonFilter_SoftQCDnonD_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM'
config.Data.splitting ='FileBased'     #'LumiBased' for data
config.Data.unitsPerJob = 5

# set here the path of a storage area you can write to
config.Data.outLFNDirBase = '/store/user/bfontana/Bfinder_Bs_MC2016/'
#config.Data.lumiMask='https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_MuonPhys_v2.txt' Json file for data

config.Data.publication= False
config.Data.outputDatasetTag='Pincopallino'
############## 

#config.Data.ignoreLocality = True

config.section_("Site")

# set here a storage site you can write to
config.Site.storageSite = 'T2_PT_NCG_Lisbon'
