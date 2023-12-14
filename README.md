This package contains various modules with functions I (Nikko Cleri) use for my astronomical research. 
This package is broken down as follows: 

spectrum_tools: contains modules to display annotations and highlights of lines on spectra. 
Also includes some rudimentary stacking methods. 

cloudy_tools: contains a model builder for the photoionization modeling code Cloudy, which is designed to be able to produce large amounts of Cloudy input (.in) files.
Also contains functions designed to make outputs from Cloudy more user friendly. 

physics_functions: contains various derivations of physical quantities (e.g., star formation rate, luminosity, etc.)
as well as some useful unit conversions (air to vacuum wavelengths, photon energy to wavelength, etc.)

stat_functions: contains uncertainty propagations

figure_functions: contains wrappers to make some of the prominent figures in my work (e.g., line ratio diagnostics)

ratio_diagnostics: contains the functional forms of many emission-line ratio diagnostics of star formation/active black holes

miscellaneous_functions: contains other miscellaneous utilities - will likely change significantly over time