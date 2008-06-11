# The following comments couldn't be translated into the new config version:

# Configuration file to run stubs/CSCGeometryAnalyser
# to dump CSC geometry information
# Tim Cox 16.08.2007. 
# Update 11.06.2008 because MessageLogger now doesn't want explicit file extensions.

import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")
# xml for endcap csc geometry
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("Geometry.MuonCommonData.muonEndcapIdealGeometryXML_cfi")

# flags for modelling of CSC layer & strip geometry
process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.EnableFloatingPointExceptions = cms.Service("EnableFloatingPointExceptions",
    enableOverFlowEx = cms.untracked.bool(True),
    enableDivByZeroEx = cms.untracked.bool(True),
    enableInvalidEx = cms.untracked.bool(True),
    enableUnderFlowEx = cms.untracked.bool(False)
)

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.MessageLogger = cms.Service("MessageLogger",
    errors = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR'),
        extension = cms.untracked.string('.out')
    ),
    # No constraint on log content...equivalent to threshold INFO
    # 0 means none, -1 means all (?)
    log = cms.untracked.PSet(
        extension = cms.untracked.string('.out')
    ),
    debug = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        extension = cms.untracked.string('.out'),
        CSC = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        noLineBreaks = cms.untracked.bool(True),
        DEBUG = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        CSCNumbering = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        threshold = cms.untracked.string('DEBUG'),
        CSCGeometryBuilderFromDDD = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        ),
        RadialStripTopology = cms.untracked.PSet(
            limit = cms.untracked.int32(-1)
        )
    ),
    # For LogDebug/LogTrace output...
    debugModules = cms.untracked.vstring('*'),
    categories = cms.untracked.vstring('CSC', 
        'CSCNumbering', 
        'CSCGeometryBuilderFromDDD', 
        'RadialStripTopology'),
    destinations = cms.untracked.vstring('log', 
        'errors', 
        'debug')
)

process.producer = cms.EDAnalyzer("CSCGeometryAnalyzer")

process.p1 = cms.Path(process.producer)
process.CSCGeometryESModule.debugV = True
