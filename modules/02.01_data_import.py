# 02.01 - data import

# sf open data portal - sfpd reports (2003-2018)
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
# df_data = read_data("data/sfpd_report_2003-18.csv")

# note: reduce original file (500mb) by subset first 10k rows and replace file
# https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
# df_data = df_data[0:10000]
# output_result(df_data, "data/sfpd_report_2003-18.csv")

# read in reduced file after processing steps above
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
df_sfpd = read_data("data/sfpd_report_2003-18.csv")

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
df_school = read_data("data/ca_school_2019-20.csv")

# sacog - lihm community dataset (2016)
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0
sacog_lihm_csv = read_data("data/sacog_lihm_areas_2016.csv")

# ca open data - covid homeless impact
# https://data.ca.gov/dataset/covid-19-homeless-impact/resource/235466b6-0eb9-4ff7-a4b4-8138f474ce83
ca_covid_homeless_csv = read_data("data/homeless_impact.csv")

# ca geoportal - county boundary
# https://gis.data.ca.gov/datasets/CALFIRE-Forestry::california-county-boundaries/data?geometry=-152.378%2C31.049%2C-85.626%2C43.258
ca_county_csv = read_data("data/California_Counties.csv")

# verify data import
# data_profile(ca_covid_homeless_csv, "ca covid homeless")
# data_profile(ca_county_csv, "ca county")
# print(ca_covid_homeless_csv.head(5), '\n')
# print(ca_county_csv.head(5), '\n')
