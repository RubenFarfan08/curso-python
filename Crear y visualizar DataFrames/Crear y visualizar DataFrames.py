# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd

# Read in the avocados dataset, parse the date column
avocados= pd.read_csv("avocados.csv", parse_dates=["date"])

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar', 
                    xlabel='Tamaño del aguacate',
                    ylabel='Total vendido',
                    title='Aguacates vendidos por tamaño',
                    color='green',
                    rot=0)

# Show the plot
plt.show()

# segundo ejercicio-------------------------------------------------------------------------------------------
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='bar', 
                    xlabel='Fecha',
                    ylabel='Total vendido',
                    title='Aguacates vendidos por Fecha',
                    color='green',
                    rot=45)

# Show the plot
plt.show()
#-------------------------------------------------------------------------------------------------------------
#Tercer ejercicio---------------------------------------------------------------------------------------------
#Los gráficos de dispersión son ideales para visualizar relaciones entre variables numéricas. 
# En este ejercicio, compararás el número de aguacates vendidos con el precio medio y verás si están relacionados. 
# Si están relacionados, puedes utilizar un número para predecir el otro.
# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", 
    y="avg_price", 
    kind="scatter", 
    xlabel='Total vendido',
    ylabel='Precio Medio',
    title='Number of avocados sold vs. average price',
    color='green' )

# Show the plot
plt.show()

#cuarto ejercicio---------------------------------------------------------------------------------------------

# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.7)

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.7)

# Add a legend
plt.legend(["conventional","organic"])

# Show the plot
plt.show()

# quinto ejercicio---------------------------------------------------------------------------------------------
# Histogram of conventional avg_price with alpha and bins

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

#detecting missing values
avocados.isnull().any()

#counting missing values
missing_values = avocados.isnull().sum()

#plot missing values
missing_values.plot(kind='bar', 
                    xlabel='Columnas',
                    ylabel='Valores faltantes',
                    title='Valores faltantes en el DataFrame de aguacates',
                    color='orange')

# Check each column for missing values
print(avocados.isnull().any())

#remove missing values
avocados_cleaned = avocados.dropna()

#replace missing values with 0
avocados_filled = avocados.fillna(0)

#Imprime un DataFrame que muestre si falta o no cada valor de avocados
print(avocados.isnull().astype(int))

#primer ejercicio encuentra valores faltantes.
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
avocados_2016 = avocados[avocados["date"].dt.year == 2016]
# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar', 
                    xlabel='Columnas',
                    ylabel='Valores faltantes',
                    title='Valores faltantes en el DataFrame de aguacates',
                    color='orange')

# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

#example of dictionary
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2025-06-11", "small_sold": 15, "large_sold": 20},
    {"date": "2025-06-10", "small_sold": 25, "large_sold": 200},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135,6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)
# Print the new DataFrame
print(avocados_2019)

# Ejercicios de csv a dataframe
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())

# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped","total_passengers"]].agg(sum)
# Calcular pasajeros accidentados por 10k
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)

# ordena airline_totals por bumps_per_10k de mayor a menor
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")