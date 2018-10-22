# -*- coding: utf-8 -*-  
import numpy as np

from grads import Grads

naqpConc = {
    "10102-43-9": ("NO"   , 30.0061),# NO
    "10102-44-0": ("NO2"  , 46.0055),# NO2
    "10028-15-6": ("O3"   , 48.0000),# O3
    "7782-77-6" : ("HONO" , 47.0100),# HNO2
    "630-08-0"  : ("CO"   , 28.0101),# CO
    "74-84-0"   : ("C2H6" , 30.0690),# C2H6
    "50-00-0"   : ("HCHO" , 30.0260),# CH2O 甲醛
    "75-07-0"   : ("ALD2" , 30.0260),# d021 乙醛
    "74-98-6"   : ("PAR"  , 44.1000),# c061 C5H12 烷烃类有机物
    "74-85-1"   : ("ETH"  , 28.0500),# C2H4 乙烯
    "590-18-1"  : ("OLEI" , 56.1063),# u041 # 双碳键: 间在中间
    "115-11-7"  : ("OLET" , 56.1063),# u042 # 双碳键，间在两边   
    "108-88-3"  : ("TOL"  , 92.1384),# r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165),# r081 二甲苯和其他多烷基芳香烃
    "78-79-5"   : ("ISOP" , 68.1170),# uu51 异戊二烯
    "2278-22-0" : ("PAN"  , 121.050),# p021 过氧乙酰硝酸酯
}

naqpEmis = {
    "10102-43-9": ("NO"   , 30.0061), # NO
    "10102-44-0": ("NO2"  , 46.0055), # NO2
    "7782-77-6" : ("HONO" , 47.0100), # HNO2
    "630-08-0"  : ("CO"   , 28.0101), # CO
    "74-85-1"   : ("C2H4" , 28.0500), # C2H4
    "74-84-0"   : ("C2H6" , 30.0690), # C2H6
    "75-07-0"   : ("ALD2" , 30.0260), # d021
    "110-54-3"  : ("PAR"  , 72.1488), # c061 C5H12 烷烃类有机物
    "108-88-3"  : ("TOL"  , 92.1384), # r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165), # r081 二甲苯和其他多烷基芳香烃
    "78-79-5"   : ("ISOP" , 68.1170), # uu51
    "590-18-1"  : ("OLEI" , 56.1063), # u041 # 双碳键: 间在中间
    "115-11-7"  : ("OLET" , 56.1063), # u042 # 双碳键，间在两边  
    "50-00-0"   : ("HCHO" , 30.0260), # CH2O
    "67-56-1"   : ("MEOH" , 32.0420), # o011
    "71-23-8"   : ("ANOL" , 102.180), # o031
    "80-56-8"   : ("TERP" , 136.234), # t0A1
}

cmaqEmis = {
    "10102-43-9": ("NO"   , 30.0061), # NO
    "10102-44-0": ("NO2"  , 46.0055), # NO2
    "75-07-0"   : ("ALD2" , 30.0260), # d021
    "630-08-0"  : ("CO"   , 28.0101), # CO
    "74-85-1"   : ("ETH"  , 28.0500), # C2H4
    "50-00-0"   : ("FORM" , 30.0260), # CH2O
    "78-79-5"   : ("ISOP" , 68.1170), # uu51
    "115-11-7"  : ("OLE"  , 56.1063), # u042
    "590-18-1"  : ("IOLE" , 56.1063), # u041    
    "110-54-3"  : ("PAR"  , 72.1488), # c061 C5H12 烷烃类有机物
    "80-56-8"   : ("TERP" , 136.234), # t0A1
    "108-88-3"  : ("TOL"  , 92.1384), # r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165), # r081 二甲苯和其他多烷基芳香烃
    "67-56-1"   : ("MEOH" , 32.0420), # o011
    "64-17-5"   : ("ETOH" , 46.0700), # o021
    "74-84-0"   : ("ETHA" , 30.0690), # C2H6
    "123-38-6"  : ("ALDX" , 58.0800), # d031
}

cmaqConc = {
    "10102-43-9": ("NO"   , 30.0061), # NO
    "10102-44-0": ("NO2"  , 46.0055), # NO2
    "10028-15-6": ("O3"   , 48.0000), # O3
    "7782-77-6" : ("HONO" , 47.0100), # HNO2
    "50-00-0"   : ("FORM" , 30.0260), # CH2O    
    "75-07-0"   : ("ALD2" , 30.0260), # d021
    "123-38-6"  : ("ALDX" , 58.0800), # d031
    "630-08-0"  : ("CO"   , 28.0101), # CO
    "2278-22-0" : ("PAN"  , 121.050), # p021 过氧乙酰硝酸酯
    "74-98-6"   : ("PAR"  , 44.1000), # c061 C5H12 烷烃类有机物
    "115-11-7"  : ("OLE"  , 56.1063), # u042
    "590-18-1"  : ("IOLE" , 56.1063), # u041   
    "80-56-8"   : ("TERP" , 136.234), # t0A1
    "108-88-3"  : ("TOL"  , 92.1384), # r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165), # r081 二甲苯和其他多烷基芳香烃
    "67-56-1"   : ("MEOH" , 32.0420), # o011
    "64-17-5"   : ("ETOH" , 46.0700), # o021
    "74-84-0"   : ("ETHA" , 30.0690), # C2H6
    "74-85-1"   : ("ETH"  , 28.0500), # C2H4
    "78-79-5"   : ("ISOP" , 68.1170), # uu51
}

