import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pld
import math
from scipy.signal import find_peaks

def create_std(arr, sample_size):
    stds = np.zeros(arr.size-sample_size, dtype=float)
    for i in range(0, arr.size-sample_size):
        sample = arr[i:i+sample_size]
        stds[i] = np.std(sample)
    return stds

def create_tans(arr, step=1):
    tans_list = []
    ind0 = 0
    ind1 = step
    while ind1 < arr.size:
        tans_list.append(arr[ind1] - arr[ind0])
        ind0 = ind1
        ind1 += step
    return np.array(tans_list)

def plot_tangents():
    '''
    TODO Add documentation here
    '''
    points = pd.read_csv("../data/2025.02.11_cell_32.5_cm", header=None)

    #xpoints = np.arange(points[1].size)
    ypoints = points[1]

    y_max_ind = pld.find_ind_of_min_or_max(ypoints, pld.operator.gt)

    ypoints = ypoints[:y_max_ind]

    indexes,_ = find_peaks(ypoints)
    minus_indexes,_ = find_peaks(ypoints*-1)
    #plt.plot(indexes, ypoints[indexes], 'ro')
    #plt.plot(minus_indexes, ypoints[minus_indexes], 'go')
    #plt.plot(np.arange(0, ypoints.size), ypoints)

    tans = create_tans(ypoints)
    stds = create_std(ypoints, 15)

    plt.plot(np.arange(0, stds.size), stds)
    plt.plot(indexes, stds[indexes], 'ro')
    plt.plot(minus_indexes, stds[minus_indexes], 'go')

#   delta_tan = 0.01
#   stop_ind = 0
#   for i in range(1, tans.size):
#       if tans[i-1]-tans[i] > delta_tan:
#           stop_ind = i
#           break
#   
#   real_stop_ind = (stop_ind-1)*step_tan

    #y_to_plot = ypoints
    #plt.plot(np.arange(0, y_to_plot.size), y_to_plot)
    #plt.plot(real_stop_ind, ypoints[real_stop_ind], 'ro')

    #tan_to_plot = tans
    #plt.plot(np.arange(0, tan_to_plot.size), tan_to_plot)
    #plt.plot(indexes, tan_to_plot[indexes], 'ro')
    #plt.plot(minus_indexes, tan_to_plot[minus_indexes], 'go')
    plt.show()
    
# std from std begin
#    std_from_std = np.zeros(stds.size-15, dtype=float)
#    for i in range(0, stds.size-15):
#        sample = stds[i:i+15]
#        std_from_std[i] = np.std(sample)
#    
#    to_plt = std_from_std[50:160]
#    plt.plot(np.arange(0, to_plt.size), to_plt)
#    plt.show()
# std from std end

    #plt.plot(np.arange(0, stop_ind), tans[:stop_ind])
    #plt.show()
    #
    #std_sample = stds[:160]
    #plt.plot(np.arange(0, std_sample.size), std_sample)
    #plt.show()

    #plt.plot(np.arange(0, tans.size), tans)
    #plt.show()

if __name__ == "__main__":
    plot_tangents()