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


A Kiel diagram displaying both cases of NCONT were plotted together on the same plot as seen in Fig.21 to determine the difference in how NCONT=4 differs from NCONT=3 and as seen in Fig.21 the data points shift to the right, away from the upper effective temperature limit in the case of NCONT=4 from the NCONT=3 case.For this reason NCONT=4 is the preferred order of NCONT as there are more stars that are within the valid region of the model grid. Also the average χ2 is lower in the case of NCONT=4, supporting the decision that NCONT=4 is the preferred value of NCONT.

<h4 align=center> Kiel diagram of NCONT=2 and NCONT=4 when fitted for TgZ </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/TgZ_2+4.png)

</div>


The plot in Fig.22 shows how NCONT=4 compares to NCONT=2 to investigate if NCONT=2 provides a better fit than NCONT=4, Fig.22 illustrates that NCONT=4 still provides the better fit as it’s data points are further away from the boundaries with more data points being within the valid region.


<h4 align=center> Kiel diagram of NCONT=3 and NCONT=4 when fitted for TgZA (effective temperature, surface gravity, metallicity and alpha elements) </h4>

<div align="center">
  
![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/TgZA_3+4.png)

</div>


The plot in Fig.23 illustrates how varying NCONT=3 and NCONT=4 in the case of the TgZA fit moves the data points around the plot. Fig.23 shows that NCONT=3 gives the better fit in this case as there are less data points against the boundaries and thus more data points in the valid region.



### Effect of polynomial order on the NORMFIT/FIT plots

<h4 align=center> Plot of continuum normalized flux divided by the models of TgZ NCONT=2 fit for the spectrum TIC_073765625_spectrum_B_8566.492492123507_rest </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/Spectra2_TgZ_NCONT2_NORMFITFIT.png)

</div>



<h4 align=center> Plot of continuum normalized flux divided by the models of TgZ NCONT=3 fit for the spectrum TIC_073765625_spectrum_B_8566.492492123507_rest </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/Spectra2_TgZ_NCONT3_NORMFITFIT.png)

</div>



<h4 align=center> Plot of continuum normalized flux divided by the models of TgZ NCONT=4 fit for the spectrum TIC_073765625_spectrum_B_8566.492492123507_rest </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/Spectra2_TgZ_NCONT4_NORMFITFIT.png)

</div>


Comparing the 3 figures shown above shows that neither of the fits are better than the rest and the CaII K and H-ϵ lines in particular are poorly fitted in all cases of NCONT for this spectra.


### Effect of fitted parameters on the fits

<h4 align=center> Kiel Diagram for both cases of Tg and TgZ fits with NCONT=3 </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/3_Tg_vs_TgZ.png)

</div>

The figure shown illustrates that the TgZ fit provides the better fit than the Tg fit in the case of NCONT=3 as there are less data points against the boundaries.

<h4 align=center> Kiel Diagram for both cases of Tg and TgZ fits with NCONT=4 </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/4_Tg_vs_TgZ.png)

</div>

The figure shown above also illustrates that the TgZ fit provides the better fit than the Tg fit in the case of NCONT=4 as there are less data points against the boundaries, both Fig.31 and Fig.32 show a line of Tg fitted data points that are against the upper temperature boundary, this supports that the TgZ fit is a more preferable fit than the Tg fit for this data.



<h4 align=center> Kiel Diagram for both cases of TgZA and TgZ fits with NCONT=4 </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/4_TgZA_vs_TgZ.png)

</div>

Because of the vertical line of data points from the TgZA at the upper temperature limit in the figure shown above, the TgZA fit is a worse fit in the case of NCONT=4 as this indicates there are more data points against the upper temperature limi

## Discussion


<h4 align=center> Table of the reduced χ2 and number of points against the boundaries as NCONT and fitted parameters change </h4>

<div align="center">

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/ncont_param_table.PNG)

</div>

By comparing the average reduced χ2 and number of points against the boundaries in each fit in the table shown above, the TgZ fit with NCONT=4 is where the best fit is achieved. This fit has the least number of data points against the boundaries and only 0.2 average reduced χ2 higher than the TgZA with NCONT=3 fit, which has the lowest average χ2. A case for the TgZA fit with NCONT=3 being the best fit could be made as this fit has the lowest average reduced χ2, however this is only 0.2 lower than the average χ2 in the TgZ with NCONT=3 fit. 
The results also shows that the TgZA fit could achieve a better fit as these match the models better than the TgZ fits. The results also show that as fitted parameters increase in the NCONT=3 case, the average reduced χ2 and number of points against the boundaries decrease, indicating that if one were to be able to fit with NCONT=5 then these would decrease even further potentially giving a better fit.

## Conclusion

The results of this project show that the best fit of the data to the models is achieved when fitting for effective temperature, surface gravity and metallicity and continuum normalizing with a polynomial with an order of four. There is potential for a better fit to be achieved when fitting for effective temperature, surface gravity, metallicity and α-elements and continuum normalizing with a polynomial with an order of three however further investigations must be done into this. The errors in the effective temperature, log(g),metallicity and α-elements are estimated to be ±100K, ±0.1, ±0.2 dex and ±0.2 dex respectively by inspection of the differences in parameters for NCONT=3 and NCONT=4.