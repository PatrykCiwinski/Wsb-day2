import pandas as pd
df=pd.read_csv("cities.csv", skipinitialspace = True)
# print(list(df))
city_name=df["City"]
sait_cities_list=[name for name in city_name if name.startswith("Santa ") or name.startswith("Saint ") or name.startswith("San ")]
print(len(sait_cities_list))

print(sait_cities_list)
