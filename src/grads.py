import numpy as np
from collections import namedtuple

class CtlMeta:
    ''' 
    example: 
       ctl = CtlMeta("a.ctl")
       ctl.dx
       ctl.dy
       ctl.vars[""].rec
       ctl.vars[""].dz
    '''
    def __init__(self, ctlFile: str):
        self._parser(ctlFile)

    def _parser(self,ctlFile):
        self.vars = {}
        infoDic = {}
        varsLst = []
        with open(ctlFile,"r") as file:
            for line in file:
                line = line.strip()
                if line[:1].isalpha():
                    cols = line.split()         
                    varsLst.append(cols[0].upper())
                    try:
                        infoDic[cols[0].upper()]=cols[1:]
                    except:
                        ...
        if  "PDEF" in infoDic.keys():
            self.nx=int(infoDic["PDEF"][0])
            self.ny=int(infoDic["PDEF"][1])
        else:
            self.nx=int(infoDic["XDEF"][0])
            self.ny=int(infoDic["YDEF"][0])

        recods = namedtuple("recods","rec  nz")    
        rec = (0,0) # conventionally the end of rec is not used
        for var in varsLst[varsLst.index("VARS")+1:varsLst.index("ENDVARS")]:
            nz  = int( infoDic[var][0] )
            if nz < 1: nz =1 
            rec = (rec[1], rec[1]+self.nx*self.ny*nz)
            self.vars[var] = recods(rec, nz)

class Grads:
    """
    example:
       grd = Grads("naqpd03.2018080616.ctl", "naqpd03.2018081316.grd")
       grd.get("T")
    """
    def __init__(self, ctlFile: str, rawFile: str):
        self.rawFile = rawFile
        self._ctl  = CtlMeta(ctlFile)
        self.nx = self._ctl.nx
        self.ny = self._ctl.ny        
        self.vars = self._ctl.vars 

    def get(self, name: str): -> numpy.array
        name = name.upper()
        nz = self.vars[name].nz
        beg, end = self.vars[name].rec
        data = np.memmap(self.rawFile, dtype=">f", mode="r", offset=beg*4, shape=end-beg)
        # ">f" : > 大小端问题; fortran direct and unformated 输出与C输出一样；
        return np.array(data).reshape(nz, self.ny, self.nx,)

if __name__ == "__main__":
    grd = Grads("naqpd01.2018080616.ctl", "naqpd01.2018081316.grd")
    t = grd.get("T")
    # import matplotlib.pyplot as plt  
    # fig, ax = plt.subplots()
    # ax.contourf( t[0,:,:], )
    # plt.show()