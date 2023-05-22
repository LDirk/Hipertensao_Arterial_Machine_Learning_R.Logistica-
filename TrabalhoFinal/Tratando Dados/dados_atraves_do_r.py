library(progress)
library(PNSIBGE)
library(readr)

dadosPNS <- get_pns(year=2019, vars=c(
"V0001",
"V0026",
"C006",
"C008",
"C009",
"D001",
"D00901", 
"N004",
"N005",
"N010",
"N011",
"P00104",
"P00404",
"P01001",
"P019",
"P02002",
"P02102",
"P034",
"P035",
"P038",
"P039",
"P03905",
"P040",
"P050",
"P051",
"P05402",
"Q00201",
"Q03001",
"Q060",
"Q06306",
"Q068",
"Q124"), design=FALSE)

colunas_interesse <- c("V0001","V0026","C006","C008","C009","D001","D00901", "N004","N005","N010","N011","P00104","P00404","P01001","P019","P02002","P02102","P034","P035","P038","P039","P03905","P040","P050","P051","P05402","Q060","Q00201","Q03001","Q06306","Q068","Q124")

df_interesse <- dadosPNS[colunas_interesse]

write_csv(df_interesse, "dataframe.csv")
