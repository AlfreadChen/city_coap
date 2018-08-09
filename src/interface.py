from grads import Grads

naqpConc = {
    "10028-15-6": ("O3"   , 48.0000),# O3
    "7782-77-6" : ("HONO" , 47.0100),# HNO2
    "10102-43-9": ("NO"   , 30.0061),# NO
    "10102-44-0": ("NO2"  , 46.0055),# NO2
    "630-08-0"  : ("CO"   , 28.0101),# CO
    "74-84-0"   : ("C2H6" , 30.0690),# C2H6
    "75-07-0"   : ("ALD2" , 30.0260),# d021
    "110-54-3"  : ("PAR"  , 72.1488),# c061 C5H12 烷烃类有机物
    "74-85-1"   : ("ETH"  , 28.0500),# C2H4
    "108-88-3"  : ("TOL"  , 92.1384),# r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165),# r081 二甲苯和其他多烷基芳香烃
    "78-79-5"   : ("ISOP" , 68.1170),# uu51
    "115-11-7"  : ("OLEI" , 56.1063),# u042
    "590-18-1"  : ("OLET" , 56.1063),# u041
    "50-00-0"   : ("HCHO" , 30.0260),# CH2O
}

naqpEmis = {
    "10102-43-9": ("NO"   , 30.0061), # NO
    "10102-44-0": ("NO2"  , 46.0055), # NO2
    "630-08-0"  : ("CO"   , 28.0101), # CO
    "74-84-0"   : ("C2H6" , 30.0690), # C2H6
    "75-07-0"   : ("ALD2" , 30.0260), # d021
    "110-54-3"  : ("PAR"  , 72.1488), # c061 C5H12 烷烃类有机物
    "74-85-1"   : ("ETH"  , 28.0500), # C2H4
    "108-88-3"  : ("TOL"  , 92.1384), # r071 甲苯和其他单烷基芳香烃
    "95-47-6"   : ("XYL"  , 106.165), # r081 二甲苯和其他多烷基芳香烃
    "78-79-5"   : ("ISOP" , 68.1170), # uu51
    "115-11-7"  : ("OLEI" , 56.1063), # u042
    "590-18-1"  : ("OLET" , 56.1063), # u041
    "50-00-0"   : ("HCHO" , 30.0260), # CH2O
    "67-56-1"   : ("MEOH" , 32.0420), # o011
    "71-23-8"   : ("ANOL" , 102.180), # o031
    "80-56-8"   : ("TERP" , 136.234), # t0A1
}

def getNaqpConc(chemLst, outLst, citys, lat2d=None, lon2d=None, metafile=None ):
    data = {}
    cityNames = list( citys.keys() )
    lons = [city[name][1] for name in cityNames]
    lats = [city[name][1] for name in cityNames]
    for fileName in chemLst:
        grd = Grads(metafile, fileName)
        for cas in naqpConc:
            gird = grd.get(naqpConc[cas][0])[0,:,:]
            points = grid2points( lat2d, lon2d, gird, lats, lons )
            for name in cityNames:
                point = points[cityNames.index(name)]*naqpConc[cas][1]*1e-3*40.9
                data.setdefualt({},cityNames).setdefualt([],cas).append(point)
    for city in cityNames:
        outName = [name for name in outLst if city in  name][0]
        writeMeanConc(fileName, data[city])

def getNaqpEmis(chemLst, outLst, citys, lat2d=None, lon2d=None, metafile=None ):
    data = {}
    cityNames = list( citys.keys() )
    lons = [city[name][1] for name in cityNames]
    lats = [city[name][1] for name in cityNames]
    for fileName in chemLst:
        grd = Grads(metafile, fileName)
        for cas in naqpEmis:
            gird = grd.get(naqpEmis[cas][0])[0,:,:]
            points = grid2points( lat2d, lon2d, gird, lats, lons )
            for name in cityNames:
                point = points[cityNames.index(name)]
                data.setdefualt({},cityNames).setdefualt([],cas).append(point)
    for city in cityNames:
        outName = [name for name in outLst if city in  name][0]
        writeMeanConc(fileName, data[city])


def writeMeanConc(fileName, data):
    hours = " ".join( [ str(i).zfill(2).ljust(7) for i in range(24)] )
    with open(fileName,"w") as file:
        file.writelines( "time".ljust(12) + hours +"\n" )
        for cas in data:
            try:
                line =  cas.ljust(12) + " ".join( [ ("%10.2f" % i) for i in data[cas] ] ) +"\n"
                file.writelines( line )
            except Exception as err:
                pass

def grid2points( lat2d, lon2d, gird, lats, lons ):
    from scipy.interpolate import griddata 
    points = np.stack( (lon2d.flatten(), lat2d.flatten()) ,axis=1)
    pntvalue = griddata(points, gird.flatten(), (lons, lats), method='nearest') # 
    return pntvalue
