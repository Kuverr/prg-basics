# class definition
class Song:
    def __init__(self,author,title,album,year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year

    def __str__ (self):
        return f'Author: {self.author}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}'

# object creation
song1 = Song('Ed Sheeran', "asd", 'zcx', '2222')
song2 = Song('Queen', "asd", 'zcx', '2122')

## object usage
print(song1)
print(song2)