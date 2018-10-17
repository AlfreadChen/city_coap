'''
   description: business logic
'''

import os
import sys
import argparse
from datetime import datetime, timedelta

prjHome = "../"
outPath = prjHome + "data/{model}/{type}/{date}/"
txtName = "{city}_{time}_chem.txt"

def loadConfig(configFile):
    '''
    Description:
        A function to load a configure file which is writed in python
    Purpose:
        control the running style of program
    '''
    import types
    try:
        script = open(configFile).read()
        config = types.ModuleType("config")
        exec(script, config.__dict__)
    except Exception as err:
        print(err)
        sys.exit(1)
    return config

class GridInfo:
    """grid information of wrf"""
    def __init__(self, gridData, gridMeta,):
        import grads
        self.gridData = gridData
        self.gridMeta = gridMeta
        grd = grads.Grads(self.gridMeta, self.gridData)
        self.lat2d = grd.get("XLAT")[0, :, :]
        self.lon2d = grd.get("XLONG")[0, :, :]

class ChemInterface:
    """ Interface for extracting data"""
    def __init__(self, forTime, citys, outName, girdInfo, chemName):
        self.citys = citys
        self.forTime = forTime
        self.outName = outName
        self.girdInfo = girdInfo
        self.chemName = chemName

    def checkOutFiles(self):
        """ check output """
        self.outFiles = []
        for city in self.citys:
            file = self.outName.format(city=city, time=self.forTime.strftime("%Y%m%d"))
            if not os.path.exists(file):
                self.outFiles.append(file)

    def getInputFiles(self):
        ''' prepare the input file '''
        self.chemInputs = []

    def getGrib(self):
        ''' get station chem conc '''
        self.lat2d = self.girdInfo.lat2d
        self.lon2d = self.girdInfo.lon2d

    def getFunc(self, fName):
        import interface, grads
        try:
            func = getattr(interface, fName)
        except Exception as err:
            print("Given wrong type or model name")
            sys.exit(1)
        return func

    def extract(self, func):
        ...

    def run(self, fName):
        self.checkOutFiles()
        if self.outFiles:
            self.getInputFiles()
            if self.chemInputs:
                self.getGrib()
                func = self.getFunc(fName)
                self.extract(func)

class NaqpInterface(ChemInterface):
    """Naqp Interface"""
    def __init__(self, nowTime, chemMeta, *args):
        super(NaqpInterface, self).__init__(*args)
        self.nowTime = nowTime
        self.chemMeta = chemMeta

    def getInputFiles(self):
        ''' prepare the input file '''
        self.chemInputs = []
        wrfTime = (self.nowTime - timedelta(hours=12)).strftime("%Y%m%d%H")
        begTime = (self.nowTime - timedelta(hours=11)).strftime("%Y%m%d%H")
        self.chemMeta = self.chemMeta.format(wrfTime=wrfTime, begTime=begTime)

        for i in range(24):
            time = (self.forTime + timedelta(hours=i-8)).strftime("%Y%m%d%H")
            file = self.chemName.format(wrfTime=wrfTime, begTime=begTime, simTime=time)
            if not os.path.exists(file):
                self.chemInputs = []
                return
            else:
                self.chemInputs.append(file)

    def extract(self, func):
        func(self.chemInputs, self.outFiles, self.citys, self.lat2d, self.lon2d, self.chemMeta)

class CmaqInterface(ChemInterface):
    """Cmaq Interface"""
    def __init__(self, nowTime, chemType, *args):
        super(CmaqInterface, self).__init__(*args)
        self.nowTime = nowTime
        self.chemType = chemType

    def getInputFiles(self):
        cmqTime = self.nowTime - timedelta(hours=12)
        if self.chemType == "emis":
            strTime = cmqTime.strftime("%Y%j%H")
        else:
            strTime = cmqTime.strftime("%Y%m%d%H")
        chemInputs = self.chemName.format(time=strTime)
        self.chemInputs = None
        # import pdb; pdb.set_trace()
        if os.path.exists(chemInputs):
            self.chemInputs = chemInputs

    def extract(self, func):
        self.lat2d = self.lat2d[1:-1, 1:-1]
        self.lon2d = self.lon2d[1:-1, 1:-1]
        func(self.chemInputs, self.outFiles, self.citys, self.lat2d, self.lon2d, self.forTime)

def main():
    '''
        Description: main of this program
    '''
    # get time;
    parser = argparse.ArgumentParser(description='extract chem data')
    parser.add_argument('-t', '--thisTime', type=str, help='China Standard Time')
    args = parser.parse_args()
    strTime = args.thisTime
    thisTime = datetime.strptime(strTime, "%Y%m%d")

    # configure;
    config = loadConfig(prjHome+os.sep+"config"+os.sep+"cfg.py")
    outDir = outPath.format(model=config.chemModl, type=config.chemType, date=strTime)
    fName = "get{model}{type}".format(model=config.chemModl.capitalize(),
                                      type=config.chemType.capitalize())

    if not os.path.exists(outDir): os.makedirs(outDir)

    girdInfo = GridInfo(config.gridData, config.gridMeta,)
    for i in range(config.foreDays):
        forTime = thisTime + timedelta(hours=24*i)
        args = (forTime, config.citys, outDir+txtName, girdInfo, config.chemName)
        if config.chemModl == "naqp":
            interfacer = NaqpInterface(thisTime, config.chemMeta, *args)
        else:
            interfacer = CmaqInterface(thisTime, config.chemType, *args)
        interfacer.run(fName)

if __name__ == "__main__":
    main()
