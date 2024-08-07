from pytube import Playlist
playlist_url = input("enter")
playlist = Playlist(playlist_url)

for videos in playlist.videos:
    videos.streams.get_highest_resolution().download()
    