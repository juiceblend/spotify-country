import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

import Playlists
import Comparison


def radar_chart(num_axes, frame = 'polygon'):
    theta = np.linspace(0, 2 * np.pi, num_axes, endpoint=False) #calculate axes angles

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_axes,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_axes))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

#Given data in the form of
# [[axis_labels],
# (playlist1 name, [audio_features1]),
# (playlist2 name, [audio_features2]),
# (playlist3 name, [audio_features3])]

def make_radar_chart(data, chart_title):

    spoke_labels = data.pop(0)
    theta = radar_chart(len(spoke_labels), frame='circle')


    fig, axes = plt.subplots(figsize=(10, 5), nrows=1, ncols=1,
                             subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['g', 'y', 'b', 'r', 'm']
    # Plot the four cases from the example data on separate axes
    axes.set_rgrids([0.2, 0.4, 0.6, 0.8])

    labels = []
    for (title, case_data), color in zip(data, colors):
        labels.append(title)
        case_data_array = []
        for key in case_data:
            case_data_array.append(case_data[key])
        axes.plot(theta, case_data_array, color=color)
        axes.fill(theta, case_data_array, facecolor=color, alpha=0.25)
    axes.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    legend = axes.legend(labels, loc=(0.9, .95),
                         labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, chart_title,
             horizontalalignment='center', color='black', weight='bold',
             size='large')


def make_comparison_chart(country):

    if country not in Playlists.TOP_PLAYLIST_DICT:
        print("Not a valid country")
        return

    x = np.linspace(0, len(Playlists.TOP_PLAYLISTS)-2, len(Playlists.TOP_PLAYLISTS)-1)

    data = Comparison.get_country_comparisons(country)
    numbers = []
    labels = []
    for pair in data:
        labels.append(pair[0])
        numbers.append(pair[1])
    # print(numbers) debug
    plot_numbers = [(-1)*np.log(float(i)) for i in numbers]

    plt.figure(figsize=(12,5))
    plt.bar(x, plot_numbers)  # Plot some data on the (implicit) axes.

    plt.ylim(ymin=0)
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.xticks(x, labels, rotation='vertical')
    plt.yticks(np.arange(0, 4.5, 0.5))
    plt.title("Similarity Data for " + country)

    plt.tight_layout()




