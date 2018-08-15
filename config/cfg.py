# Chemical Conditions
chemType = "emis" # emis, conc
chemModl = "naqp" # naqp, cmaq, camx, wrfc

chemName = "/public/city_henan/data/output/emis/emis.total.{simTime}.d1"
chemMeta = "/public/home/model/zhangwd/em_v9/emis.total.201505.d1.ctl"

#chemName = "/public/city_henan/data/output/naqpms/{wrfTime}/out/data/{begTime}/testd1.{simTime}.grd"
#chemMeta = "/public/city_henan/data/output/naqpms/{wrfTime}/out/data/testd1.{begTime}.ctl"

# MetaData
gridData = "/public/city/data/input/datagrid/grid.d1"
gridMeta = "/public/city/data/input/datagrid/grid.d1.ctl"

# number of forecast days
foreDays = 6

# stations of simulation 
citys = {
    "nanjing"    :[118.74593, 32.04278],
    "shengzhan"  :[118.74583, 32.04278],
    "suzhou"     :[120.60, 31.30],
    "nantong"    :[120.86, 32.01],
    "lianyungang":[119.22, 34.60],
    "yangzhou"   :[119.42, 32.39],
    "zhenjiang"  :[119.27, 32.12],
    "suqian"     :[118.30, 33.96],
}
