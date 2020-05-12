import json
import os
import requests

from SpotifyGeneratePlaylist.exceptions import ResponseException
from SpotifyGeneratePlaylist.secrets import spotify_token, spotify_user_id


class CreatePlaylist:
    def __init__(self):
        self.all_song_info = {}

    def create_playlist(self, playlist_name):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": playlist_name,
            "description": "Autogenerated playlist by SPXcz's AutogeneratedSpotifyPlaylist Github: https://github.com/SPXcz/AutogeneratedSpotifyPlaylist",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != 201:
            raise ResponseException(response.status_code)

        response_json = response.json()

        # playlist id
        return response_json["id"]

    def get_spotify_uri(self, song_name, artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != 200:
            raise ResponseException(response.status_code)

        response_json = response.json()

        songs = response_json["tracks"]["items"]

        #Checking for existance of a song
        if not songs:
            return None
        
        # only use the first song
        uri = songs[0]["uri"]

        return uri

    #Gets an ID of a playlist based on input
    def getPlaylistId(self, playlist_name):
        query = "https://api.spotify.com/v1/me/playlists"

        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

         # check for valid response status
        if response.status_code != 200:
            raise ResponseException(response.status_code)

        response_json = response.json()

        for resp in response_json["items"]:

            set1 = set(resp["name"].split(' '))
            set2 = set(playlist_name.split(' '))

            if(set1 == set2):
                #returns id of playlist we're looking for
                return resp["id"]
        
        #No playlist with such name has been found
        return None

    #gets an array of songs already in a playlist
    def getSongsInPlaylist(self, playlist_id):
        tmp = []
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)

        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        if response.status_code != 200:
            raise ResponseException(response.status_code)

        response_json = response.json()

        for i in range(0, len(response_json["items"])-1):
            tmp.append(response_json["items"][i]["track"]["name"])

        return tmp

    def add_song_to_playlist(self, playlist_id):
        """Add all songs into a new Spotify playlist"""

        # collect all of uri
        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]

        # add all songs into new playlist
        request_data = json.dumps(uris)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != 201:
            print("A problem has occured, trying again")
            return True
            #raise ResponseException(response.status_code)

        #response_json = response.json()
        return False