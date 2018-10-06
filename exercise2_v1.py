class Song:
    def __init__(self, title, artist, album, trackNr):
        self.title = title
        self.artist = artist
        self.album = album
        self.trackNr = trackNr
        
        artist.addSong(self)       
        
    def getArtist(self):
        return self.artist
        
        
        
class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        
        artist.addAlbum(self)
        
    def addTrack(self, song):
        self.tracks.append(song)
        
class Artist:
    def __init__(self, name):
        self.name = name
        
        self.songs = []
        self.albums = []
            
    def addSong(self, song):
        self.songs.append(song)
        
    def addAlbum(self, album):
        self.albums.append(album)
            
class Playlist:
    def __init__(self, name):
        self.name = name
        
        self.track_songs = []
        
    def addTrackSong(self, song):
        self.track_songs.append(song)
        
artist1 = Artist("Norman Laren")
album1 = Album("Album White", artist1, 1990)
s1 = Song("Happiness is today", artist1, album1, 0)
s2 = Song("Sadness is today", artist1, album1, 1)
album1.addTrack(s1)
album1.addTrack(s2)

playlist = Playlist("My songs")

for i in album1.tracks:
    playlist.addTrackSong(i)
    
for i in playlist.track_songs:
    print(i.artist.name)


        
       