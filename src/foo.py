import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    points = pd.read_csv("../data/2025.02.11_cell_32.5_cm", header=None)
    
    xpoints1 = np.arange(points[1].size)
    ypoints1 = points[1]

    plt.plot(xpoints1, ypoints1)
    plt.show()
