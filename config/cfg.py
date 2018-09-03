# Chemical Conditions
chemType = "conc" # emis, conc
chemModl = "naqp" # naqp, cmaq

#chemName = "/p200/js2/city_cmaq_js2/data/output/emis/D2/EM_D2_{time}.ncf" # 201827312
#chemName = "/p200/js2/city_cmaq_js2/data/output/cctm/D2/CCTM_CONC_D2_{time}.ncf" # 2018082912

#chemName = "/p200/js2/city_js2/data/output/emis/emis.total.{simTime}.d2"
#chemMeta = "/p200/js2/city_js2/data/input/em_sample/emis.total.201501.d2.ctl"

chemName = "/p200/js2/city_js2/data/output/naqpms/{wrfTime}/out/data/{begTime}/testd2.{simTime}.grd"
chemMeta = "/p200/js2/city_js2/data/output/naqpms/{wrfTime}/out/data/testd2.{begTime}.ctl"

# MetaData
gridData = "/p200/js2/city_js2/data/input/datagrid/grid.d2"
gridMeta = "/p200/js2/city_js2/data/input/datagrid/grid.d2.ctl"

# number of forecast days
foreDays = 3

# stations of simulation 
citys = {
    "nanjing"    :[118.74593, 32.04278],
    #"shengzhan"  :[118.74583, 32.04278],
    #"suzhou"     :[120.60, 31.30],
    #"nantong"    :[120.86, 32.01],
    #"lianyungang":[119.22, 34.60],
    #"yangzhou"   :[119.42, 32.39],
    #"zhenjiang"  :[119.27, 32.12],
    #"suqian"     :[118.30, 33.96],
}
