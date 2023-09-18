import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import seaborn as sns
from nikkos_tools import ratio_diagnostics as rd

scatter_kwargs = {
    's' : 100,
    'marker' : 'o', 
    'color' : 'k',
    'cmap' : 'Reds',
    'cbar_label' : 'colorbar', 
    'vmin' : 0,
    'vmax' : 8
        }

def plot_snr_hist(line, linelabel, dfs, labels, colors, save_path=False):
    
    plt.figure(figsize=(10,10))
    for i, df in enumerate(dfs): 
        plt.hist(df[df.line == line]['snr_line'],  label=labels[i], color=colors[i], alpha=0.5)
    plt.xlabel(f'S/N$_{{{linelabel}}}$')
    plt.ylabel('Number of Objects')
    plt.legend()
    if save_path:
        plt.savefig(save_path)
    
def plot_niibpt(x, y, xerr=None, yerr=None, save_path=None, show_colorbar=False, contour=False, contour_x=None, contour_y=None, **kwargs):
    '''
    Generates [NII]/Ha BPT diagram given x and y arrays. Can be done with multiple x and y arrays with different markers. 
    '''
    kwargs = scatter_kwargs | kwargs

    fig = plt.figure(figsize = (11, 10))
    gs = GridSpec(nrows=10, ncols=11)
    gs.update(wspace = 0.5, hspace = 0.5)   
    ax = fig.add_subplot(gs[0:10, 0:10])
    
    if type(x) == list and type(y) == list and type(xerr) == list and type(yerr) == list:
        for i in range(len(x)):
            data = ax.scatter(x[i], y[i], s=list(kwargs['s'])[i], ec='k', c=list(kwargs['color'])[i], marker=list(kwargs['marker'])[i], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])

            ax.errorbar(x=x[i], y=y[i], xerr=xerr[i], yerr=yerr[i], ls='None', c='k', zorder=-9)
    else:
        data = ax.scatter(x, y, s=kwargs['s'], ec='k', c=kwargs['color'], marker=kwargs['marker'], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])

        ax.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, ls='None', c='k', zorder=-9)
           
    if contour:
        sns.kdeplot(x=contour_x, y=contour_y, color='gray', fill='True', zorder=-99, ax=ax)
    else:
        pass
    
    xbpt = np.linspace(-2,0, 1000)
    ax.plot(xbpt, rd.bpt_kauffman03(xbpt), c='black', ls='-', lw=3, label='Kauffmann et al. 2003', zorder=-9)
    ax.plot(xbpt, rd.bpt_kewley01(xbpt), c='black', ls=':', lw=3, label='Kewley et al. 2001', zorder=-9)
    ax.axis([-1.75, 0, -0.5, 1.5])
    ax.set_xlabel(r'log([N II]/H$\alpha$)')
    ax.set_ylabel(r'log([O III]/H$\beta$)')
    ax.legend()
    
    if show_colorbar:
        ax_cbar = fig.add_subplot(gs[0:10,10:11])
        fig.colorbar(data, ax_cbar, use_gridspec=True, label = kwargs['cbar_label'])
    if save_path:
        plt.savefig(f'{save_path}')
        
