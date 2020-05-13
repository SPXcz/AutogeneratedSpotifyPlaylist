from spotify_auto import YtToSpotify
import sys

def main():
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
    playlist_id = obj.getPlaylistId(playlist_name)
    if(playlist_id is None):
        print("Playlist hasn't been found")
        return
    print("Playlist has been found")

    duplicateSongs = obj.getSongsInPlaylist(playlist_id)

    obj.names = obj.getSongsInPlaylist(playlist_id)[:]

    #Get list of songs
    obj.getNames(no_songs, url, playlist_id)
    print("Playlist has been filled")

main()