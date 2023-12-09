from pytube import YouTube
from bs4 import BeautifulSoup
import requests
import os
import numpy as np
import pandas as pd

def get_songs_info():
    song_name=input("Enter a song name(for more songs add ',' at end of every song): ")
    return song_name

def search_youtube():
    url=f"https://www.youtube.com/results?search_query={song_name}"
    response= requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    video_links = []
    for a_tag in soup.find_all("a", attrs={"class": "yt-simple-endpoint style-scope ytd-video-renderer"}):
        video_link = "https://www.youtube.com" + a_tag.get("href")
        video_links.append(video_link)
    
    # Return the list of video links
    return video_links

def download_audio(video_url):
    try:
        youtube_obj = YouTube(video_url)
        audio_stream = youtube_obj.streams.get_audio_only()
        audio_stream.download()
        print(f"Downloaded audio for {youtube_obj.title}")
    except Exception as e:
        print(f"Error downloading audio: {e}")
def save_audio(audio_data,song_name):
    file_name=f"{song_name}.mp3"
    with open(file_name, "wb") as f:
        f.write(audio_data)
    print(f"Saved audio file: {file_name}")

def main():
    song_name = get_songs_info()
    video_links = search_youtube(song_name)
    for video_link in video_links:
        download_audio(video_link)

if __name__ == "__main__":
    main()


