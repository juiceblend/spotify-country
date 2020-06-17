import Playlists
import Chart
import Comparison

# Make Radar chart
Chart.make_radar_chart(Playlists.get_graphing_data(
    [Playlists.TOP_PLAYLIST_DICT['Malaysia'],
        Playlists.TOP_PLAYLIST_DICT['Israel']]),
    'Malaysia and Israel')


# Make Comparison chart
Chart.make_comparison_chart("Malaysia")
Chart.plt.show()


# Print Comparison Data
# Comparison.print_comparisons(Playlists.TOP_PLAYLISTS)
