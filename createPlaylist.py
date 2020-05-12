from spotify_auto import YtToSpotify
import sys

def main():
    #Program has 3 arguments: URL of the first song, name of your new playlist, number of YT pages to be examined (1 page is ~ 7 songs)
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