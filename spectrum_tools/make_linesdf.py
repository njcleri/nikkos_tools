import pandas as pd
from nikkos_tools import physics_functions as pf

lines = {
    'Lya': [1215.67, 'Ly$\\alpha$', -1],
    'NV': [1240, 'NV', 1],
    'CIV_1548': [1548, 'CIV', -1],
    'HeII_1640': [1640.4, 'HeII', 1],
    'OIII_1664': [1664, 'OIII]', 1],
    'SiIII_1883': [1883, 'SiIII]', -1],
    'CIII_1907': [1906.8, 'CIII]', 1],
    'MgII_2798': [2798, 'MgII', 1],
    'NeV_3346': [3346, '', -1],
    'NeV_3426': [3426, '[NeV]', -1],
    'OII_3727': [3727, '[OII]', -1],
    'NeIII_3869': [3869, '[NeIII]', 1],
    'Hdelta': [4102, 'H$\\delta$', 1],
    'Hgamma': [4341, 'H$\\gamma$', -1],
    'OIII_4363': [4363, '[OIII]', 1],
    'HeII_4686': [4686, 'HeII', -1],
    'Hbeta': [4861, 'H$\\beta$', -1],
    'OIII_4959': [4959, '', 1],
    'OIII_5007': [5007, '[OIII]', 1],
    'HeI': [5876, 'HeI', -1],
    'Halpha': [6563, 'H$\\alpha$', -1],
    'SII_6716': [6716, '', -1],
    'SII_6731': [6731, '[SII]', -1]
 }

def make_linesdf(save_path='./linesdf.csv'):
    linesdf = (pd.DataFrame(lines)
            .T
            .reset_index()
            .rename(columns={'index':'line', 0:'wavelength_air', 1:'label', 2:'offset'})
            .assign(wavelength_vacuum = lambda x: pf.convert_wavelength_air_to_vacuum(x.wavelength_air))
            )
    linesdf.to_csv(save_path, index=None)
    
if __name__ == '__main__':
    make_linesdf()
    