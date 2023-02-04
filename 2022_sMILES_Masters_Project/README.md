# 2022 sMILES Masters Project

Data Analysis software written in Python to determine the best fitting SSPs (Simple Stellar Populations) from the sMILES spectral library to observations of the galaxy G422436 from the SALT (South African Large Telescope). The sMILES library has SSPs from 5 families from [α/Fe] abundances with there being 636 spectra in each family for a total of 3180 spectra. The software blurs, rebins and normalizes the SSPs and determines the best fitting SSP for each [α/Fe] abundance via a reduced chi-squared test. The software also creates 3d plots with Metallicity vs Age vs Reduced chi-squared for each abundance family and creates plots showing the residuals for best fitting SSP from each family. The module fit_tools was developed to be used in conjunction with this software, containing functions for the analysis. The results of this project determined that the sMILES SSPs do not match the target galaxy well due to the reduced chi-squared of all SSPs are greater than 1, and that the best fitting SSP has a solar-like [α/Fe] with an age of 5 Gyrs and metallicity of +0.4. The reduced chi-squared of the best fitting SSP is 7.13. The results show that typically the best fits to the target galaxy are found when an SSP has an [α/Fe] of +0.0 to +0.2 with metallicities ranging from -0.4 to +0.4 and have an age of more than 2 Gyrs.

## Introduction

The sMILES library was created with improvements made on the MILES library. sMILES improves on the MILES library by using predictions of abundance patterns to differentially correct the MILES library, creating the sMILES library. The target galaxy GAMA422436 was detected in the Herschel-ATLAS survey and is in the GAMA survey, it is a dusty early type galaxy and classified as an Sa type galaxy by NASA/IPAC Extragalactic Database. This software aims to find the best fitting parameters for SSPs from the sMILES library to the observational data of GAMA422436.

<h4 align=center> Image of the target galaxy </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/GAMA422436.PNG)

</div>
  
This is achieved by blurring and rebinning the sMILES SSPs to the same binning as the SALT data and then continuum normalizing both the models and data so a chi-squared test can be performed to determine the best fit. A software called ``pPXF`` created by Michele Cappellari can extract the stellar kinemtic or gas kinematics and stellar population of spectra with absorption lines by full spectrum fitting. This software then fits the stellar and gas kinematics however this is not for SSPs and so the creation of this software serves as a stepping stone for future works in the development of such a tool.


## Method

This software was developed using Spyder Python 3.9 on a Windows 10 PC and Python 3.7 on the UCLan Starlink network which was accessed from a Linux OS machine at UCLan. Both work spaces had the modules ``specutils``, ``SpectRes``, ``astropy``, ``scipy``, ``glob``, ``numpy``, ``matplotlib`` and the local module that was made with this software, ``fit_tools``. The observational data was read in using ``astropy`` as the data is in the format of a FITS file and was then continuum normalized with a Chebyshev polynomial using the ``fit_continuum`` function from ``specutils``. To begin processing the SSPs, the SSPs were read in by using ``glob`` to find all SSP files that do not contain the variance following the sMILES library naming convention and using a for loop to read in the data and error for a single SSP with a function from ``fit_tools`` to extract the data into a list and perform the analysis on each SSP individually.
The SSPs are blurred using the ``gaussian_filter1d`` function from ``scipy``, the function blurs an input flux by an input sigma value. The input sigma value was calculated as the sigma difference in pixels before any loops. This follows a similar method used in the Sauron kinematics example from the ``pPXF`` software.
The SSPs are rebinned to the same binning as the SALT data using ``SpectRes`` and then continuum normalized using the same method as for the SALT data. The reduced chi-squared test is then performed with functions from the fit_tools local module. Then reduced chi-squared, age, metallicity, and filename for the SSP is then store into their own respective list. This process is repeated for all SSPs in each abundance family resulting in a list containing 5 nested lists, one for each abundance family, and each nested list contains 4 nested lists, one for each of the stored parameters from the data processing.
Diagnostic plots were made to ensure that the processes were performing as expected and the Chebyshev polynomial order was varied to determine which polynomial order gives the best result and was found that a Polynomial order of 6 gives the best result. The software also applies a mask to the spectra to remove some edge effects from continuum normalization.

The effects of the blurring and rebinning can be seen in the diagnostic plots shown below.

<h4 align=center> Blurring diagnostic plot </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/Blurring_diagnostic.png)

</div>

<h4 align=center> Rebinning diagnostic plot </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/Rebinning_diagnostic.png)

</div>

Edge effects from continuum normalization as sen in the plot.

<h4 align=center> Applied mask </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/mask.PNG)

</div>


The described loop for the SSP processing can be summarized with the block diagram shown below

<h4 align=center> SSP processing loop block diagram </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/loop.PNG)

</div>


## Results

It was found that the best fitting SSPs have a solar-like abundance.

<h4 align=center> 3d plot showing trends in reduced chi-squared as Age and Metallicity are varied for solar-like abundance SSPs </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/3d_solar.PNG)

</div>



<h4 align=center> Best fitting SSP </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/best_SSP.PNG)

</div>

## Discussion

The 3d-plots showing the trends in reduced chi-squared demonstrate the Age-metallicity degeneracy where it is difficult to differentiate old and metal poor galaxies from young, metal rich galaxies. None of the SSPs are well fitted to the target galaxy however the best fitted SSP has a reduced chi-squared of 7.13 with an age and metallicity of 5 Gyrs and +0.4 respectively and solar-like [α/Fe] abundance. The age-metallicity degeneracy is also demonstrated in the best fitted SSP with a solar-like [α/Fe] abundance and best fitted SSP with [α/Fe]=+0.2 as the solar-like SSP is a young metal rich SSP while the SSP with [α/Fe]=+0.2 is an old metal poor SSP, showing that a best fitting SSP to the target galaxy can be a young metal rich SSP or an old metal poor SSP.
