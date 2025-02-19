import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import operator

def find_ind_of_min_or_max(arr, op):
    sought_for = arr[0]
    sought_for_ind = 0
    ind = 0
    for elem in arr:
        if op(elem, sought_for):
            sought_for = elem
            sought_for_ind = ind
        ind += 1
    return sought_for_ind

def plot_linear_dependence_and_min_max_points_of_signal():
    '''
    TODO Add documentation here
    '''
    points = pd.read_csv("../data/2025.02.11_cell_32.5_cm", header=None)

    xpoints = np.arange(points[1].size)
    ypoints = points[1]

    y_max_ind = find_ind_of_min_or_max(ypoints, operator.gt)

    plt.plot(xpoints, ypoints)
    plt.plot(y_max_ind, ypoints[y_max_ind], 'ro')
    plt.plot(0, ypoints[0], 'ro')
    plt.plot([0, y_max_ind], [ypoints[0], ypoints[y_max_ind]])
    plt.show()

if __name__ == "__main__":
    plot_linear_dependence_and_min_max_points_of_signal()
