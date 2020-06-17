import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='0c1ff6bbc21f46cf9bdb819d54b4f6ee',
    client_secret='b97b99df2ec64e2cb7729856ccc77b5a'))

# ATTRIBUTES = ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']
# TO DO: add loudness? has to be normalized to [0,1]

ATTRIBUTES = ['danceability', 'energy', 'acousticness', 'speechiness', 'valence']


def playlist_audio_features_average(playlist):
    playlist_length = playlist['tracks']['total']

    playlist_dict = dict()
    track_ids = []

    for key in ATTRIBUTES:
        playlist_dict[key] = 0

    for track_pager in spotify.playlist_tracks(playlist['id'])['items']:
        try:
            track_ids.append(track_pager['track']['id'])
        except:
            cheese = 0

    analysis = spotify.audio_features(tracks=track_ids)
    for indiv_analysis in analysis:
        try:
            for key in indiv_analysis:
                if key in ATTRIBUTES:
                    playlist_dict[key] += indiv_analysis[key] / playlist_length
        except:
            cheese = 0

    for key in playlist_dict:
        playlist_dict[key] = round(playlist_dict[key], 3)

    return playlist_dict


def get_graphing_data(playlists):
    data = [ATTRIBUTES]
    for playlist in playlists:
        data.append((playlist['name'], playlist_audio_features_average(playlist)))

    return data


SPOTIFY_PLAYLISTS = []
for playlist in spotify.featured_playlists()['playlists']['items']:
    SPOTIFY_PLAYLISTS.append(playlist)

MY_PLAYLISTS = [
    spotify.playlist('4d186dlkoOtfF9r40nxam6'),
    spotify.playlist('4etliHA7sV54hxIzjnGRGS'),
    spotify.playlist('3Id3NdT4RpBLf37MLDrlY0'),
    spotify.playlist('7ERdFnPRd7sf2UzNC5nUEG')
]

