import numpy as np

def bpt_kauffman03(logniiha):
	'''
	Defining the BPT AGN/SF dividing line from Kauffmann 2003.
	'''    
	return 0.61/(logniiha - 0.05) + 1.3    

def bpt_kewley01(logniiha):
	'''
	Defining the BPT AGN/SF dividing line from Kewley 2001.
	'''    
	return 0.61/(logniiha - 0.47) + 1.19    

def vo87(logsiiha):
	'''
	Defining the unVO87 AGN/SF dividing line from Veilleux & Osterbrock 1987.
	Singularity at log(SII/Ha) = 0.0917
	'''    
	return 0.48/(1.09*logsiiha - 0.10) + 1.3    
	
def unvo87(logsiiha):
	'''
	Defining the unVO87 AGN/SF dividing line from Backhaus et al. 2021.
	Singularity at log(SII/Ha) = -0.11
	'''    
	return 0.48/(1.09*logsiiha + 0.12) + 1.3

def ohno(logneiiioii):
	'''
	defining the unv087 dividing line from Backhaus et al. 2021.
	Singularity at log(NeIII/OII) = 0.285
	'''    
	return 0.35/(2.8*logneiiioii - 0.8) + 0.64

def mass_excitation_j11(logmass):
	'''
 	Return the Mass Excitation AGN/SF dividing line from Juneau et al. 2011
	'''
	y_upper = np.zeros(len(logmass))
	for i,m in enumerate(logmass):
		if m <= 9.9:
			y_upper[i] = 0.37/(m - 10.5) + 1.1
		else:
			y_upper[i] = 594.753 + -167.074*m +15.6748*m**2 + -0.491215*m**3
			
	y_lower = np.zeros(len(logmass))
	for i,m in enumerate(logmass):
		if (m >= 9.9)&(m <= 11.2):
			y_lower[i] = 800.492 + -217.328*m + 19.6431*m**2 + -0.591349*m**3
		else:
			y_lower[i] = np.NaN
	
	return y_upper, y_lower

def mass_excitation_j14(logmass):
	'''
 	Return the Mass Excitation AGN/SF dividing line from Juneau et al. 2014
	'''
	y_upper = np.zeros(len(logmass))
	for i,m in enumerate(logmass):
		if m <= 10:
			y_upper[i] = 0.375/(m - 10.5) + 1.14
		else:
			y_upper[i] = 410.24 + -109.333*m + 9.71731*m**2 + -0.288244*m**3
			
	y_lower = np.zeros(len(logmass))
	for i,m in enumerate(logmass):
		if m <= 9.6:
			y_lower[i] = 0.375/(m - 10.5) + 1.14
		else:
			y_lower[i] = 352.066 + -93.8249*m + 8.32651*m**2 + -0.246416*m**3
	
	return y_upper, y_lower