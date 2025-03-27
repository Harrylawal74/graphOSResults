import matplotlib.pyplot as plt
import numpy as np

# Sample x and y values
x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

# Create a plot and add a table
fig, ax = plt.subplots()

# Hide the axes
ax.axis('tight')
ax.axis('off')

# Create the table
table_data = list(zip(x, y))
table = ax.table(cellText=table_data, colLabels=['x', 'y'], loc='center')

# Show the plot
plt.show()