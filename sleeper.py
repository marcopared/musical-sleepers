import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from scipy import signal
import numpy as np
import pandas as pd


# Detrends given data
#   inputs - data: the data (in a list) to be detrended
#   returns - the detrended data
def detrend(data):
    return signal.detrend(data)


# Highpass filter function
#   inputs - data: data in list form
#            cutoff: cutoff frequency 
#            fs: data sampled
#            order: order of the butterworth filter
#   returns - filtered output
def butter_highpass(data, cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq

    # Designs a digital Butterworth highpass filter
    # b and a are filter coefficients
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)

    # Applies digital filter forward and backward to a signal
    y = signal.filtfilt(b, a, data)
    return y


# Lowpass filter function
#   inputs - data: data in list form
#            cutoff: cutoff frequency
#            fs: data sampled
#            order: order of the butterworth filter
#   returns - filtered output
def butter_lowpass(data, cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq

    # Designs a digital Butterworth lowpass filter
    # b and a are filter coefficients
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)

    # Applies digital filter forward and backward to a signal
    y = signal.filtfilt(b, a, data)
    return y


# Creates a liveplot that updates every given interval miliseconds
#   inputs - data: the data in list form
#            xs: interval of x-axis
def liveplot(data, interval):
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(self):
        xs = []
        ys = data  # Add data here

        for x in range(len(ys)):
            xs.append(xs * x)

        ax1.clear()  # Clears axis
        ax1.plot(xs, ys)  # Plots data again

    # Uses the animate function to plot in fig every 500 miliseconds
    ani = animation.FuncAnimation(fig, animate, interval=500)
    plt.show()
