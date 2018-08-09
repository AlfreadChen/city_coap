# Chemical Conditions
chemType = "conc" # emis, conc
chemModl = "naqp" # naqp, cmaq, camx, wrfc
chemName = "/public/post/forecast/model/naqpms/hourly/{begTime}/naqpd01.{simTime}.grd" 
chemMeta = "/public/post/forecast/model/naqpms/hourly/naqpd01.{begTime}.ctl"

# MetaData
gridData = "/public/post/datagrid/wrfd01.dat"
gridMeta = "/public/post/datagrid/wrfd01.ctl"

# number of forecast days
foreDays = 7

# stations of simulation 
citys = {
    "zhengzhou":[120.4625, 36.1067],
}


