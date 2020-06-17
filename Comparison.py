import Playlists
from math import sqrt


def get_comparisons(playlists):
    temp_data = []
    for playlist in playlists:
        temp_data.append((playlist['name'], Playlists.playlist_audio_features_average(playlist)))
    comparison_list = []
    for index1 in range(len(temp_data)):
        for index2 in range(index1):
            distance = 0
            for key in Playlists.ATTRIBUTES:
                score1 = temp_data[index1][1][key]
                score2 = temp_data[index2][1][key]

                distance += (score1 - score2) ** 2
            distance = round(sqrt(distance), 4)

            comparison_list.append((temp_data[index1][0], temp_data[index2][0], distance))

    return comparison_list


def comparison_sort_helper(data):
    return data[2]



def sort_comparison_list(list):
    list.sort(key=comparison_sort_helper)


def print_comparisons(playlists):
    comparisons = get_comparisons(playlists)
    sort_comparison_list(comparisons)
    comparisons = [str(i) for i in comparisons]

    f = open("Country_Comparisons.txt", "w")
    for data in comparisons:
        f.write(data + '\n')

    f.close()


def get_country_comparisons(country):
    comparisons = []
    with open("Country_Comparisons.txt", "r") as reader:
        lines = reader.readlines()
    # print(lines) debug
    for line in lines:
        if country in line:
            other_country = ''
            for key in Playlists.TOP_PLAYLIST_DICT:
                if key != country:
                    if key in line:
                        other_country = key
            parts = line.split(',')
            parts[2] = parts[2].replace(' ', '')
            parts[2] = parts[2].replace(')', '')
            parts[2] = parts[2].replace('\n', '')
            comparisons.append((other_country, parts[2]))

    return comparisons
