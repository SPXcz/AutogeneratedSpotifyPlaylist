# About
This project contains a library for automated Spotify playlist creation based on one input song.
Search for songs is done through YouTube recomendations by web scraping (Selenium is needed).
This project is inspired by and is partly based on [TheComeUpCode's SpotifyGeneratePlaylist](https://github.com/TheComeUpCode/SpotifyGeneratePlaylist). You can find additional documentation in that repository.

# Installation

1) Download this repository

2) Install needed dependencies by using a CMD command (and preferably update them):     
`pip3 install -r requirements.txt`

3) Download ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and put it into the directory of this project.

4) Get your Spotify token from [here](https://developer.spotify.com/console/post-playlists/) and Spotify user ID (found in your account info).
Pictures below show more info:

[How to find your token](https://github.com/SPXcz/AutogeneratedSpotifyPlaylist/blob/master/SpotifyGeneratePlaylist/images/spotify_token.png)

[How to find your user ID](https://github.com/SPXcz/AutogeneratedSpotifyPlaylist/blob/master/SpotifyGeneratePlaylist/images/userid.png)

<b>Note:</b> You should update your Token time to time. Chosing all options while generating your token is recomended.

# Usage

<h3>Creating new playlist</h3>

To create new playlist use <b>createPlaylist.py</b>. For the program to function you need to add 3 arguments:   

`py createPlaylist.py [Youtube URL of a song] [name of your Spotify playlist] [number of YT pages]`

<ul>
<li><b>Youtube URL of a song</b> - This song is a starting point and the playlist is going to have similar feel to it</li>
<li><b>Name of your Spotify playlist</b> - Name of new Spotify playlist in your account for songs to be added.</li>
<li><b>Number of YT pages</b> - Number of YouTube pages to be searched. One page results in ~7 songs.</li>
</ul>

<h3>Adding songs to already exisitng playlist</h3>

To add new songs to already existing playlist, use <b>createPlaylist.py</b>. For the program to function you need to add 3 arguments:   

`py addToPlaylist.py [Youtube URL of a song] [name of your Spotify playlist] [number of YT pages]`

<ul>
<li><b>Youtube URL of a song</b> - This song is a starting point and the playlist is going to have similar feel to it</li>
<li><b>Name of your Spotify playlist</b> - Name of a Spotify playlist in your account for songs to be added to. Playlist has to exist!</li>
<li><b>Number of YT pages</b> - Number of YouTube pages to be searched. One page results in ~7 songs.</li>
</ul>

This project is in no way affiliated with Spotify dev team.