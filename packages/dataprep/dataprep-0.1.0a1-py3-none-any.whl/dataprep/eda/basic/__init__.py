"""
    This module implements the plot(df) function.
"""

from typing import Optional, Tuple, Union

import dask.dataframe as dd
import pandas as pd
from bokeh.io import show
from bokeh.plotting import Figure

from .compute import compute
from .render import render


def plot(
    df: Union[pd.DataFrame, dd.DataFrame],
    x: Optional[str] = None,
    y: Optional[str] = None,
    *,
    bins: int = 10,
    ngroups: int = 10,
    largest: bool = True,
    bandwidth: float = 1.5,
    sample_size: int = 1000,
    value_range: Optional[Tuple[float, float]] = None,
    yscale: str = "linear",
    tile_size: Optional[float] = None,
    show_plot: bool = True,
) -> Figure:
    """Generates plots for exploratory data analysis.

    If col_x and col_y are unspecified, the distribution of
    each coloumn is plotted. A histogram is plotted if the
    column contains numerical values, and a bar chart is plotted
    if the column contains categorical values.

    If col_x is specified and col_y is unspecified, the
    distribution of col_x is plotted in various ways. If col_x
    contains categorical values, a bar chart and pie chart are
    plotted. If col_x contains numerical values, a histogram,
    kernel density estimate plot, box plot, and qq plot are plotted.

    If col_x and col_y are specified, plots depicting
    the relationship between the variables will be displayed. If
    col_x and col_y contain numerical values, a scatter plot, hexbin
    plot, and binned box plot are plotted. If one of col_x and col_y
    contain categorical values and the other contains numerical values,
    a box plot and multi-line histogram are plotted. If col_X and col_y
    contain categorical vales, a nested bar chart, stacked bar chart, and
    heat map are plotted.

    Parameters:
    ----------
    df : Union[pd.DataFrame, dd.DataFrame]
        Dataframe from which plots are to be generated
    x : str, optional, default None
        A valid column name from the dataframe.
    y : str, optional, default None
        A valid column name from the dataframe.
    bins : int, default 10
        For a histogram or box plot with numerical x axis, it defines
        the number of equal-width bins to use when grouping.
    ngroups : int, default 10
        When grouping over a categorical column, it defines the
        number of groups to show in the plot. Ie, the number of
        bars to show in a bar chart.
    largest : bool, default True
        If true, when grouping over a categorical column, the groups
        with the largest count will be output. If false, the groups
        with the smallest count will be output.
    bandwidth : float, default 1.5
        Bandwidth for the kernel density estimation.
    sample_size : int, default 1000
        Sample size for the scatter plot.
    value_range : (float, float), optional, default None
        The lower and upper bounds on the range of a numerical column.
        Applies when column x is specified and column y is unspecified.
    yscale: str, default "linear"
        The scale to show on the y axis. Can be "linear" or "log".
    tile_size : Optional[float] = None
        Size of the tile for the hexbin plot. Measured from the middle
        of a hexagon to its left or right corner.
    show_plot: bool, default True
        Whether or not to show the plot.

    Returns
    -------
    An object of figure or
        An object of figure and
        An intermediate representation for the plots of different columns in the data_frame.

    Examples
    --------
    >>> import pandas as pd
    >>> from dataprep.eda import *
    >>> iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    >>> plot(iris)
    >>> plot(iris, "petal_length", bins=20, value_range=(1,5))
    >>> plot(iris, "petal_width", "species")
    """

    intermediate = compute(
        df,
        x=x,
        y=y,
        bins=bins,
        ngroups=ngroups,
        largest=largest,
        bandwidth=bandwidth,
        sample_size=sample_size,
        value_range=value_range,
    )
    figure = render(intermediate, yscale=yscale, tile_size=tile_size)
    if show_plot:
        show(figure)
    return figure
