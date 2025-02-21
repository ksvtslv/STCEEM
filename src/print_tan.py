import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pld
import math

def plot_tangents():
    '''
    TODO Add documentation here
    '''
    points = pd.read_csv("../data/2025.02.11_cell_32.5_cm", header=None)

    #xpoints = np.arange(points[1].size)
    ypoints = points[1]

    y_max_ind = pld.find_ind_of_min_or_max(ypoints, pld.operator.gt)

    ypoints = ypoints[:y_max_ind]

    tans = np.zeros(y_max_ind, dtype=float)
    for i in range(1, y_max_ind):
        tans[i-1] = ypoints[i]-ypoints[i-1]
    
    stds = np.zeros(tans.size-15, dtype=float)
    for i in range(0, tans.size-15):
        sample = tans[i:i+15]
        stds[i] = np.std(sample)
    
    delta_tan = 0.0015
    stop_ind = 0
    for i in range(1, tans.size-1):
        if tans[i-1]-tans[i] > delta_tan:
            stop_ind = i
            break
    
    print(stop_ind, tans[stop_ind-10:stop_ind+10], tans[0])

    plt.plot(np.arange(0, stop_ind), tans[:stop_ind])
    plt.show()

#    plt.plot(np.arange(0, stds.size), stds)
#    plt.show()
#
#    plt.plot(np.arange(0, tans.size), tans)
#    plt.show()

if __name__ == "__main__":
    plot_tangents()