TOP_PLAYLIST_DICT = {
    'Global': spotify.playlist('37i9dQZEVXbMDoHDwVN2tF'),  # Global
    'Argentina': spotify.playlist('37i9dQZEVXbMMy2roB9myp'),  # Argentina
    'Australia': spotify.playlist('37i9dQZEVXbJPcfkRz0wJ0'),  # Australia
    'Austria': spotify.playlist('37i9dQZEVXbKNHh6NIXu36'),  # Austria
    'Belgium': spotify.playlist('37i9dQZEVXbJNSeeHswcKB'),  # Belgium
    'Bolivia': spotify.playlist('37i9dQZEVXbJqfMFK4d691'),  # Bolivia
    'Brazil': spotify.playlist('37i9dQZEVXbMXbN3EUUhlg'),  # Brazil
    'Bulgaria': spotify.playlist('37i9dQZEVXbNfM2w2mq1B8'),  # Bulgaria
    'Canada': spotify.playlist('37i9dQZEVXbKj23U1GF4IR'),  # Canada
    'Chile': spotify.playlist('37i9dQZEVXbL0GavIqMTeb'),  # Chile
    'Colombia': spotify.playlist('37i9dQZEVXbOa2lmxNORXQ'),  # Columbia
    'Costa Rica': spotify.playlist('37i9dQZEVXbMZAjGMynsQX'),  # Costa Rica
    'Czech Republic': spotify.playlist('37i9dQZEVXbIP3c3fqVrJY'),  # Czech Republic
    'Denmark': spotify.playlist('37i9dQZEVXbL3J0k32lWnN'),  # Denmark
    'Dominican Republic': spotify.playlist('37i9dQZEVXbKAbrMR8uuf7'),  # Dominican Republic
    'Ecuador': spotify.playlist('37i9dQZEVXbJlM6nvL1nD1'),  # Ecuador
    'El Salvador': spotify.playlist('37i9dQZEVXbLxoIml4MYkT'),  # El Salvador
    'Estonia': spotify.playlist('37i9dQZEVXbLesry2Qw2xS'),  # Estonia
    'Finland': spotify.playlist('37i9dQZEVXbMxcczTSoGwZ'),  # Finland
    'France': spotify.playlist('37i9dQZEVXbIPWwFssbupI'),  # France
    'Germany': spotify.playlist('37i9dQZEVXbJiZcmkrIHGU'),  # Germany
    'Greece': spotify.playlist('37i9dQZEVXbJqdarpmTJDL'),  # Greece
    'Guatemala': spotify.playlist('37i9dQZEVXbLy5tBFyQvd4'),  # Guatemala
    'Honduras': spotify.playlist('37i9dQZEVXbJp9wcIM9Eo5'),  # Honduras
    'Hong Kong': spotify.playlist('37i9dQZEVXbLwpL8TjsxOG'),  # Hong Kong
    'Hungary': spotify.playlist('37i9dQZEVXbNHwMxAkvmF8'),  # Hungary
    'Iceland': spotify.playlist('37i9dQZEVXbKMzVsSGQ49S'),  # Iceland
    'India': spotify.playlist('37i9dQZEVXbLZ52XmnySJg'),  # India
    'Indonesia': spotify.playlist('37i9dQZEVXbObFQZ3JLcXt'),  # Indonesia
    'Ireland': spotify.playlist('37i9dQZEVXbKM896FDX8L1'),  # Ireland
    'Israel': spotify.playlist('37i9dQZEVXbJ6IpvItkve3'),  # Israel
    'Italy': spotify.playlist('37i9dQZEVXbIQnj7RRhdSX'),  # Italy
    'Japan': spotify.playlist('37i9dQZEVXbKXQ4mDTEBXq'),  # Japan
    'Latvia': spotify.playlist('37i9dQZEVXbJWuzDrTxbKS'),  # Latvia
    'Lithuania': spotify.playlist('37i9dQZEVXbMx56Rdq5lwc'),  # Lithuania
    'Luxembourg': spotify.playlist('37i9dQZEVXbKGcyg6TFGx6'),  # Luxembourg
    'Malaysia': spotify.playlist('37i9dQZEVXbJlfUljuZExa'),  # Malaysia
    'Mexico': spotify.playlist('37i9dQZEVXbO3qyFxbkOE1'),  # Mexico
    'Netherlands': spotify.playlist('37i9dQZEVXbKCF6dqVpDkS'),  # Netherlands
    'New Zealand': spotify.playlist('37i9dQZEVXbM8SIrkERIYl'),  # New Zealand
    'Nicaragua': spotify.playlist('37i9dQZEVXbISk8kxnzfCq'),  # Nicaragua
    'Norway': spotify.playlist('37i9dQZEVXbJvfa0Yxg7E7'),  # Norway
    'Panama': spotify.playlist('37i9dQZEVXbKypXHVwk1f0'),  # Panama
    'Paraguay': spotify.playlist('37i9dQZEVXbNOUPGj7tW6T'),  # Paraguay
    'Peru': spotify.playlist('37i9dQZEVXbJfdy5b0KP7W'),  # Peru
    'Philippines': spotify.playlist('37i9dQZEVXbNBz9cRCSFkY'),  # Philippines
    'Poland': spotify.playlist('37i9dQZEVXbN6itCcaL3Tt'),  # Poland
    'Portugal': spotify.playlist('37i9dQZEVXbKyJS56d1pgi'),  # Portugal
    'Romania': spotify.playlist('37i9dQZEVXbNZbJ6TZelCq'),  # Romania
    'Singapore': spotify.playlist('37i9dQZEVXbK4gjvS1FjPY'),  # Singapore
    'Slovakia': spotify.playlist('37i9dQZEVXbKIVTPX9a2Sb'),  # Slovakia
    'South Africa': spotify.playlist('37i9dQZEVXbMH2jvi6jvjk'),  # South Africa
    'Spain': spotify.playlist('37i9dQZEVXbNFJfN1Vw8d9'),  # Spain
    'Sweden': spotify.playlist('37i9dQZEVXbLoATJ81JYXz'),  # Sweden
    'Switzerland': spotify.playlist('37i9dQZEVXbJiyhoAPEfMK'),  # Switzerland
    'Taiwan': spotify.playlist('37i9dQZEVXbMnZEatlMSiu'),  # Taiwan
    'Thailand': spotify.playlist('37i9dQZEVXbMnz8KIWsvf9'),  # Thailand
    'Turkey': spotify.playlist('37i9dQZEVXbIVYVBNw9D5K'),  # Turkey
    'United Kingdom': spotify.playlist('37i9dQZEVXbLnolsZ8PSNw'),  # United Kingdom
    'United States': spotify.playlist('37i9dQZEVXbLRQDuF5jeBp'),  # United States
    'Uruguay': spotify.playlist('37i9dQZEVXbMJJi3wgRbAy'),  # Uruguay
    'Vietnam': spotify.playlist('37i9dQZEVXbLdGSmz6xilI'),  # Vietnam
}

TOP_PLAYLISTS = []
for country in TOP_PLAYLIST_DICT:
    TOP_PLAYLISTS.append(TOP_PLAYLIST_DICT[country])