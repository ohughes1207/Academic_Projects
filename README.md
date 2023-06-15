# Academic Projects

<!--- - [My Personal Projects](https://github.com/ohughes1207/Personal_Projects) --->

## Introduction

I was introduced to programming during my 1st year at UCLan where we were taught the fundamentals of Python, from printing "Hello, World" to loading data from .txt and .dat files for data analysis. These fundamentals were further developed throughout the 2nd year and was expanded upon with creating our own modules and functions, and being introduced to the scientific libraries for Python such as Scipy, numpy and matplotlib and more. I found that I wanted to pursure a career and delve deeper into programming after finding my Python assignments and projects throughout my time at UCLan fulfilling.

This repository contains my academic projects from my time at UCLan.

## 2022 sMILES Masters Project

The goal of my final year project was to determine the best fitting simple stellar population (SSP) from the [sMILES spectral library](https://arxiv.org/abs/2104.04822) to the galaxy GAMA422436. This was acheived by processing both the data from the sMILES library and GAMA422436, then determining the reduced chi-squared for each SSP to then find the best fitting SSP to the galaxy.

The results of this project found that the best fitting SSP has a solar-like \[α/Fe\] ratio, an age of 5 Gyrs and a metallicity of +0.4 dex. However, the results also showed that overall the SSPs do not match the target galaxy. The spectra for the best fitting SSP is shown in the figure below along with the spectra of the target galaxy and their residuals on an offset.

<h4 align=center> Best fitting SSP </h4>

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2022_sMILES_Masters_Project/figs/aFep00_best_fit.png)

## 2021 FERRE Undergraduate Project

The goal of my third year project was to determine the atmospheric properties of chemically peculiar Ap stars by fitting models to their spectra. This was accomplished using the [FERRE](https://github.com/callendeprieto/ferre) data analysis software, this software matches models to data. Which required me to learn how to configure the software and make diagnostic runs to further understand how to operate FERRE. The outputs from FERRE were imported into Microsoft Excel to be analysed and plotted to identify any poorly fitted spectra. Many different configurations for FERRE were tested to determine which configuration gave the best results, this was determined by the average reduced χ2 and considering how many spectra were poorly fitted.

From the results of this project it was shown that the best fit is achieved when FERRE is configured to fit the models to the data with the effective temperature, surface gravity and metallicity using a 4th order polynomial, which resulted in a reduced χ2 of 61.26. The table below shows the reduced χ2 for each configuration for FERRE. It is important to note that while there is a configuration with a marginally lower reduced χ2 than the fit that was considered to be best fitting, it was not considered better fitting as the number of poorly fitted spectra increases significantly. 

<h4 align=center> Reduced χ2 for each configuration </h4>

![](https://raw.githubusercontent.com/ohughes1207/Academic_Projects/main/2021_FERRE_Undergraduate_Project/figs/ncont_param_table.PNG)
