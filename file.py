import matplotlib.pyplot as plt

# Create some example data
x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Plot the data
plt.plot(x_data, y_data)

# Set the gap between tick marks on the x and y axes to 2
gap = 2
plt.xticks(range(min(x_data), max(x_data) + 1, gap))
plt.yticks(range(min(y_data), max(y_data) + 1, gap))

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with a Gap of 2 between Tick Marks')

# Show the plot
plt.show()