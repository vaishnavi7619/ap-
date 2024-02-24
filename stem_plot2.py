import numpy as np
import matplotlib.pyplot as plt

# Define the stem plot function
def stem_plot(x, y, title):
    plt.stem(x, y)
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Define the stem plot data
n = np.arange(0, 30)
x_n = 7.5 * (1/2)*n + 9 * n * (1/2)*n
stem_plot
