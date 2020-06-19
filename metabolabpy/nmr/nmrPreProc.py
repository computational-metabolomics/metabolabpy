'''
NMR data pre-processing

'''

import numpy as np


class NmrPreProc:
    
    def __init__(self):
        self.excludeStart              = np.array([])
        self.excludeEnd                = np.array([])
        self.segStart                  = np.array([])
        self.segEnd                    = np.array([])
        self.segAlignRefSpc            = 1
        self.noiseThreshold            = 4.0                         # times std of noise region
        self.noiseStart                = 10.0
        self.noiseEnd                  = 10.5
        self.bucketPoints              = 0
        self.bucketPPM                 = 0.005
        self.compressBuckets           = False
        self.scaleSpc                  = ""
        self.varianceStabilisation     = ""
        self.varLambda                 = 1e-5
        self.varX0                     = 0.0
        self.pName                     = ""
        self.fName                     =""
        self.samplesInRows             = True
        self.plotSelect                = np.array([])
        self.classSelect               = np.array([])
        self.plotColours               = []
        self.preProcFill               = False
        self.alpha                     = 1.0
        self.colour                    = 'gray'
        self.thColour                  = 'red'
        self.thLineWidth               = 2.0
        self.flagExcludeRegion         = False
        self.flagSegmentalAlignment    = False
        self.flagNoiseFiltering        = False
        self.flagBucketSpectra         = False
        self.flagCompressBuckets       = False
        self.flagScaleSpectra          = False
        self.flagVarianceStabilisation = False
        self.flagExportDataSet         = False
        self.stdVal                    = 0.0
        self.exportPathName            = ""
        self.exportFileName            = ""
        self.exportDelimiterTab        = True
        self.exportCharacter           = ","
        self.exportSamplesInRowsCols   = 0
        self.rDolphinExport            = False
        # end __init__

    def __str__(self): # pragma: no cover
        strStr = "NMR data pre-processing"
        return strStr
        # end __str__

    def init(self, nspc):
        self.plotSelect     = np.arange(nspc)
        self.classSelect    = np.empty(nspc, dtype = 'str')
        for k in range(nspc):
            self.classSelect[k] = "1"
            
        self.initPlotColours()
        return "pre-processing initialised"
        # end init
        
    def initPlotColours(self, int1 = 0.4, int2 = 0.8, int3 = 0.4):
        self.plotColours = [( 0.0,  0.0, int1),
                            (int1,  0.0,  0.0),
                            ( 0.0, int1,  0.0),
                            ( 0.0, int1, int1),
                            (int1, int1,  0.0),
                            (int1,  0.0, int1),
                            (int3, int3, int2),
                            (int2, int3, int3),
                            (int3, int2, int3),
                            (int3, int2, int2),
                            (int2, int2, int3),
                            (int2, int3, int2)]
        # end initPlotColours
    
    def setAlpha(self, alpha):
        self.alpha = alpha
        return "Alpha set"
        # end setAlpha
        
    
