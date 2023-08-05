from .config import *
from scipy.optimize import curve_fit

def appearance_energy(data, savedir=None):
    """
    This function finds the appearance energy of all amu species present in
    the data by means of linear fit.

    Parameters
    ----------
    data: string or Pandas DataFrame
        This should be a string that points to the csv DataFrame file
        or a Pandas DataFrame. (FULL DIRECTORY STRING REQUIRED)

    Returns
    -------
    energies: list
        This will be a list where each element is string with the amu
        energy in the following format 'amu: energy'


    Example
    -------

    """
    df   = check_data_type(data)

    #Grab species of interest
    soi = species_of_interest(df)

    #initialize a dictionary for appearance energies
    energies={}

    #iterate through each species of interest
    for specie in soi:

        #slice the DataFrame so that it only has rows with amu value
        #equal to the specie of interest
        temp = df.loc[df[amu] == specie]

        x    = temp[ev].values
        y    = temp[sem].values
        a,b = x[y>0],y[y>0]

        if len(a) < 4:
            continue

        past = 1e20
        for i in range(len(a) - 4):
            a0 = a[0:len(a)-i]
            b0 = b[0:len(b)-i]

            #Perform a levenberg marquet method power law
            #fitting to the data-set
            popt, pcov = curve_fit(p_law, a0, b0, method='lm',
                                   maxfev=2000000000)

            #get index of max fitting x-value
            k = np.where(x == max(a0))[0][0]

            #Get residuals of data - fitting
            now = np.linalg.norm( y[0:k] - p_law(x[0:k], *popt) )

            #Check if this is the best fit
            if now < past:
                j = i

            past = now

        #Perform a levenberg marquet method power law
        #fitting to the data-set
        a0 = a[0:len(a)-j]
        b0 = b[0:len(b)-j]
        popt, pcov = curve_fit(p_law, a0, b0, method='lm',
                               maxfev=2000000000)

        #Fitted data
        fit0 = p_law(x, *popt)

        if savedir is not None:
            ae = str(round(popt[0],2))
            p  = str(round(popt[1],2))
            s  = 'AE = ' + ae + '\np = ' + p
            plt.plot(x,y,'.', label='Data')
            #plt.plot(x,y1,'.', label='Gaussian Sums')
            plt.plot(x, fit0, label='Wanier Fitting of Data')
            #plt.plot(x, fit1, label='Wanier Fitting of Gaussian Sums')
            plt.text(12, 0.7*max(y), s)
            plt.title(specie)
            plt.savefig(savedir + str(specie) + '.png')
            plt.close()

        #interpolate the x-intercept and add it to the dictionary
        energies[specie] = popt[0:2]

    return energies
