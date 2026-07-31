import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-40, 40, 100)

print(x.size)

y = np.sin(x)
print(y.size)

# the library that we are going to plot the graph is matplotlib, we have to import it first, then we can use the plot function to plot the graph.

# to print the output graph on screen
# plt.plot(x, y)
# plt.show()

y = x*x+2*x+6
plt.plot(x, y)
plt.show()