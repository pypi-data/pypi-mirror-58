# plotting.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

import matplotlib as mpl
import matplotlib.backends.backend_pdf as mplpdf
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

try:
    from labellines import labelLines
    _LABELLINES_ENABLED = True
except ImportError:
    _LABELLINES_ENABLED = False

import scqubits.utils.constants as constants
from scqubits.utils.misc import process_which
from scqubits.settings import DEFAULT_ENERGY_UNITS

mpl.rcParams['font.sans-serif'] = "Arial"
mpl.rcParams['font.family'] = "sans-serif"
mpl.rcParams['figure.dpi'] = 150


def _process_options(axes, x_range=None, y_range=None, xlabel=None, ylabel=None, title=None):
    if x_range is not None:
        axes.set_xlim(x_range)
    if y_range is not None:
        axes.set_ylim(y_range)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_title(title)


def wavefunction1d(wavefunc, potential_vals=None, offset=0, scaling=None, xlabel='phi', ylabel='wavefunction',
                   x_range=None, y_range=None, title=None, fig_ax=None, filename=None, **kwargs):
    """
    Plots the amplitude of a real-valued 1d wave function, along with the potential energy if provided.

    Parameters
    ----------
    wavefunc: WaveFunction object
        basis and amplitude data of wave function to be plotted
    potential_vals: array of float
        potential energies, array length must match basis array of `wavefunc`
    offset: float
        y-offset for the wave function (e.g., shift by eigenenergy)
    scaling: float, optional
        scaling factor for wave function amplitudes
    ylabel: str
        y-axis label
    xlabel: str
        x-axis label
    x_range: (float, float)
        plot range for x-axis
    y_range: (float, float)
        plot range for y-axis
    title: str, optional
        plot title
    filename: str, optional
        file path and name (not including suffix) for output
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition
    **kwargs:
        keyword arguments passed on to axes.plot()

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    fig, axes = fig_ax or plt.subplots()

    scaling = scaling or 1
    x_vals = wavefunc.basis_labels
    y_vals = offset + scaling * wavefunc.amplitudes
    offset_vals = [offset] * len(x_vals)

    if potential_vals is not None:
        axes.plot(x_vals, potential_vals, color='gray')
    axes.plot(x_vals, y_vals, **kwargs)
    axes.fill_between(x_vals, y_vals, offset_vals, where=(y_vals != offset_vals), interpolate=True)
    _process_options(axes, x_range, y_range, xlabel, ylabel, title)

    if filename:
        out_file = mplpdf.PdfPages(filename)
        out_file.savefig()
        out_file.close()

    return fig, axes


def wavefunction1d_discrete(wavefunc, xlabel='x', ylabel='wavefunction', x_range=None, y_range=None, title=None,
                            filename=None, fig_ax=None, **kwargs):
    """
    Plots the amplitude of a real-valued 1d wave function in a discrete basis. (Example: transmon in the charge basis.)

    Parameters
    ----------
    wavefunc: WaveFunction object
        basis and amplitude data of wave function to be plotted
    x_range: tupel(int, int)
        lower and upper bound for values on the x axis
    y_range: (float, float)
        plot range for y-axis
    xlabel: str
        x-axis label
    ylabel: str
        y-axis label
    title: str, optional
        plot title
    filename: str, optional
        file path and name (not including suffix)
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition
    **kwargs:
        keyword arguments passed on to axes.plot()


    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    fig, axes = fig_ax or plt.subplots()

    x_vals = wavefunc.basis_labels
    width = .75

    axes.bar(x_vals, wavefunc.amplitudes, width=width, **kwargs)
    axes.set_xticks(x_vals + width / 2)
    axes.set_xticklabels(x_vals)
    _process_options(axes, x_range, y_range, xlabel, ylabel, title)

    if filename:
        out_file = mplpdf.PdfPages(filename)
        out_file.savefig()
        out_file.close()

    return fig, axes


