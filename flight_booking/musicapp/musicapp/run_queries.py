from django.core.management.base import BaseCommand
from myapp.models import Album, Song, Singer, Writer
from django.db.models import Q, F, Count

class Command(BaseCommand):
    help = 'Run multiple queries and print the results'

    def handle(self, *args, **kwargs):
        # Example 1: Get albums that were either released after 2020 or have a song longer than 5 minutes.
        albums = Album.objects.filter(
            Q(release_date__year__gt=2020) | Q(songs__duration__gt="00:05:00")
        )
        self.stdout.write("Albums released after 2020 or with songs longer than 5 minutes:")
        for album in albums:
            self.stdout.write(album.title)

        # Example 2: Get songs where the date_created is the same as the date_updated.
        songs = Song.objects.filter(date_created=F('date_updated'))
        self.stdout.write("\nSongs where date_created equals date_updated:")
        for song in songs:
            self.stdout.write(song.title)

        # Example 3: Get albums along with the number of songs in each album.
        albums_with_song_count = Album.objects.annotate(song_count=Count('songs'))
        self.stdout.write("\nAlbums with the number of songs:")
        for album in albums_with_song_count:
            self.stdout.write(f'{album.title}: {album.song_count} songs')

        # Example 4: Get singers who have more than 5 songs.
        singers = Singer.objects.annotate(song_count=Count('songs')).filter(song_count__gt=5)
        self.stdout.write("\nSingers with more than 5 songs:")
        for singer in singers:
            self.stdout.write(singer.name)

        # Add more queries as needed...
