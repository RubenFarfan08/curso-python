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
# Create a dictionary with the data
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

