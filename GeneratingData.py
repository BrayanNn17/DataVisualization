import matplotlib.pyplot as plt
from RandomWalk import RandomWalk
# Keep making new walks, as long as the program is active.

rw = RandomWalk(5000)
rw.fill_walk()
 
 # Plot the points, and show the plot.
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=1)
plt.show()
