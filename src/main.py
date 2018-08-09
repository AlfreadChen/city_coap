import os
from datetime, import datetime, timedelta

prjHome = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
outPath = prjHome + os.sep + "data" + os.sep + "{model}" + os.sep + "{date}" +  os.sep
outName = "{city}_{time}_chem.txt"

def main(): 
    # get time;
    parser  = OptionParser()
    parser.add_option("-t", "--time", dest="thisTime", help="China Standard Time")
    options, args = parser.parse_args()
    thisTime = datetime.strptime(options.thisTime,"%Y%m%d")
    
    # configure;
    config = loadConfig( configFile = prjHome+os.sep+"config"+os.sep+"cfg.py")

    for itime in ( thisTime + timedelta(hours=24*i) for i in range(foreDays.foreDays) ):
        strTime = itime.strftime("%Y%m%d")
        outPath = outPath.foramt(model=config.chemModl, date=strTime)   
        if not os.path.exists(outPath): 
            os.makedirs(outPath)  
        getConc(config.chemModl, config.chemType, itime, config.chemName, 
        outPath + outName, config.citys, config.metafile, config.gridData, config.gridMeta)

def getConc(chemModl, chemType, nowTime, chemName, outName, citys, gridData, gridMeta, metafile=None):
    # check output
    cstTime = nowTime.strftime("%Y%m%d")
    outLst = (outName.foramt(city=name, time=cstTime) for name in citys)
    if all( os.path.exists(file) for file in outLst ): 
        return True
    # check input
    nowTime -= timedelta(hours=8)
    utcTime = nowTime.strftime("%Y%m%d")
    timeLst = (nowTime+timedelta(hours=i) for i in range(24))
    chemLst = (chemName.foramt(begTime=utcTime,simTime=itime.strftime("%Y%m%d%H")) for itime in timeLst)  
    if not all( os.path.exists(file) for file in chemLst ):
        return True   
    
    # get function  
    funcName = "get{}{}".format(chemModl.capitalize(),chemType.capitalize())
    try:
        import interface
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
        func(chemLst, outLst, citys, lat2d, lon2d, metafile)
    if chemModl == "cmap":
        from grads import Grads
        grd = Grads(gridMeta, gridData)
        lat2d = grd.get("XLAT")[0,:,:]
        lon2d = grd.get("XLONG")[0,:,:]
        lat2d = lat2d[1:-1]    
        lon2d = lon2d[1:-1]       
        func(chemLst[0], outLst, citys, lat2d, lon2d)
    

