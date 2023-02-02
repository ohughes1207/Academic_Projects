# 2022 sMILES Masters Project

Data Analysis software written in Python to determine the best fitting SSPs (Simple Stellar Populations) from the sMILES spectral library to observations of the galaxy G422436 from the SALT (South African Large Telescope). The sMILES library has SSPs from 5 families from [α/Fe] abundances with there being 636 spectra in each family for a total of 3180 spectra. The software blurs, rebins and normalizes the SSPs and determines the best fitting SSP for each [α/Fe] abundance via a reduced chi-squared test. The software also creates 3d plots with Metallicity vs Age vs Reduced chi-squared for each abundance family and creates plots showing the residuals for best fitting SSP from each family. The module fit_tools was developed to be used in conjunction with this software, containing functions for the analysis. The results of this project determined that the sMILES SSPs do not match the target galaxy well due to the reduced chi-squared of all SSPs are greater than 1, and that the best fitting SSP has a solar-like [α/Fe] with an age of 5 Gyrs and metallicity of +0.4. The reduced chi-squared of the best fitting SSP is 7.13. The results show that typically the best fits to the target galaxy are found when an SSP has an [α/Fe] of +0.0 to +0.2 with metallicities ranging from -0.4 to +0.4 and have an age of more than 2 Gyrs.

## Introduction

The sMILES library was created with improvements made on the MILES library. sMILES improves on the MILES library by using predictions of abundance patterns to differentially correct the MILES library, creating the sMILES library. The target galaxy GAMA422436 was detected in the Herschel-ATLAS survey and is in the GAMA survey, it is a dusty early type galaxy and classified as an Sa type galaxy by NASA/IPAC Extragalactic Database. This software aims to find the best fitting parameters for SSPs from the sMILES library to the observational data of GAMA422436.

<h4 align=center> Image of the target galaxy G422436 </h4>

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/GAMA422436.PNG)

This is achieved by blurring and rebinning the sMILES SSPs to the same binning as the SALT data and then continuum normalizing both the models and data so a chi-squared test can be performed to determine the best fit. A software called pPXF created by Michele Cappellari can extract the stellar kinemtic or gas kinematics and stellar population of spectra with absorption lines by full spectrum fitting. This software then fits the stellar and gas kinematics however this is not for SSPs and so the creation of this software serves as a stepping stone for future works in the development of such a tool.


## Method



## Results



## Discussion


