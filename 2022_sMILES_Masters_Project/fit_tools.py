# -*- coding: utf-8 -*-
"""
@author: Olliver

This module was developed and intended to be used with the software sMILES SSP fitting.

Olliver Hughes 22 Jan 2022 - Function to convert SSP files added
Olliver Hughes 25 Mar 2022 - Function for Chi-squared test added
Olliver Hughes 16 Apr 2022 - Function to extract the Age and Metallicity from filenames following sMILES naming convention added

"""

import numpy as np

#Checks if the line can be converted and ignores lines with text (i.e. Headers, comments etc)
def can_convert(row_text):
    
    for entry in row_text.rstrip().split('        '):

        try:
            
            float(entry)
        except:
            
            return False
    

    return True


#Performs Chi-squared test and returns the sum of all chi-squareds to be used in calculating reduced chi-squared
def chi_test(obs_flux, model_flux, error):
    
    chi_array = ((obs_flux-model_flux))**2/(error)**2
    
    chi_squared_sum = np.sum(chi_array)
    
    return chi_squared_sum


#Extracts metallicity and age from input filename then converts and returns them as floating point numbers
def convert_Z_Age(filename):
    Z = filename[8:13]
    Age = filename[14:21]
    
    #Reads the letter before the metallicity number and decides if the number if positive or negative based on if it is p or m
    if Z[0] == 'm':
        Z_converted = np.negative(float(Z[1:]))
    elif Z[0] == 'p':
        Z_converted = np.positive(float(Z[1:]))
    else:
        print('Filename does not follow sMILES naming convention')
    
    Age_float = float(Age)
    
    return Z_converted, Age_float