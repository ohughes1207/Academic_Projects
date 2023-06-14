# 2021 FERRE Undergraduate Project

The atmospheric properties of 735 observed spectra from chemically peculiar Ap stars have been measured using theoretical grids of star spectra. Model grids have been applied to the 735 spectra using the FERRE data analysis code. This project presents the results of the fit of the observed spectra to the model grid and discusses which are the best fit. The results show that the best fit is achieved when continuum normalizing with a polynomial with an order of 4 and effective temperature, log(g) and metallicity [M/H] are varied however there is potential for a four parameter fit including the α-elements and continuum normalizing with a polynomial with an order of 3. The errors in the effective temperature, log(g), metallicity and α-elements are estimated to be ±100K, ±0.1, ±0.2 dex and ±0.2 dex respectively.

## Introduction

By taking advantage of exoplanet survey from NASA’s Explorers program in 2018, an analysis of the spectra of stars can be done. The stars analysed in this project have been monitored from the TESS satellite with photometric time series observations and were selected because of suspected high frequency pulsations. The fluxes and wavelengths of 735 chemically peculiar Ap stars have been observed. The instrument used for the observations was a 1.9m telescope with low resolution grating and 2 arcseconds per 2 pixels. FERRE is a software written in FORTRAN90 that analyses data by matching models to data, the software will be used to analyse 735 spectra, this software could be a valuable tool in future endeavours. The goal of this project is to determine the atmospheric properties of peculiar, pulsating A star candidates, to do this, A software called FERRE will be used analyse the spectra of 735 stars, this software produces data by fitting the observations with the model grids provided by the ATK library. The model grid used for this analysis has an effective temperature upper limit and lower limit of 10000K and 6000K, log(g) has and upper limit of 5 and lower limit of 2 and metallicity [M/H] has an upper limit of 0.5 dex and lower limit of -2.5 dex.

### Chemically peculiar pulsating Ap stars 

These particular stars have unusual abundances of Si, Cr, and other rare earth metals compared to other stars and they have stronger magnetic fields than other stars, they are on main sequence if not somewhere near and typically have an effective temperature of more than 7000K and are unstable. As their name suggests, these stars are pulsating, meaning that they continuously expand and contract, causing their brightness to change. These stars also have a lower rotational velocity than normal A type stars. It is for these reasons that Ap stars have been researched by Astronomers.

## Method

PuTTY and Xming were used in conjunction throughout this project to access the UCLan Starlink network. Through this network is how the data was accessed and the FERRE software was ran. The FERRE documentation was referred to for research in order to understand how to operate the software. Prior to running FERRE for all the data, FERRE was ran on data for a single spectra to perform diagnostic tests.

Before running FERRE, the data were converted into the format required by FERRE using software written in FORTRAN90. This software outputs 3 files which became the inputs for FERRE. The initial diagnostic tests with FERRE were performed on a singular spectrum to fit for effective temperature and surface gravity, the spectrum used in these diagnostic tests was chosen at random. The FERRE documentation specified that the Signal-to-Noise ratio (SNR) is given as the average SNR however after manually calculating this it was found that this information in the FERRE documentation is incorrect and the SNR is instead given as the median of the SNR. Following this, the reduced χ2 was calculated manually also to verify that this is correct and was found to be in agreement with the FERRE documentation.

After the diagnostic tests on the singular spectrum were completed, more diagnostic tests were performed on multiple spectra. 5 spectra were chosen at random to be used for these diagnostics. FERRE was ran to fit for effective temperature, surface gravity and metallicity for these 5 spectra. Following this, FERRE was ran to fit only for effective temperature and surface gravity with a polynomial order of 3 on the 5 spectra. Due to the format of the data outputted by FERRE a Python script was written to extract the data of a single spectrum which is specified by the user. With the extracted data, comparisons can be made to see the effect that changing the polynomial order and fitted parameters has on the results. More diagnostic tests to fit for different parameters with varying order of polynomials were performed to compare the results and further investigate the differences that fitting for different parameters with varying order of polynomials has on the result.

The report provided in this repository provides more details on the methodology throughout this project.

## Results

The resulting plots from the methodology were compared to see the effect of changing each parameter.

### Effect of polynomial order on the fits

<h4 align=center> Kiel diagram of NCONT=3 and NCONT=4 when fitted for TgZ (effective temperature, surface gravity and metallicity) </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/TgZ_3+4.png)

</div>


<h4 align=center> Kiel diagram of NCONT=2 and NCONT=4 when fitted for TgZ </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/TgZ_2+4.png)

</div>




<h4 align=center> Kiel diagram of NCONT=3 and NCONT=4 when fitted for TgZA (effective temperature, surface gravity, metallicity and alpha elements) </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/TgZA_3+4.png)

</div>


## Discussion
