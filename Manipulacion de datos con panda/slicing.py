#Segmentar y subconjuntar con .loc e .iloc
import pandas as pd
dogs = pd.read_csv("dogs.csv", parse_dates=["date"])
temperatures= pd.read_csv("temperatures.csv", parse_dates=["date"])
temperatures_ind = temperatures.set_index("city")
breeds=["labrador","Poodle","Chow Chow", "schanuzer","labrador","chihuahua","st bernador"]
print(breeds[2:5])
print(breeds[:3])
print(breeds[3:])

dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
print(dogs_srt)

#slicing the outer index level

dogs_srt.loc["Chow Chow":"Poodle"]

dogs_srt.loc[("Labrador","Brown"):("schanuzer","Grey")]

#slicing columns
dogs_srt.loc[:"name":"height_cm"]

#slice twice
dogs_srt.loc[("Labrador","Brown"):("schanuzer","Grey"),"name":"height_cm"]

#subconjuntar por fecha
dogs = dogs.set_index("date_of_birth").sort_index()
print(dogs)

#Slicing by dates
dogs.loc["2014-08-25":"2016-09-16"]
#slicing by partial date
dogs.loc["2024":"2026"]
#segmentar por numero de fila / columna
print(dogs.iloc[2:5,1:4])


# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])


# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), 'date':'avg_temp_c'])

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

""" Utiliza .iloc[] en temperatures para tomar subconjuntos.
Obtén la fila 23, columna 2 (posiciones índice 22 y 1).
Obtén las 5 primeras filas (posiciones de índice 0 a 5).
Obtén todas las filas, columnas 3 y 4 (posiciones de índice 2 a 4).
Obtén las 5 primeras filas, columnas 3 y 4. """

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])


temperatures["year"] = temperatures["date"].dt.year
# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    values='avg_temp_c',    # Columna a promediar
    index=['country', 'city'],  # Filas jerárquicas
    columns='year',         # Columnas por año
    aggfunc='mean'          # Función de agregación (promedio por defecto)
)

# See the result
print(temp_by_country_city_vs_year)



# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"), 2005:2010]


# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis=1)

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])