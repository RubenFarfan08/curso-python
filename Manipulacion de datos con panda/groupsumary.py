import pandas as pd
dogs = pd.read_csv("dogs.csv", parse_dates=["date"])
sales = pd.read_csv("sales.csv", parse_dates=["date"])


#grouped summaries
dogs.groupby("color")["weight_kg"].mean()
dogs.groupby("color")["weight_kg"].agg([min,max,sum])
dogs.groupby(["color","breed"])["weight_kg"].mean()


# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

#Agrupa sales por "type", toma la suma de "weekly_sales" y almacénala como sales_by_type.
#Calcula la proporción de ventas en cada tipo de tienda dividiendo por la suma de sales_by_type. Asigna a sales_propn_by_type.

 # Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales["weekly_sales"])
print(sales_propn_by_type)

#Agrupa sales por "type" y "is_holiday", toma la suma de weekly_sales y almacénala como sales_by_type_is_holiday.
# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type","is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)


""" Importa numpy con el alias np.
Obtén el mínimo, el máximo, la media y la mediana de weekly_sales para cada tipo de tienda utilizando .groupby() y .agg(). Guárdalo como sales_stats. 
¡Asegúrate de utilizar las funciones de numpy!
Obtén el mínimo, el máximo, la media y la mediana de unemployment y fuel_price_usd_per_l para cada tipo de tienda. Guárdalo como unemp_fuel_stats. """
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


#Pivot Tables
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median])

dogs.pivot_table(values="weight_kg", index="color", columns="breed") 
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0) #agrega los 0
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0, margins=True) #agrega una columna all y manda la media de todos los valores, sin incluir los faltantes

""" Dinamizar sobre una variable
Las tablas dinámicas son la forma estándar de agregar datos en las hojas de cálculo.

En pandas, las tablas dinámicas son esencialmente otra forma de realizar cálculos agrupados. Es decir, el método .pivot_table() es una alternativa a .groupby().

En este ejercicio, realizarás cálculos utilizando .pivot_table() para reproducir los cálculos que realizaste en la lección anterior utilizando .groupby().

sales está disponible y pandas se importa como pd. """

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(
    values="weekly_sales", 
    index="type",          # Filas: categorías de tienda (A, B, etc.)
    columns="is_holiday",  # Columnas: ¿es día festivo? (True/False)
    aggfunc="mean"         # Calcula la media de ventas
)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)


# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="type", columns="department", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type",  fill_value=0, margins=True))

#Columns and index
dogs.columns
dogs.index

#setting a column as the index
dogs_ind = dogs.set_index("name")
