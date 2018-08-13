import os
import sys
from optparse import OptionParser
from datetime import datetime, timedelta

prjHome = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
outDir  = prjHome + os.sep + "data" + os.sep + "{model}" + os.sep + "{date}" +  os.sep
outName = "{city}_{time}_chem.txt"

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

def main(): 
    # get time;
    parser  = OptionParser()
    parser.add_option("-t", "--time", dest="thisTime", help="China Standard Time")
    options, args = parser.parse_args()
    thisTime = datetime.strptime(options.thisTime,"%Y%m%d")
    
    # configure;
    config = loadConfig( configFile = prjHome+os.sep+"config"+os.sep+"cfg.py")

    strTime = thisTime.strftime("%Y%m%d")
    outPath = outDir.format(model=config.chemModl, date=strTime)   
    if not os.path.exists(outPath): 
        os.makedirs(outPath)  

    for itime in ( thisTime + timedelta(hours=24*i) for i in range(config.foreDays) ):
        getChem(config.chemModl, config.chemType, thisTime, itime, config.chemName, outPath + outName, config.citys, config.gridData, config.gridMeta, config.chemMeta)

def getChem(chemModl, chemType, nowTime, forTime, chemName, outName, citys, gridData, gridMeta, chemMeta=None):
    # check output
    cstTime = forTime.strftime("%Y%m%d")
    outLst = [outName.format(city=name, time=cstTime) for name in citys]
    if all( os.path.exists(file) for file in outLst ): 
        return True

    # check input
    nowTime -= timedelta(hours=8)
    wrfTime = (nowTime - timedelta(hours=4) ).strftime("%Y%m%d%H")
    begTime = (nowTime - timedelta(hours=3) ).strftime("%Y%m%d%H")
    chemMeta = chemMeta.format(wrfTime=wrfTime, begTime=begTime)
    timeLst = (forTime+timedelta(hours=i) for i in range(24))
    chemLst = [chemName.format(wrfTime=wrfTime, begTime=begTime, simTime=itime.strftime("%Y%m%d%H")) for itime in timeLst]  
    print(chemLst)
    if not all( os.path.exists(file) for file in chemLst ):
        return True   
        
    # get function  
    funcName = "get{model}{type}".format(model=chemModl.capitalize(),type=chemType.capitalize()) 
    import interface
    try:
        func = getattr(interface, funcName )
    except Exception as err:
        print(err)
        print("Given wrong type or model name")
        sys.exit(1)   

    if chemModl == "naqp":
        from grads import Grads
        grd = Grads(gridMeta, gridData)
        lat2d = grd.get("XLAT")[0,:,:]
        lon2d = grd.get("XLONG")[0,:,:]
        func(chemLst, outLst, citys, lat2d, lon2d, chemMeta)
    if chemModl == "cmap":
        from grads import Grads
        grd = Grads(gridMeta, gridData)
        lat2d = grd.get("XLAT")[0,:,:]
        lon2d = grd.get("XLONG")[0,:,:]
        lat2d = lat2d[1:-1,1:-1]    
        lon2d = lon2d[1:-1,1:-1]       
        func(chemLst[0], outLst, citys, lat2d, lon2d)
    
if __name__ == "__main__":
    main()
