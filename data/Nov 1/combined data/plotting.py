import numpy as np
import matplotlib.pyplot as plt

def readfile(filename):
    """
    Reads file name and generate x and y data for plotting
    Parameters
    ----------
    filename : The name of the file to be plotted.

    Returns
    -------
    x : x data for plot.
    y : y data for plot.
    y_err : y error
    z : z data
    z_err : z error
    """
    a = np.loadtxt(filename)
    x = a[:,0]
    y = a[:,1]/1e-6
    return x ,y,

def plot(x ,y, file1 = 'plots.pdf'):
    plt.scatter(x,y)
    plt.title('Mean current ($\mu$A, 1e-6A) vs Wavelength (nm)')
    plt.xlabel('Wavelength (nm, 1e-9m)')
    plt.ylabel('current ($\mu$A, 1e-6A)')
    plt.figtext(0.63,0.95,'Data collected Nov 1st')
    plt.savefig(file1, format = 'pdf')
    plt.show()


filename = input("enter text file .txt ")
x ,y = readfile(filename)

plot(x, y)
