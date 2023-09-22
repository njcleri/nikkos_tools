import pandas as pd
from nikkos_tools import physics_functions as pf

lines = {
        'Lya':[1215.67,r'Ly$\alpha$'],
        'NV':[1240,'NV'],
        'CIV_1548':[1548,'CIV'],
        'HeII_1640':[1640.4,'HeII'],
        'OIII_1664':[1664,'OIII]'],
        'SiIII_1883':[1883,'SiIII]'],
        'CIII_1907':[1906.8,'CIII]'],
        'MgII_2798':[2798,'MgII'],
        'NeV_3346':[3346,''],
        'NeV_3426':[3426,'[NeV]'],
        'OII_3727':[3727,'[OII]'],
        'NeIII_3869':[3869,'[NeIII]'],
        'Hdelta':[4102,r'H$\delta$'],
        'Hgamma':[4341,r'H$\gamma$'],
        'OIII_4363':[4363,'[OIII]'],
        'HeII_4686':[4686,'HeII'],
        'Hbeta':[4861, r'H$\beta$'],
        'OIII_4959':[4959,''],
        'OIII_5007':[5007,'[OIII]'],
        'HeI':[5876,'HeI'],
        'Halpha':[6563, r'H$\alpha$'],
        'SII_6716':[6716,''],
        'SII_6731':[6731,'[SII]']
		}

shifts = {
        'Lya':-1,
        'NV':1,
        'CIV_1548':-1,
        'HeII_1640':1,
        'OIII_1664':1,
        'SiIII_1883':-1,
        'CIII_1907':1,
        'MgII_2798':1,
        'NeV_3346':-1,
        'NeV_3426':-1,
        'OII_3727':-1,
        'NeIII_3869':1,
        'Hdelta':1,
        'Hgamma':-1,
        'OIII_4363':1,
        'HeII_4686':-1,
        'Hbeta':-1,
        'OIII_4959':1,
        'OIII_5007':1,
        'HeI':-1,
        'Halpha':-1,
        'SII_6716':-1,
        'SII_6731':-1
		}

def make_linesdf():
    for key in lines.keys():
        lines.get(key).append(shifts.get(key))
    linesdf = (pd.DataFrame(lines)
            .T
            .reset_index()
            .rename(columns={'index':'line', 0:'wavelength_air', 1:'label', 2:'offset'})
            .assign(wavelength_vacuum = lambda x: pf.convert_wavelength_air_to_vacuum(x.wavelength_air))
            )
    linesdf.to_csv('linesdf.csv', index=None)
    
if __name__ == '__main__':
    make_linesdf()
    