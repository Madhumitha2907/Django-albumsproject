import os
import sys
import django
from datetime import timedelta
from django.db.models import Count, Q, F

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicapp.settings')

# Setup Django
django.setup()

# Import models
from albums.models import Album, Song, Singer

# Example 1: Get albums that were either released after 2020 or have a song longer than 5 minutes.
albums = Album.objects.filter(
    Q(release_date__year__gt=2020) | Q(songs__duration__gt=timedelta(minutes=5))
)
print("Albums released after 2020 or with songs longer than 5 minutes:")
for album in albums:
    print(album.title,Song.title)

# Example 2: Get songs where the date_created is the same as the date_updated.
songs = Song.objects.filter(date_created=F('date_updated'))
print("\nSongs where date_created equals date_updated:")
for song in songs:
    print(song.title)

# Example 3: Get albums along with the number of songs in each album.
albums_with_song_count = Album.objects.annotate(song_count=Count('songs'))
print("\nAlbums with the number of songs:")
for album in albums_with_song_count:
    print(f'{album.title}: {album.song_count} songs')

# Example 4: Get singers who have more than 5 songs.
singers = Singer.objects.annotate(song_count=Count('songs')).filter(song_count__gte=2)
print("\nSingers with more than 5 songs:")
for singer in singers:
    print(singer.name)