def wavefunction2d(wavefunc, figsize=(8, 3), zero_calibrate=False, filename=None, fig_ax=None):
    """
    Creates a density plot of the amplitude of a real-valued wave function in 2 "spatial" dimensions.

    Parameters
    ----------
    wavefunc: WaveFunctionOnGrid object
        basis and amplitude data of wave function to be plotted
    figsize: tuple(float, float)
        width, height in inches
    zero_calibrate: bool, optional
        whether to calibrate plot to zero amplitude
    filename: str, , optional
        file path and name (not including suffix)
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    fig, axes = fig_ax or plt.subplots(figsize=figsize)

    min_vals = wavefunc.gridspec.min_vals
    max_vals = wavefunc.gridspec.max_vals

    if zero_calibrate:
        absmax = np.amax(np.abs(wavefunc.amplitudes))
        imshow_minval = -absmax
        imshow_maxval = absmax
        cmap = plt.get_cmap('PRGn')
    else:
        imshow_minval = np.min(wavefunc.amplitudes)
        imshow_maxval = np.max(wavefunc.amplitudes)
        cmap = plt.cm.viridis

    im = axes.imshow(wavefunc.amplitudes, extent=[min_vals[0], max_vals[0], min_vals[1], max_vals[1]],
                     cmap=cmap, vmin=imshow_minval, vmax=imshow_maxval, origin='lower', aspect='auto')
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="2%", pad=0.05)
    fig.colorbar(im, cax=cax)

    if filename:
        out_file = mplpdf.PdfPages(filename)
        out_file.savefig()
        out_file.close()

    return fig, axes


def contours(x_vals, y_vals, func, contour_vals=None, show_colorbar=True, figsize=None, filename=None,
             fig_ax=None):
    """Contour plot of a 2d function `func(x,y)`.

    Parameters
    ----------
    x_vals: (ordered) list
        x values for the x-y evaluation grid
    y_vals: (ordered) list
        y values for the x-y evaluation grid
    func: function f(x,y)
        function for which contours are to be plotted
    contour_vals: list of float, optional
        contour values can be specified if so desired
    show_colorbar: bool, optional
    figsize: tuple(float, float), optional
        figure size
    filename: str, optional
        file path and name (not including suffix)
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """

    x_grid, y_grid = np.meshgrid(x_vals, y_vals)
    z_array = func(x_grid, y_grid)

    if fig_ax is None:
        if figsize is None:
            aspect_ratio = (y_vals[-1] - y_vals[0]) / (x_vals[-1] - x_vals[0])
            figsize = (8, 8 * aspect_ratio)
        fig, axes = plt.subplots(figsize=figsize)
    else:
        fig, axes = fig_ax

    im = axes.contourf(x_grid, y_grid, z_array, levels=contour_vals, cmap=plt.cm.viridis, origin="lower")

    if show_colorbar:
        divider = make_axes_locatable(axes)
        cax = divider.append_axes("right", size="2%", pad=0.05)
        fig.colorbar(im, cax=cax)

    if filename:
        out_file = mplpdf.PdfPages(filename)
        out_file.savefig()
        out_file.close()

    return fig, axes


def matrix(data_matrix, mode='abs', xlabel='', ylabel='', zlabel='', filename=None, fig_ax=None):
    """
    Create a "skyscraper" plot and a 2d color-coded plot of a matrix.

    Parameters
    ----------
    data_matrix: ndarray of float or complex
        2d matrix data
    mode: str from `constants.MODE_FUNC_DICT`
        choice of processing function to be applied to data
    xlabel, ylabel, zlabel: str, optional
    filename: str, optional
        file path and name (not including suffix)
    fig_ax: tuple(Figure, (Axes, Axes)), optional
        fig and ax objects for matplotlib figure addition

    Returns
    -------
    Figure, (Axes1, Axes2)
        figure and axes objects for further editing
    """
    if fig_ax is None:
        fig = plt.figure(figsize=(10, 5))
        ax1 = fig.add_subplot(1, 2, 1, projection='3d')
        ax2 = plt.subplot(1, 2, 2)
    else:
        fig, (ax1, ax2) = fig_ax

    matsize = len(data_matrix)
    element_count = matsize ** 2  # num. of elements to plot

    xgrid, ygrid = np.meshgrid(range(matsize), range(matsize))
    xgrid = xgrid.T.flatten() - 0.5  # center bars on integer value of x-axis
    ygrid = ygrid.T.flatten() - 0.5  # center bars on integer value of y-axis

    zbottom = np.zeros(element_count)  # all bars start at z=0
    dx = 0.75 * np.ones(element_count)  # width of bars in x-direction
    dy = dx  # width of bars in y-direction (same as x-direction)

    modefunction = constants.MODE_FUNC_DICT[mode]
    zheight = modefunction(data_matrix).flatten()  # height of bars from matrix elements
    nrm = mpl.colors.Normalize(0, max(zheight))  # <-- normalize colors to max. data
    colors = plt.cm.viridis(nrm(zheight))  # list of colors for each bar

    # skyscraper plot
    ax1.view_init(azim=210, elev=23)
    ax1.bar3d(xgrid, ygrid, zbottom, dx, dy, zheight, color=colors)
    ax1.axes.w_xaxis.set_major_locator(plt.IndexLocator(1, -0.5))  # set x-ticks to integers
    ax1.axes.w_yaxis.set_major_locator(plt.IndexLocator(1, -0.5))  # set y-ticks to integers
    ax1.set_zlim3d([0, max(zheight)])
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_zlabel(zlabel)

    # 2d plot
    ax2.matshow(modefunction(data_matrix), cmap=plt.cm.viridis)

    cax, _ = mpl.colorbar.make_axes(ax2, shrink=.75, pad=.02)  # add colorbar with normalized range
    _ = mpl.colorbar.ColorbarBase(cax, cmap=plt.cm.viridis, norm=nrm)

    if filename:
        out_file = mplpdf.PdfPages(filename)
        out_file.savefig()
        out_file.close()

    return fig, (ax1, ax2)


def data_vs_paramvals(xdata, ydata, x_range=None, ymax=None, xlabel=None, ylabel=None, title=None, label_list=None,
                      filename=None, fig_ax=None, **kwargs):
    """Plot of a set of yadata vs xdata.
    The individual points correspond to the a provided array of parameter values.

    Parameters
    ----------
    xdata, ydata: ndarray
        must have compatible shapes for matplotlib.pyplot.plot
    x_range: tuple(float, float), optional
        custom x-range for the plot
    ymax: float, optional
        custom maximum y value for the plot
    xlabel, ylabel: str, optional
        optional labels for x and y axis
    filename: str, optional
        write graphics and parameter set to file if path and filename are specified
    title: str, optional
        plot title
    label_list: list(str), optional
        list of labels associated with the individual curves to be plotted
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition
    **kwargs:
        keyword arguments passed on to axes.plot()

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    fig, axes = fig_ax or plt.subplots()

    if ymax:
        ymin, _ = axes.get_ylim()
        ymin = ymin - (ymax - ymin) * 0.05
        y_range = (ymin, ymax)
    else:
        y_range = None

    if label_list is None:
        axes.plot(xdata, ydata, **kwargs)
    else:
        for idx, ydataset in enumerate(ydata.T):
            axes.plot(xdata, ydataset, label=label_list[idx], **kwargs)
        axes.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    _process_options(axes, x_range, y_range, xlabel, ylabel, title)

    if filename:
        out_file = mplpdf.PdfPages(filename + '.pdf')
        out_file.savefig()
        out_file.close()

    return fig, axes


