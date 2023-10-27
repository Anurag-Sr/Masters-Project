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
    y = a[:,1]
    y_err = a[:,2]
    z = a[:,3]
    z_err = a[:,4]
    return x ,y, y_err, z, z_err

def plot(file1, file2, x ,y, y_err, z, z_err):
    plt.errorbar(x,y,y_err,fmt = 'o')
    plt.title('Mean current (pA, 1e-12A) vs Wavelength')
    plt.xlabel('Wavelength (nm, 1e-9m)')
    plt.ylabel('current (pA, 1e-12)')
    plt.figtext(0.63,0.95,'Data collected Oct 25th')
    plt.savefig(file1, format = 'pdf')
    plt.show()

    plt.errorbar(x,z,z_err,fmt = 'o')
    plt.title('Mean current (pA, 1e-12A) vs Wavelength')
    plt.xlabel('Wavelength (nm, 1e-9m)')
    plt.ylabel('current (pA, 1e-12)')
    plt.figtext(0.63,0.95,'Data collected Oct 25th')
    plt.savefig(file2, format = 'pdf')
    plt.show()

filename = input("enter text file .txt ")
x ,y, y_err, z, z_err = readfile(filename)

savefig1 = input("enter plot file 1 .pdf ")
savefig2 = input("enter plot file 2 .pdf ")

plot(savefig1, savefig2, x, y, y_err, z, z_err)
