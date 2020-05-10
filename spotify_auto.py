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
    def getNames(self, no_songs, url):
        self.browserConnect()
        for i in range(0, no_songs):
            url = self.getNameFromYT(url)
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

        #Putting information about the song into an array
        if name is not None and artist is not None:
                # save all important info and skip any missing song and artist
                self.all_song_info[name] = {
                    "youtube_url": youtube_url,
                    "song_name": name,
                    "artist": artist,

                    # add the uri, easy to get song to put into playlist
                    "spotify_uri": self.get_spotify_uri(name+" "+artist)

                }
                print("Song name: ", name, " by:", artist, " has been added")

        next_song_scrap = self.browser.find_elements_by_xpath("//*[@id=\"dismissable\"]/div/div[.]/a")
        #Finding next song to be added
        for song_scrap in next_song_scrap:
            song = song_scrap.text
            song_parts = song.split(" - ")
            if(len(song_parts) < 2):
                continue
            artist = song_parts[0]
            song_parts = re.split('\(|\[',song_parts[1])
            name = song_parts[0]
            #Checking for existance of a song and 
            if((self.get_spotify_uri(name) is not None) and (self.all_song_info.get(name, None) is None)):
                return song_scrap.get_attribute('href')
        
        return None

       

    #Open browser and set it up
    def browserConnect(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        self.browser = webdriver.Chrome("chromedriver.exe")

    #Close browser
    def browserClose(self):
        self.browser.close()


def main():
    #Program has 3 arguments: URL of the first song, name of your new playlist, number of songs in your playlist
    if(len(sys.argv) <= 1):
        url = input("URL of seed song: ")
        playlist_name = input("Name of your new playlist: ")
        no_songs = int(input("Number of songs you want to add: "))
    else:
        url = sys.argv[1]
        playlist_name = sys.argv[2]
        no_songs = int(sys.argv[3])

    obj = YtToSpotify()
    #Get list of songs
    obj.getNames(no_songs, url)
    #Add those songs to your playlist
    obj.add_song_to_playlist(playlist_name)

main()