def getNaqp(chemLst, outLst, citys, lat2d, lon2d, metafile, metaDic, factor= None):
    data = {}
    cityNames = list( citys.keys() )
    lons = [citys[name][0] for name in cityNames]
    lats = [citys[name][1] for name in cityNames]
    for fileName in chemLst:
        grd = Grads(metafile, fileName)
        #import pdb; pdb.set_trace()
        for cas in metaDic:
            gird = grd.get(metaDic[cas][0])[0,:,:]
            points = grid2points( lat2d, lon2d, gird, lats, lons )
            #import pdb; pdb.set_trace() 
            for name in cityNames:
                if factor:
                    point = points[cityNames.index(name)]*metaDic[cas][1]*factor
                else:
                    point = points[cityNames.index(name)]
                data.setdefault(name,{}).setdefault(cas,[]).append(point)
    for city in cityNames:
        outName = [name for name in outLst if city in name][0]
        writeMeanConc(outName, data[city])

def getNaqpConc(chemLst, outLst, citys, lat2d, lon2d, metafile ):
    factor = 0.04464 # ppb -->ug/m^3
    getNaqp(chemLst, outLst, citys, lat2d, lon2d, metafile, naqpConc, factor = factor)

def getNaqpEmis(chemLst, outLst, citys, lat2d, lon2d, metafile ):
    getNaqp(chemLst, outLst, citys, lat2d, lon2d, metafile, naqpEmis)

def getCmaq(chemFile, outLst, citys, lat2d, lon2d, metaDic, forTime, factor= None):
    import numpy as np
    import xarray as xr
    from datetime import timedelta
    data = {}
    cityNames = list( citys.keys() )
    lons = [citys[name][0] for name in cityNames]
    lats = [citys[name][1] for name in cityNames]
    girdData = xr.open_dataset(chemFile)
    time = list( girdData["TFLAG"].values[:,1,0] + girdData["TFLAG"].values[:,1,1]*1000 )
    for cas in metaDic:
        for itime in [forTime + timedelta(hours=i-8) for i in range(24)]:
            ind = int(itime.strftime("%Y%j")) + int(itime.strftime("%H%M%S"))*1000
            ind = time.index(ind)   
            gird = girdData[metaDic[cas][0]].values[ind,0,:,:]
            points = grid2points( lat2d, lon2d, gird, lats, lons )
            for name in cityNames:
                if factor:
                    area = girdData.attrs["XCELL"]*girdData.attrs["YCELL"]
                    point = points[cityNames.index(name)]*metaDic[cas][1]*factor/area
                    #import pdb; pdb.set_trace()
                else:
                    point = points[cityNames.index(name)]*metaDic[cas][1]*44.64 # ppm --> ug/m^3
                data.setdefault(name,{}).setdefault(cas,[]).append(point)
    for city in cityNames:
        outName = [name for name in outLst if city in name][0]
        writeMeanConc(outName, data[city])

def getCmaqEmis(chemFile, outLst, citys, lat2d, lon2d, forTime):
    getCmaq(chemFile, outLst, citys, lat2d, lon2d, cmaqEmis, forTime, factor=1e6)

def getCmaqConc(chemFile, outLst, citys, lat2d, lon2d, forTime):
    getCmaq(chemFile, outLst, citys, lat2d, lon2d, cmaqConc, forTime)

def writeMeanConc(fileName, data):
    hours = " ".join( [ str(i).zfill(2).ljust(7) for i in range(24)] )
    with open(fileName,"w") as file:
        file.writelines( "time".ljust(12) + hours +"\n" )
        for cas in data:
            try:
                forStr = "%10.4f" if cas != "630-08-0" else "%10.2f"
                line =  cas.ljust(12) + " ".join( [ (forStr % i) for i in data[cas] ] ) +"\n"
                file.writelines( line )
            except Exception as err:
                pass

def grid2points( lat2d, lon2d, gird, lats, lons ):
    from scipy.interpolate import griddata 
    points = np.stack( (lon2d.flatten(), lat2d.flatten()) ,axis=1)
    pntvalue = griddata(points, gird.flatten(), (lons, lats), method='linear') # nearest 
    return pntvalue
