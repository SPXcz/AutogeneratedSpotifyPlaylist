from selenium import webdriver
import youtube_dl
import re
from time import sleep
from SpotifyGeneratePlaylist.create_playlist import CreatePlaylist
import sys

#Extension of TheComeUpCode's CreatePlaylist class
class YtToSpotify(CreatePlaylist):
    def __init__(self):
        super().__init__()

    #Gets names of songs through YT web scraping which will be added to your playlist
    def getNames(self, no_songs, url, playlist_id):
        self.browserConnect()
        for i in range(0, no_songs):
            url = self.getNameFromYT(url)
            sleep(20)
            self.add_song_to_playlist(playlist_id)
            print("New songs added")
            self.all_song_info = {}
            if(url == None):
                print("Error while finding new song")
                return

        self.browserClose()

    def getNameFromYT(self, youtube_url):
        #Finding and parsing YT URL so we can get name of the song and atrist's name
        self.browser.get(youtube_url)
        sleep(5)
        song_name_scrap = self.browser.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
        song = song_name_scrap.text
        song_parts = song.split(" - ")
        artist = song_parts[0]
        song_parts = re.split('\(|\[', song_parts[1])
        name = song_parts[0]

        #Adds song of this page
        self.addSong(youtube_url, name, artist)

        next_song_scrap = self.browser.find_elements_by_xpath("//*[@id=\"dismissable\"]/div/div[.]/a")
        #Finding next song to be added
        for i in range(2, len(next_song_scrap)):
            song = next_song_scrap[i].text
            song_parts = song.split(" - ")
            if(len(song_parts) < 2):
                continue
            artist = song_parts[0]
            song_parts = re.split('\(|\[',song_parts[1])
            name = song_parts[0]
            #Checking for existance of a song and whether it's been already added
            if((self.get_spotify_uri(name) is not None) and (self.all_song_info.get(name, None) is None)):
                sleep(1)
                curr_url = next_song_scrap[0].get_attribute('href')
                self.addSong(curr_url, name, artist)
        
        return curr_url

    def addSong(self, youtube_url, name, artist):
        #Putting information about the song into an array
        if name is not None and artist is not None:
                # save all important info and skip any missing song and artist
                self.all_song_info[name] = {
                    "youtube_url": youtube_url,
                    "song_name": name,
                    "artist": artist,

                    # add the uri, easy to get song to put into playlist, searches based on the input (string)
                    "spotify_uri": self.get_spotify_uri(name+" "+artist)

                }
                print("Song name: ", name, " by:", artist, " has been added")

    #Open browser and set it up
    def browserConnect(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        self.browser = webdriver.Chrome("chromedriver.exe")

    #Close browser
    def browserClose(self):
        self.browser.close()


def main():
    #Program has 3 arguments: URL of the first song, name of your new playlist, number of YT pages to be examined (1 page is ~ 14 songs)
    if(len(sys.argv) <= 1):
        url = input("URL of seed song: ")
        playlist_name = input("Name of your new playlist: ")
        no_songs = int(input("Number of songs you want to add: "))
    else:
        url = sys.argv[1]
        playlist_name = sys.argv[2]
        no_songs = int(sys.argv[3])

    obj = YtToSpotify()
    # create a new playlist
    playlist_id = obj.create_playlist(playlist_name)
    print("Playlist has been created")
    #Get list of songs
    obj.getNames(no_songs, url, playlist_id)
    print("Playlist has been filled")

main()