def evals_vs_paramvals(specdata, which=-1, x_range=None, ymax=None, subtract_ground=False, filename=None,
                       title=None, label_list=None, fig_ax=None, **kwargs):
    """Generates a simple plot of a set of eigenvalues as a function of one parameter.
    The individual points correspond to the a provided array of parameter values.

    Parameters
    ----------
    specdata: SpectrumData
        object includes parameter name, values, and resulting eigenenergies
    which: int or list(int)
        number of desired eigenvalues (sorted from smallest to largest); default: -1, signals all eigenvalues
        or: list of specific eigenvalues to include
    x_range: (float, float)
        custom x-range for the plot
    ymax: float, optional
        custom maximum y value for the plot
    subtract_ground: bool
        whether to subtract the ground state energy
    filename: str
        write graphics and parameter set to file if path and filename are specified
    title: str, optional
        plot title
    label_list: list(str), optional
        list of labels associated with the individual curves to be plotted
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition
    **kwargs:
        keyword arguments passed on to axes.plot()

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    index_list = process_which(which, specdata.energy_table[0].size)

    xdata = specdata.param_vals
    ydata = specdata.energy_table[:, index_list]
    if subtract_ground:
        ydata = (ydata.T - ydata[:, 0]).T

    xlabel = specdata.param_name
    ylabel = 'energy [{}]'.format(DEFAULT_ENERGY_UNITS)

    return data_vs_paramvals(xdata, ydata, xlabel=xlabel, ylabel=ylabel, x_range=x_range, ymax=ymax, title=title,
                             label_list=label_list, filename=filename, fig_ax=fig_ax, **kwargs)


def matelem_vs_paramvals(specdata, select_elems=4, mode='abs', x_range=None, y_range=None, xlabel=None, ylabel=None,
                         title=None, filename=None, fig_ax=None, **kwargs):
    """Generates a simple plot of matrix elements as a function of one parameter.
    The individual points correspond to the a provided array of parameter values.

    Parameters
    ----------
    specdata: SpectrumData
        object includes parameter name, values, and matrix elements
    select_elems: int or list
        either maximum index of desired matrix elements, or list [(i1, i2), (i3, i4), ...] of index tuples
        for specific desired matrix elements
    mode: str from `constants.MODE_FUNC_DICT`, optional
        choice of processing function to be applied to data (default value = 'abs')
    x_range: (float, float), optional
        custom x-range for the plot
    y_range: (float, float), optional
        custom y-range for the plot
    xlabel, ylabel: str, optional
        axes labels
    title: str, optional
        plot title
    filename: str, optional
        write graphics and parameter set to file if path and filename are specified
    fig_ax: tuple(Figure, Axes), optional
        fig and ax objects for matplotlib figure addition
    **kwargs:
        keyword arguments passed on to axes.plot()

    Returns
    -------
    tuple(Figure, Axes)
        matplotlib objects for further editing
    """
    fig, axes = fig_ax or plt.subplots()
    xlabel = xlabel or specdata.param_name
    ylabel = ylabel or 'matrix_element'
    _process_options(axes, x_range, y_range, xlabel, ylabel, title)

    modefunction = constants.MODE_FUNC_DICT[mode]
    x = specdata.param_vals

    if isinstance(select_elems, int):
        for row in range(select_elems):
            for col in range(row + 1):
                y = modefunction(specdata.matrixelem_table[:, row, col])
                axes.plot(x, y, label=str(row) + ',' + str(col), **kwargs)
    else:
        for index_pair in select_elems:
            y = modefunction(specdata.matrixelem_table[:, index_pair[0], index_pair[1]])
            axes.plot(x, y, label=str(index_pair[0]) + ',' + str(index_pair[1]), **kwargs)

    if _LABELLINES_ENABLED:
        labelLines(axes.get_lines(), zorder=2.0)
    else:
        axes.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    if filename:
        out_file = mplpdf.PdfPages(filename + '.pdf')
        out_file.savefig()
        out_file.close()

    return fig, axes


def print_matrix(matrix, show_numbers=True, fig_ax=None, **kwargs):
    """Pretty print a matrix, optionally printing the numerical values of the data.
    """
    fig, axes = fig_ax or plt.subplots()

    m = axes.matshow(matrix, cmap=plt.cm.viridis, interpolation='none', **kwargs)
    fig.colorbar(m, ax=axes)

    if show_numbers:
        for y_index in range(matrix.shape[0]):
            for x_index in range(matrix.shape[1]):
                axes.text(x_index, y_index, "{:.03f}".format(matrix[y_index, x_index]),
                          va='center', ha='center', fontsize=8, rotation=45, color='white')
    # shift the grid
    for axis, locs in [(axes.xaxis, np.arange(matrix.shape[1])), (axes.yaxis, np.arange(matrix.shape[0]))]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=locs)
    axes.grid(True, which='minor')
    axes.grid(False, which='major')

    return fig, axes


def spectrum_with_matrixelement(spectrum_data, matrixelement_table, param_name='external parameter',
                                energy_name='energy [{}]'.format(DEFAULT_ENERGY_UNITS),
                                matrixelement_name='matrix element',
                                norm_range=None, x_range=None, y_range=None, colormap='jet',
                                figsize=(15, 10), line_width=2):
    """Takes a list of x-values,
    a list of lists with each element containing the y-values corresponding to a particular curve,
    a list of lists with each element containing the external parameter value (t-value)
    that determines the color of each curve at each y-value,
    and a normalization interval for the t-values."""
    fig = plt.figure(figsize=figsize)

    if norm_range is None:
        norm_range = (np.min(matrixelement_table), np.max(matrixelement_table))

    for i in range(len(spectrum_data.energy_table[0])):
        pts = np.array([spectrum_data.param_vals, spectrum_data.energy_table[:, i]]).T.reshape(-1, 1, 2)
        segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
        line_collection = mpl.collections.LineCollection(segs, cmap=plt.get_cmap(colormap),
                                                         norm=plt.Normalize(*norm_range))
        line_collection.set_array(matrixelement_table[:, i])
        line_collection.set_linewidth(line_width)
        plt.gca().add_collection(line_collection)

    plt.xlabel(param_name)
    plt.ylabel(energy_name)
    if not x_range:
        x_range = [np.amin(spectrum_data.param_vals), np.amax(spectrum_data.param_vals)]
    if not y_range:
        y_range = [np.amin(spectrum_data.energy_table), np.max(spectrum_data.energy_table)]

    plt.xlim(*x_range)
    plt.ylim(*y_range)

    axcb = fig.colorbar(line_collection)
    axcb.set_label(matrixelement_name)
    return fig, axcb
