import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pld

def plot_tangents():
    '''
    TODO Add documentation here
    '''
    points = pd.read_csv("../data/2025.02.11_cell_32.5_cm", header=None)

    xpoints = np.arange(points[1].size)
    ypoints = points[1]

    y_max_ind = pld.find_ind_of_min_or_max(ypoints, pld.operator.gt)

    ypoints = ypoints[:y_max_ind]

    tans = np.zeros(y_max_ind-1, dtype=int)
    for i in range(1, y_max_ind-1):
        tans[i] = ypoints[i]/i

    plt.plot(np.arange(1, y_max_ind), tans)
    plt.show()

if __name__ == "__main__":
    plot_tangents()