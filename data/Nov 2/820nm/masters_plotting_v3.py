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

    """
    a = np.loadtxt(filename)
    x = a[:,0]/2
    y = a[:,1]/1e-6
    return x ,y 

def stats(y):
    avg = "{0:.4g}".format(np.mean(y))
    std = "{0:.3g}".format(np.std(y))
    var = "{0:.3g}".format(np.var(y))
    return avg, std, var

def plot(x, y, avg, std, var, wavelength,  savefile = 'plots.pdf', date = '2nd Nov'):
    """
    Plots x and y data 
    
    Parameters
    ----------
    x : x data for plot.
    y : y data for plot.

    """
    yerr = np.ones(len(x))*1e-12
    plt.errorbar(x,y,yerr, fmt = 'o', c = 'blue', label = 'data')
    plt.title('Measurement of current with '+ str(wavelength)+ ' wavelength laser source')
    plt.xlabel('Time in minutes')
    plt.ylabel('Measured current in micro amps ($\mu$A, 1e-6A)')
    plt.figtext(0.61,0.97,'Data collected on ' + str(date))
    plt.figtext(0,-0.02,'Note: Data collected over 10 mins with intervals of 30s between each measurement')
    plt.figtext(0, -0.06, '20 measurements in total')
    plt.figtext(0.92, 0.75, 'mean: '+ str(avg)+' 1e-6')
    plt.figtext(0.92, 0.70, 'std: '+ str(std)+' 1e-6')
    plt.figtext(0.92, 0.65, 'var: '+ str(var)+' 1e-6')
    plt.savefig(savefile, format = 'pdf', bbox_inches="tight")
    
    #plt.show()

def textfile(wavelength, mean, std, var, savetext = 'info.txt'):
    with open(savetext, 'w') as f:
        f.write('Information of mean, variance and standard deviation of measurement')
        f.write("\n")
        f.write(str('wavelength ') + str(wavelength))
        f.write("\n")
        f.write(str('mean ') + str(mean) + " +/- " + str(std) + ' ' + '$\mu$A 1e-6')
        f.write("\n")
        f.write(str('variance ') + str(var) + ' 1e-6')
    f.close()
    
def main():
    filename = input('enter filename as .txt ')
    x, y = readfile(filename)
    avg, std, var = stats(y)
    #date = input("enter date the data was collected on ")
    #savename = input('enter name of png file to save as .pdf ')
    #savetext = input('enter name of txt file to save info as .txt ')
    Wavelength = input('enter wavelength in nm ')
    plot(x,y, avg, std, var, Wavelength)
    textfile(Wavelength, avg, std, var)
    
if __name__ == "__main__":
    main()

