# Chemical Conditions
chemType = "conc" # emis, conc
chemModl = "naqp" # naqp, cmaq

#chemName = "/p200/js2/city_cmaq_js2/data/output/emis/D2/EM_D2_{time}.ncf"
#chemName = "/p200/js2/city_cmaq_js2/data/output/cctm/D2/CCTM_CONC_D2_{time}.ncf"

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
    "beijing"  : [116.19 , 39.55,  ],
    "wuhan"    : [114.886, 30.452, ],
    "zhengzhou": [113.605, 37.748, ],
}
