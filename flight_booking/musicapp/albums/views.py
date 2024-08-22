from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song, Singer, Writer
from .forms import AlbumForm, SongForm, SingerForm, WriterForm
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.generic import ListView

# Home page showing all albums
'''
def album_list(request):
    # Fetch all albums
    albums = Album.objects.all()
    
    # Get the page number from the query parameters, default to 1
    page_number = request.GET.get('page', 1)
    items_per_page = 1  # Set how many albums to display per page
    
    try:
        page_number = int(page_number)
        if page_number < 1:
            raise ValueError
    except ValueError:
        raise Http404("Invalid page number.")
    
    # Calculate the start and end indices for the current page
    start = (page_number - 1) * items_per_page
    end = start + items_per_page
    
    # Slice the queryset to get only the albums for the current page
    paginated_albums = albums[start:end]
    
    # Check if there's a next page
    has_next_page = albums[end:end+1].exists()
    
    # Pass the paginated albums and pagination info to the template
    context = {
        'albums': paginated_albums,
        'page_number': page_number,
        'has_next_page': has_next_page,
    }
    
    return render(request, 'albums/album_list.html', context)

'''
class AlbumListView(ListView):
    model = Album

    def render_to_response(self, context, **response_kwargs):
        data = list(self.get_queryset().values())
        return JsonResponse(data, safe=False)

def album_list(request):
    albums = Album.objects.all()
    paginator = Paginator(albums, 1)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'albums/album_list.html', context)
'''
def album_list(request):
    albums = Album.objects.all()
    paginator = Paginator(albums, 1)  # Paginate albums, 1 per page
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)

    # If the request asks for JSON, return JSON response
    if request.headers.get('Accept') == 'application/json':
        albums_data = list(page_obj.object_list.values())  # Convert albums to list of dicts
        response_data = {
            'albums': albums_data,
            'page': page_obj.number,
            'pages': paginator.num_pages,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
        }
        return JsonResponse(response_data)

    # Otherwise, render the HTML template
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'albums/album_list.html', context)
# Album details page showing all songs in the album
'''

def album_lists(request):
    albums = Album.objects.all()
    # Convert the album objects into a list of dictionaries
    data = list(albums.values())  # .values() returns a QuerySet of dicts
    return JsonResponse(data, safe=False)
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all().order_by('date_created','title')
    #referer = request.META.get('HTTP_REFERER', '/')
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')
    return render(request, 'albums/album_detail.html', {'album': album, 'songs': songs,'previous_page':previous_page})

# Song details page showing singers and writers
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    singers = song.singers.all().order_by('name')
    writers = song.writers.all().order_by('name')   
    referer = request.META.get('HTTP_REFERER', '/')
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')

    return render(request, 'songs/song_detail.html', {'song': song, 'singers': singers, 'writers': writers,'previous_page': previous_page})

# Add, edit, delete views for Album, Song, Singer, Writer
@login_required
@permission_required('album.add_album', raise_exception=True)
def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/album_form.html', {'form': form})
@login_required
@permission_required('album.edit_album', raise_exception=True)
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_form.html', {'form': form})
@login_required
@permission_required('album.delete_album', raise_exception=True)
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'albums/album_confirm_delete.html', {'album': album})

# Similar views for Song
@login_required
@permission_required('song.add_song', raise_exception=True)
def song_add(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'songs/song_form.html', {'form': form})
@login_required
@permission_required('song.edit_song', raise_exception=True)
def song_edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_detail', pk=pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'songs/song_form.html', {'form': form})
@login_required
@permission_required('song.delete_song', raise_exception=True)
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        song.delete()
        return redirect('album_detail', pk=song.album.pk)
    return render(request, 'songs/song_confirm_delete.html', {'song': song})

# Similar views for Singer
@login_required
@permission_required('singer.add_singer', raise_exception=True)
def singer_add(request):
    if request.method == "POST":
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('singer_list')
    else:
        form = SingerForm()
    return render(request, 'singers/singer_form.html', {'form': form})
