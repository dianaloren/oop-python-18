class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        
    def getName(self):
        return self.name
        
    def changeName(self, name):
        self.name = name
        
    def addAlbum(self, album):
        self.albums.append(album)
        
    def getAlbums(self):
        return self.albums
    

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
    def getTitle(self):
        return self.title
    
    def changeTitle(self, title):
        self.title = title
        
    def getArtist(self):
        return self.artist
        
class Album:
    def __init__(self, title, year, artistName, songName):
        self.title = title
        self.year = year        
        
        self.artist = Artist(artistName)    #Composition      
        self.songs = []
        
    def getName(self):
        return self.name
    
    def getYear(self):
        return self.year
        
    def addSongs(self, song):
        self.songs.append(Song(songName, artist))
        
    def getArtist(self):
        return self.artist.getName()
        
    def getSongs(self):
        return self.songs
        
class Playlist:
    def __init__(self, nameList):
        self.name = nameList
        self.songs = []
        
    def getName(self):
        return self.name
    
    def changeName(self, name):
        self.name = name
        
    def addSong(self, song):
        self.songs.append(song)
        
#In Action
artist1 = Artist("Elton John")
artist2 = Artist("Sinead OConnor")
artist3 = Artist("Santana")
artist4 = Artist("Luciano Pavarotti")

song11 = Song("Song 1", artist1)
song12 = Song("Song 2", artist1)
song13 = Song("Song 3", artist1)

album1 = Album()