def plot_vo87(x, y, xerr=None, yerr=None, save_path=None, show_colorbar=False, contour=False, contour_x=None, contour_y=None, **kwargs):
    '''
    Generates VO87 diagram given x and y arrays. Can be done with multiple x and y arrays with different markers. 
    '''
    kwargs = scatter_kwargs | kwargs

    fig = plt.figure(figsize = (11, 10))
    gs = GridSpec(nrows=10, ncols=11)
    gs.update(wspace = 0.5, hspace = 0.5)   
    ax = fig.add_subplot(gs[0:10, 0:10])
    
    if type(x) == list and type(y) == list and type(xerr) == list and type(yerr) == list:
        for i in range(len(x)):
            data = ax.scatter(x[i], y[i], s=list(kwargs['s'])[i], ec='k', c=list(kwargs['color'])[i], marker=list(kwargs['marker'])[i], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])
            ax.errorbar(x=x[i], y=y[i], xerr=xerr[i], yerr=yerr[i], ls='None', c='k', zorder=-8)
    else:
        data = ax.scatter(x, y, s=kwargs['s'], ec='k', c=kwargs['color'], marker=kwargs['marker'], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])
        ax.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, ls='None', c='k', zorder=-8)
    
    if contour:
        sns.kdeplot(x=contour_x, y=contour_y, color='gray', fill='True', zorder=-99, ax=ax)
    else:
        pass
           
    xvo87 = np.linspace(-2,-0.1, 1000)
    ax.plot(xvo87, rd.vo87(xvo87), c='black', ls='-', lw=3, label= 'VO87', zorder=-9)
    ax.axis([-1.75, 0, -0.5, 1.5])
    ax.set_xlabel(r'log([S II]/H$\alpha$)')
    ax.set_ylabel(r'log([O III]/H$\beta$)')
    ax.legend()
    
    if show_colorbar:
        ax_cbar = fig.add_subplot(gs[0:10,10:11])
        fig.colorbar(data, ax_cbar, use_gridspec=True, label=kwargs['cbar_label'])
    if save_path:
        plt.savefig(f'{save_path}')
        
def plot_ohno(x, y, xerr=None, yerr=None, save_path=None, show_colorbar=False, contour=False, contour_x=None, contour_y=None, **kwargs):
    '''
    Generates OHNO diagram given x and y arrays. Can be done with multiple x and y arrays with different markers. 
    '''
    kwargs = scatter_kwargs | kwargs
    
    fig = plt.figure(figsize = (11, 10))
    gs = GridSpec(nrows=10, ncols=11)
    gs.update(wspace = 0.5, hspace = 0.5)   
    ax = fig.add_subplot(gs[0:10, 0:10])
    
    if type(x) == list and type(y) == list and type(xerr) == list and type(yerr) == list:
        for i in range(len(x)):
            data = ax.scatter(x[i], y[i], s=list(kwargs['s'])[i], ec='k', c=list(kwargs['color'])[i], marker=list(kwargs['marker'])[i], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])

            ax.errorbar(x=x[i], y=y[i], xerr=xerr[i], yerr=yerr[i], ls='None', c='k', zorder=-8)
    else:
        data = ax.scatter(x, y, s=kwargs['s'], ec='k', c=kwargs['color'], marker=kwargs['marker'], 
                            cmap=kwargs['cmap'], vmin=kwargs['vmin'], vmax=kwargs['vmax'])
        ax.errorbar(x=x, y=y, xerr=xerr, yerr=yerr, ls='None', c='k', zorder=-8)
        
    if contour:
        sns.kdeplot(x=contour_x, y=contour_y, color='gray', fill='True', zorder=-99, ax=ax)
    else:
        pass
    xohno = np.linspace(-2,0.285, 1000)
    ax.plot(xohno, rd.ohno(xohno), c='black', ls='-', lw=3, label='Backhaus et al. 2022 OHNO', zorder=-9)
    ax.axis([-1.75, 1, -0.5, 1.5])
    ax.set_xlabel('log([Ne III]/[O II])')
    ax.set_ylabel(r'log([O III]/H$\beta$)')
    ax.legend()
    
    if show_colorbar:
        ax_cbar = fig.add_subplot(gs[0:10,10:11])
        fig.colorbar(data, ax_cbar, use_gridspec=True, label=kwargs['cbar_label'])
    if save_path:
        plt.savefig(f'{save_path}')

def plot_spectrum_minimalist(x, y, save_path=False):
    fig = plt.figure(figsize = (20 , 10))
    gs = GridSpec(nrows=3, ncols=5)
    gs.update(wspace=0, hspace=0)

    ax = fig.add_subplot(gs[0:3, 0:5])
    ax.plot(x,y, color='k')
    ax.tick_params(labelleft=False, left=False, top=False, right=False)
    ax.minorticks_off()
    ax.axis('off')
    if save_path:
        plt.savefig(f'{save_path}', transparent=True)