@login_required
@permission_required('singer.edit_singer', raise_exception=True)
def singer_edit(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('singer_detail', pk=pk)
    else:
        form = SingerForm(instance=singer)
    return render(request, 'singers/singer_form.html', {'form': form})
@login_required
@permission_required('singer.delete_singer', raise_exception=True)
def singer_delete(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    if request.method == "POST":
        singer.delete()
        return redirect('singer_list')
    return render(request, 'singers/singer_confirm_delete.html', {'singer': singer})

# Similar views for Writer
@login_required
@permission_required('writer.add_writer', raise_exception=True)
def writer_add(request):
    if request.method == "POST":
        form = WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('writer_list')
    else:
        form = WriterForm()
    return render(request, 'writers/writer_form.html', {'form': form})
@login_required
@permission_required('writer.edit_writer', raise_exception=True)
def writer_edit(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        form = WriterForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('writer_detail', pk=pk)
    else:
        form = WriterForm(instance=writer)
    return render(request, 'writers/writer_form.html', {'form': form})
@login_required
@permission_required('writer.delete_writer', raise_exception=True)
def writer_delete(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    if request.method == "POST":
        writer.delete()
        return redirect('writer_list')
    return render(request, 'writers/writer_confirm_delete.html', {'writer': writer})
@login_required
@permission_required('singer.add_singer', raise_exception=True)    
def add_singer_to_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            singer = form.save()
            song.singers.add(singer)
            return redirect('song_detail', pk=song_id)
    else:
        form = SingerForm()
        previous_page = request.session.get('previous_page', '/')
    
    return render(request, 'singers/singer_form.html', {'form': form,'previous_page':previous_page})
@login_required
@permission_required('writer.add_writer', raise_exception=True)    
def add_writer_to_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = WriterForm(request.POST)
        if form.is_valid():
            writer = form.save()
            song.writers.add(writer)
            return redirect('song_detail', pk=song_id)
    else:
        form = WriterForm()
        previous_page = request.session.get('previous_page', '/')
    
    return render(request, 'writers/writer_form.html', {'form': form,'previous_page':previous_page})    
def singer_list(request):
    singers = Singer.objects.values('name').distinct().order_by('name')
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')
    return render(request, 'singers/singer_list.html', {'singers': singers,'previous_page':previous_page})

def singer_detail(request, pk):
    singer = get_object_or_404(Singer, pk=pk)
    songs = singer.songs.all()  # Assuming a many-to-many relationship with Song
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')
    return render(request, 'singers/singers_details.html', {'singer': singer, 'songs': songs,'previous_page':previous_page})

def writer_list(request):
    unique_writers = Writer.objects.values('name').distinct().order_by('name')
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')
    context = {
        'writers': unique_writers,
        'previous_page':previous_page
    }
    return render(request, 'writers/writer_list.html',context)

def writer_detail(request, pk):
    writer = get_object_or_404(Writer, pk=pk)
    songs = Song.objects.filter(writers=writer) # Filtering songs by the writer
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    previous_page = request.session.get('previous_page', '/')
    return render(request, 'writers/writers_details.html', {'writer': writer, 'songs': songs,'previous_page':previous_page})

def get_songs_by_singer(request, singer_name):
    singers = Singer.objects.filter(name=singer_name)
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')
    previous_page = request.session.get('previous_page', '/')
    if not singers:
        return render(request, 'albums/no_songs.html', {'singer_name': singer_name})
    songs = Song.objects.filter(singers__in=singers).distinct()
    return render(request, 'singers/songs_by_singer.html', {
        'singer_name': singer_name,
        'songs': songs,
        'singers': singers,
        'previous_page':previous_page
    })    
def get_songs_by_writer(request,writer_name):
    writers=Writer.objects.filter(name=writer_name)
    if 'HTTP_REFERER' in request.META:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')
    previous_page = request.session.get('previous_page', '/')
    if not writers:
        return render(request,'albums/no_songs.html',{'writer_name':writer_name})
    songs=Song.objects.filter(writers__in=writers).distinct()
    return render(request,'writers/song_by_writer.html',{
        'writer_name':writer_name,
        'songs':songs,
        'writers':writers,
        'previous_page':previous_page
    })        

# login view and logout views and all...
def login_view(request):
    if request.user.is_authenticated:
        return redirect('album_list')  # Redirect authenticated users to home

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('album_list')  # Redirect to a home page or dashboard after login
    else:
        form = AuthenticationForm()

    return render(request, 'albums/login.html', {'form': form})    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'albums/signup.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'albums/profile.html')