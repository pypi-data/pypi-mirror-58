import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

import pandas as pd
import numpy as np

from . import _common


def plot(samples, *, capsules=None, size=None):
    """
    Plots signals/samples via matplotlib, optionally including conditions/
    capsules as shaded regions.

    Parameters
    ----------
    samples : pd.DataFrame
        A DataFrame with a pandas.Timestamp-based index with a column for
        each signal.

    capsules : pd.DataFrame
        A DataFrame with (at minimum) three columns: Condition, Capsule Start
        and Capsule End. Each unique Condition will be plotted as a
        differently-colored shaded region behind the sample data.

    size : str
        This value, if provided, is passed directly to
        matplotlib.rcParams['figure.figsize'] to control the size of the
        rendered plot.
    """
    _common.validate_argument_types([
        (samples, 'samples', pd.DataFrame),
        (capsules, 'capsules', pd.DataFrame),
        (size, 'size', str)
    ])

    if size:
        matplotlib.rcParams['figure.figsize'] = size

    def _convert_to_timestamp(matplotlib_timestamp, matplotlib_axis):
        return pd.Period(ordinal=int(matplotlib_timestamp), freq=matplotlib_axis.freq).to_timestamp()

    ax = samples.plot()

    if capsules is not None:
        unique_conditions = capsules[['Condition']].drop_duplicates()['Condition'].to_list()

        capsule_colors = dict()
        colors = cm.tab10(np.linspace(0, 1, len(unique_conditions)))
        for i in range(0, len(colors)):
            capsule_colors[unique_conditions[i]] = colors[i]

        axis_start_matplotlib, axis_end_matplotlib = ax.get_xlim()
        axis_start = _convert_to_timestamp(axis_start_matplotlib, ax)
        axis_end = _convert_to_timestamp(axis_end_matplotlib, ax)

        for index, capsule in capsules.iterrows():
            color = capsule_colors[capsule['Condition']]
            start = axis_start if pd.isna(capsule['Capsule Start']) else capsule['Capsule Start']
            end = axis_end if pd.isna(capsule['Capsule End']) else capsule['Capsule End']

            ax.axvspan(start, end, facecolor=color, edgecolor=None, alpha=0.3)

    plt.show()
