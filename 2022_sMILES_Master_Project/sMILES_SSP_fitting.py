# -*- coding: utf-8 -*-
"""
@author: Olliver Hughes


sMILES SSP Fitting software performs blurring, rebinning and continuum normalization of the sMILES SSPs and input observed data.
The best fitting SSPs are determined via a Chi-squared test.
This software is intended to be used with the module fit_tools.py, developed specifically for this software.
In development of this software SALT data of the galaxy G422436 was used for the input data.

Olliver Hughes 26 Jan 2022
Olliver Hughes 1 Feb 2022 - Blurring for a single SSP has been implemented
Olliver Hughes 14 Feb 2022 - Blurring for multiple SSPs implemented
Olliver Hughes 7 Mar 2022 - Rebinning of sMILES SSPs to SALT data binning using spectres implemented
Olliver Hughes 7 Mar 2022 - Reads files names based on naming pattern
Olliver Hughes 10 Mar 2022 - Continuum fitting of SSPs and SALT data using specutils implemented
Olliver Hughes 25 Mar 2022 - Chi-Squared test functionality added to fit_tools.py module
"""

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from specutils.fitting import fit_continuum
from specutils.spectra import Spectrum1D, SpectralRegion
from astropy import units as u
import glob
import spectres as sp
from scipy import ndimage
from astropy.modeling.polynomial import Chebyshev1D
from matplotlib import cm
from mpl_toolkits import mplot3d
import fit_tools as ft #Local module



