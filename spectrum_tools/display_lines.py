import pandas as pd

def load_lines(file):
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        print('FileNotFoundError: lines file not found')

def display_lines_air(ax, vertical_anchor, lines_to_show=[], redshift=0, 
                      wavelength_conversion=1, width=20, fontsize=15, show_text=False, lines_file='linesdf.csv'):
    linesdf = load_lines(lines_file)
    
    for line in lines_to_show:
        line_data = linesdf[linesdf.line == line]
        wave_min = (line_data.wavelength_air.values[0]-width/2)*wavelength_conversion*(1+redshift)
        wave_max = (line_data.wavelength_air.values[0]+width/2)*wavelength_conversion*(1+redshift)
        offset = line_data.offset.values[0]*wavelength_conversion*(1+redshift)
        label = line_data.label.values[0]
        if type(label) != str:
            label = ''

        ax.axvspan(wave_min, wave_max, color='k', ec=None, alpha=0.1)
        if show_text and (offset > 0):
            ax.text((wave_max), vertical_anchor, f'{label}',\
            fontsize=fontsize, verticalalignment='top', horizontalalignment='left', rotation='vertical')
        
        if show_text and (offset < 0):
            ax.text((wave_max), vertical_anchor, f'{label}',\
            fontsize=fontsize, verticalalignment='top', horizontalalignment='right', rotation='vertical')
            
def display_lines_vacuum(ax, vertical_anchor, lines_to_show=[], redshift=0, 
                      wavelength_conversion=1, width=20, fontsize=15, show_text=False, lines_file='linesdf.csv'):
    linesdf = load_lines(lines_file)
    
    for line in lines_to_show:
        line_data = linesdf[linesdf.line == line]
        wave_min = (line_data.wavelength_vacuum.values[0]-width/2)*wavelength_conversion*(1+redshift)
        wave_max = (line_data.wavelength_vacuum.values[0]+width/2)*wavelength_conversion*(1+redshift)
        offset = line_data.offset.values[0]*wavelength_conversion*(1+redshift)
        label = line_data.label.values[0]
        if type(label) != str:
            label = ''

        ax.axvspan(wave_min, wave_max, color='k', ec=None, alpha=0.1)
        if show_text and (offset > 0):
            ax.text((wave_max), vertical_anchor, f'{label}',\
            fontsize=fontsize, verticalalignment='top', horizontalalignment='left', rotation='vertical')
        
        if show_text and (offset < 0):
            ax.text((wave_max), vertical_anchor, f'{label}',\
            fontsize=fontsize, verticalalignment='top', horizontalalignment='right', rotation='vertical')