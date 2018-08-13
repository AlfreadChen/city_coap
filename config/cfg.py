# Chemical Conditions
chemType = "conc" # emis, conc
chemModl = "naqp" # naqp, cmaq, camx, wrfc
#chemName = "/public/city_henan/data/output/emis/emis.total.{simTime}.d1"
#chemMeta = "/public/home/model/zhangwd/em_v9/emis.total.201505.d1.ctl"

chemName = "/public/city_henan/data/output/naqpms/{wrfTime}/out/data/{begTime}/testd1.{simTime}.grd"
chemMeta = "/public/city_henan/data/output/naqpms/{wrfTime}/out/data/testd1.{begTime}.ctl"

# MetaData
gridData = "/public/city/data/input/datagrid/grid.d1"
gridMeta = "/public/city/data/input/datagrid/grid.d1.ctl"

# number of forecast days
foreDays = 7

# stations of simulation 
citys = {
    "zhengzhou":[120.4625, 36.1067],
}
