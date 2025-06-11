# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados["size"].value_counts()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar", title="avocados sold by size")

# Show the plot
plt.show()