def sMILES_SSP_fitting():
    
    
    file = 'G422436_sci_apr_central_rest.fits' #SALT observational data to be read in
    err_file = 'G422436_sci_sig_central_rest.fits' #Error of read in SALT observational data
    
    hdu = fits.open(file) #Read in fits file
    err_hdu = fits.open(err_file) #Read in error fits file
    
    h1=hdu[0].header #Define fits header
    err_h = err_hdu[0].header #Define error fits header
    
    
    SALT_flux = hdu[0].data #Array containing the SALT fluxes from the fits file
    SALT_err = err_hdu[0].data #Array containing the errors of the SALT fluxes
    
    SALT_median_norm = SALT_flux/np.median(SALT_flux) #SALT flux normalized by the median of the SALT flux 
    
    SALT_wvl = np.arange(h1['CRVAL1'], h1['CRVAL1'] + (h1['CDELT1'] * (h1['NAXIS1'])), h1['CDELT1']) #Create an array containing the wavelengths from the data in the fits file
    
    Chebyshev_NCONT=6 #Chebyshev polynomial order
    
    
    SALT_spectrum=Spectrum1D(flux=SALT_flux*(u.erg / u.angstrom / u.cm ** 2 / u.s),spectral_axis=SALT_wvl*u.angstrom) #Container for SALT spectral data

    SALT_cont_model = fit_continuum(SALT_spectrum, model=Chebyshev1D(Chebyshev_NCONT)) #Shape of the continuum of the specified spectrum as an astropy model
    
    SALT_cont_flux = SALT_cont_model(SALT_wvl*u.angstrom) #Continuum fitted
    
    SALT_cont_norm = SALT_flux / SALT_cont_flux #Normalise the SALT flux by it's continuum
    SALT_err_cont_norm = SALT_err / SALT_cont_flux #Normalise SALT errors by the continuum of the SALT flux to maintain Signal-Noise ratio

    SALT_FWHM = 5 #SALT Telescope has an instumental resolution of 5 Angstroms
    
    wvlRange = h1['CRVAL1'] + np.array([0., h1['CDELT1']*(h1['NAXIS1'] - 1)]) #Lower and upper wavelength of the SALT data

    sMILES_FWHM = 2.5 #sMILES has a resolution of 2.5 Angstroms
    
    sMILES_pix_size = 0.9000 #sMILES SSP's have a pixel size of 0.9000 Angstroms
        
    FWHM_diff = np.sqrt(SALT_FWHM**2 - sMILES_FWHM**2)
    sigma = FWHM_diff/2.355/sMILES_pix_size #Sigma difference in pixels
    
    alphaFe_path = 'sMILES_SSP/Mbi_iTp/OUT_aFe*/M/'
    
    alphaFe_dir = glob.glob(alphaFe_path)
    print(alphaFe_dir)
    sMILES_list = [[] for i in range(len(alphaFe_dir))] #Create list of empty lists equal to same number of Alpha/Fe directories found in alphaFe_path
    
    edge_array = np.array([3785.0, 6580]) #Wavelength range for edge masking
    edge_limits = (SALT_wvl >= edge_array[0]) & (SALT_wvl <= edge_array[1]) #To reduce edge effects, data outside the wavelength range in edge_array are excluded
    
    for alphaFe, aFe_list in zip(alphaFe_dir, sMILES_list):
        
        print('Processing files in directory: ' + alphaFe)
        
        #Create lists to store the parameters from the file names
        Reduced_chi_list = []
        Filenames_list = []
        Age_list = []
        Z_list = []
        cont_norm_SSP_list = []
        
        file_pattern = 'Mbi*[!_var]' #File path containing sMILES SSPs and defines pattern of the file names (Files with names beginning with "Mbi" and exlude those that end with "_var")
        SSP_path = alphaFe+file_pattern #Location of the sMILES SSPs found based on file naming pattern
        
        SSP_files = glob.glob(alphaFe+file_pattern) #Finds files based on the specified file path and naming pattern and create a list of these file names
        
        #Begin loop to process data from the files found in the SSP_files list
        for f in SSP_files:
            
            #Define filename of the current SSP file being processed
            original_filename = f[32:]
            
            #Prints name of the SSP file currently being processed for user feedback
            print('Processing file: ' + original_filename)
            
            #Define the var file of the respective SSP file
            var_f = f+'_var'
        
        
            #Read in SSP file and it's respective var file in read mode
            i = open(f, 'r')
            j = open(var_f, 'r')
            
            #Read lines of the SSP and var file ignoring those with strings     (i.e only lines containing numbers only are read in)
            rows_ssp = [[float(number) for number in row.rstrip().split("        ")] for row in i.readlines() if ft.can_convert(row)]
            rows_var = [[float(number) for number in row.rstrip().split("        ")] for row in j.readlines() if ft.can_convert(row)]
            
            #Convert read in numbers to 2d numpy array containing the wavelengths and fluxes of the SSP file and var file
            ssp = np.array([[row[0] for row in rows_ssp], [row[1] for row in rows_ssp]])
            var = np.array([[row[0] for row in rows_var], [row[1] for row in rows_var]])
            
            #Define the wavelengths and fluxes for the SSP file and var file
            ssp_Wavelength = ssp[0]
            ssp_Flux = ssp[1]
            var_Wavelength = var[0]
            var_Flux = var[1]
            
            #Blur the flux of the SSP and var file using a Gaussian filter
            blurred_ssp = ndimage.gaussian_filter1d(ssp_Flux, sigma)
            blurred_var = ndimage.gaussian_filter1d(var_Flux, sigma)
            
            #Rebin the flux of the SSP and var file to match the SALT observational data
            rebinned_ssp = sp.spectres(SALT_wvl, ssp_Wavelength, blurred_ssp)
            rebinned_var = sp.spectres(SALT_wvl, var_Wavelength, blurred_var)
            
            #Define the final processed fluxes of the SSP and var files
            processed_ssp = rebinned_ssp
            processed_var = rebinned_var
            
            #Containers for the SSP and var spectral data
            ssp_spectrum = Spectrum1D(flux=processed_ssp*(u.erg / u.angstrom / u.cm ** 2 / u.s), spectral_axis=SALT_wvl*u.angstrom)
            var_spectrum = Spectrum1D(flux=processed_var*(u.erg / u.angstrom / u.cm ** 2 / u.s), spectral_axis=SALT_wvl*u.angstrom)
            
            
            ssp_fit = fit_continuum(ssp_spectrum, model=Chebyshev1D(Chebyshev_NCONT))
            
            
            ssp_cont = ssp_fit(SALT_wvl*u.angstrom)
            
            #Continuum normalize processed flux of SSP and var file spectral data respectively
            ssp_cont_norm = processed_ssp/ssp_cont
            var_cont_norm = processed_var/ssp_cont
            
            
            #Calculate chi squared using function from local module
            chi = ft.chi_test(SALT_cont_norm[edge_limits], ssp_cont_norm[edge_limits], SALT_err_cont_norm[edge_limits])
            #print('Sum of Chi-squared: ')
            #print(chi)
            
            #Define degrees of freedom to be used in reduced chi squared calculations
            #Degrees of freedom = (Number of data points - number of varied parameters), varied parameters are Age, [α/Fe] and Total Metallicity [M/H]
            dof = h1['NAXIS1'] - 3
            
            #Determine the reduced chi squared of the SSP file 
            reduced_chi_squared = chi/dof
            
            #Extract the age and metallicity from the filename of the SSP
            file_Z, file_Age = ft.convert_Z_Age(original_filename)
            
            #Append the processed parameters to their respective list so they can be used in plots later
            Reduced_chi_list.append(reduced_chi_squared.value)
            Age_list.append(file_Age)
            Z_list.append(file_Z)
            cont_norm_SSP_list.append(ssp_cont_norm)
            Filenames_list.append(original_filename)
            
            #Close the SSP and var files
            i.close()
            j.close()
            
        #Append the list of parameters of all SSPs in the abundance direcory being looped to the sMILES_list
        aFe_list.append(Reduced_chi_list)
        aFe_list.append(Age_list)
        aFe_list.append(Z_list)
        aFe_list.append(cont_norm_SSP_list)
        aFe_list.append(Filenames_list)
        
    
    
    output_f = open("sMILES_fit_output.txt", "a") #Creates the output file where the parameters of the best fitting SSPs from each Alpha/Fe abundance will be written to
    output_f.write('[alpha/Fe] Directory'+'\t'+'Filename'+'\t'+'Age (Gyrs)'+'\t'+'Metallicity'+'\t'+'Reduced Chi-Squared'+'\n') #Writes the name of the parameter with tab spacing
    
    
    #Begin loop to make plots for each Alpha/Fe abundance 
    for aFe, aFe_directory in zip(sMILES_list, alphaFe_dir):
        
        #Define the lists for each parameter in the Alpha/Fe abundance that is currently being worked on
        Red_chi_sqr = np.array(aFe[0])
        Age = np.array(aFe[1])
        Z = np.array(aFe[2])
        SSP_Flux = np.array(aFe[3])
        Filename = np.array(aFe[4])
        
        
        #Creates 3d plot of surfce with metallicity, age and reduced chi-squared
        plt.figure(dpi=200)
        ax=plt.axes(xlabel='Z Metallicity', ylabel='Age (GYrs)', zlabel='Reduced Chi-Squared', projection ='3d')# title=aFe_directory[23:29], projection ='3d')
        print(aFe_directory[23:29])
        ax.plot_trisurf(Z, Age, Red_chi_sqr, cmap=cm.jet_r, label=aFe_directory[23:29])
        ax.invert_zaxis()
        ax.view_init(210, 240)
        #plt.savefig(aFe_directory[23:29]+'_3d_plot.png', bbox_inches="tight") #Save the plot as a .png file with name based off the Alpha/Fe abundance that the plot is for
        plt.show()
        
        
        #Creates a scatter plot of age vs metallicity with colours of the points qualitatively indicating their reduced chi-squared
        plt.figure(dpi=200)
        plt.axes(xlabel='Z Metallicity', ylabel='Age (GYrs)')#, title=aFe_directory[23:29])
        print(aFe_directory[23:29])
        plt.scatter(Z, Age, c=Red_chi_sqr, s=10, cmap=cm.jet_r, label=aFe_directory[23:29])
        plt.colorbar(label='\u03C7 $^2$')
        plt.gca().invert_yaxis()
        #ax.view_init(210, 240)
        #plt.savefig(aFe_directory[23:29]+'_scatter_plot.png', bbox_inches="tight")
        plt.show()
        
        
        min_chi_index =np.argmin(Red_chi_sqr) #Defines the index of the lowest reduced chi-squared in the list of reduced chi-squareds
        
        
        #Plots processed SALT data, best fitting SSP and the residuals all on the same plot with an offset in each to show them more clearly
        plt.figure(dpi=200)
        plt.axes(xlabel='Wavelength (Angstrom)', ylabel='Normalized Flux')
        plt.grid()
        plt.plot(SALT_wvl[edge_limits], SSP_Flux[min_chi_index][edge_limits], label='Best Fitting SSP Continuum Normalized')
        plt.plot(SALT_wvl[edge_limits], SALT_cont_norm.value[edge_limits] - 1.5, label='SALT Continuum Normalized')
        plt.plot(SALT_wvl[edge_limits], (SALT_cont_norm.value[edge_limits]-SSP_Flux[min_chi_index][edge_limits]) - 1.5, label='Residuals (SALT - sMILES SSP)')
        
        #4 black vertical dashed lines are placed on the plots to indicate where there are gaps in the detectors 
        plt.axvline(x=4663.9, linestyle= '--', color = 'black')
        plt.axvline(x=4734.7, linestyle= '--', color = 'black')
        plt.axvline(x=5690.3, linestyle= '--', color = 'black')
        plt.axvline(x=5753.8, linestyle= '--', color = 'black')
        
        plt.legend(bbox_to_anchor=(0,1.01), loc='lower left')
        #plt.savefig(aFe_directory[23:29]+'_best_fit.png', bbox_inches="tight")
        
        #Used to zoom in on a specific region, useful for when trying to indentify spectral lines
        #plt.xlim([4220, 4230])
        #plt.ylim([0.1, 1.5])
        plt.show()
        
        
        #Plots the best fitting SSP before and after the edge limits have been applied 
        plt.figure(dpi=200)
        plt.axes(xlabel='Wavelength (Angstrom)', ylabel='Normalized Flux')
        plt.grid()
        plt.plot(SALT_wvl, SSP_Flux[min_chi_index], label='SSP pre-mask')
        plt.plot(SALT_wvl[edge_limits], SSP_Flux[min_chi_index][edge_limits] - 1.5, label='SSP post edge masking')
        
        plt.axvline(x=4663.9, linestyle= '--', color = 'black')
        plt.axvline(x=4734.7, linestyle= '--', color = 'black')
        plt.axvline(x=5690.3, linestyle= '--', color = 'black')
        plt.axvline(x=5753.8, linestyle= '--', color = 'black')
        
        plt.legend(bbox_to_anchor=(0,1.01), loc='lower left')
        #plt.savefig(aFe_directory[23:29]+'_SSP'+'_masking.png', bbox_inches="tight")
        
        #plt.xlim([4200, 4400])
        #plt.ylim([0.1, 1.5])
        plt.show()
        
        
        output_f.write(aFe_directory[23:29]+'\t'+Filename[min_chi_index]+'\t'+str(Age[min_chi_index])+'\t'+str(Z[min_chi_index])+'\t'+str(np.round(Red_chi_sqr[min_chi_index], decimals=2))+'\n') #Writes the parameters of the best fitting SSP to the output file with tab spacing
    output_f.close()
        
    
    #Plots the processed SALT data before and after the edge limits have been applied
    plt.figure(dpi=200)
    plt.axes(xlabel='Wavelength (Angstrom)', ylabel='Normalized Flux')
    
    plt.grid()
    plt.plot(SALT_wvl, SALT_cont_norm.value, label='SALT data before edge mask applied')
    plt.plot(SALT_wvl[edge_limits], SALT_cont_norm.value[edge_limits] - 1.5, label='SALT data with applied edge mask')
    
    plt.axvline(x=4663.9, linestyle= '--', color = 'black')
    plt.axvline(x=4734.7, linestyle= '--', color = 'black')
    plt.axvline(x=5690.3, linestyle= '--', color = 'black')
    plt.axvline(x=5753.8, linestyle= '--', color = 'black')
    
    plt.legend(bbox_to_anchor=(0,1.01), loc='lower left')
    #plt.savefig('SALT'+'_masking.png', bbox_inches="tight")
    
    #plt.xlim([4200, 4400])
    #plt.ylim([0.1, 1.5])
    plt.show()
    
    SNR= (SALT_cont_norm.value)/SALT_err_cont_norm.value
    
    #Plots the Signal-Noise ratio of the SALT data
    plt.figure(dpi=200)
    plt.axes(xlabel='Wavelength (Angstrom)', ylabel='Signal-Noise')
    #plt.title('SALT Signal-Noise ratio', loc='right')
    plt.grid()
    plt.plot(SALT_wvl, SNR, label='SALT Signal-Noise')
    plt.axvline(x=4663.9, linestyle= '--', color = 'black')
    plt.axvline(x=4734.7, linestyle= '--', color = 'black')
    plt.axvline(x=5690.3, linestyle= '--', color = 'black')
    plt.axvline(x=5753.8, linestyle= '--', color = 'black')
    
    plt.legend(bbox_to_anchor=(0,1.01), loc='lower left')
    #plt.savefig('SALT_SNR'+'.png', bbox_inches="tight")
    
    #plt.xlim([4220, 4230])
    #plt.ylim([0.1, 1.5])
    plt.show()
    
    #Prints the median of the Signal-Noise ratio
    print('Median of the SNR:', np.round(np.median(SNR), decimals=2))
        
        
        
    
    
sMILES_SSP_fitting()