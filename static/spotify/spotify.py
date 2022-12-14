import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from search.models import Music

cid = 'f51d2425b3654997b816dc838de321d9'
secret = '8db96243df26412388227c064fcc5210'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
album_cover = []
for i in range(0, 950, 50):
    track_results = sp.search(q='year:2022', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        album_cover.append(t['album']['images'][0]['url'])
        # The below model inserting only needed to be done one to insert the 950 songs. Do not uncomment or it will add more.
        # p = Music(music_title=t['name'], music_artist=t['artists'][0]['name'], music_picture=t['album']['images'][0]['url'])
        # p.save()

