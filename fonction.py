import os
import requests
from pytubefix import Channel
from moviepy.editor import VideoFileClip
from picture_resize import resize_image
import re


def clean_file(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_process(channel_url, base_directory='downloads', videos_limit=3):
    #DOWNLOAD 
    channel = Channel(channel_url)
    channel_name_clean = clean_file(channel.channel_name)
    print(f'\n--- DOWNLOADING VIDEOS FROM --- \n{channel.channel_name}')

    # CREATION PATH
    base_directory = os.path.join(base_directory, channel_name_clean)
    os.makedirs(base_directory, exist_ok=True)

    #INIT LIMIT VD
    video_cpt = 0
    metadata_file = os.path.join(base_directory, 'channel_url.txt')
    with open(metadata_file, 'w', encoding='utf-8') as file:
        file.write(f'--- CHANNEL URL --- \n{channel_url}\n')

    for video in channel.videos:
        if video_cpt >= videos_limit:
            print(f'\n--- END DOWNLOADING VIDEOS FROM --- \n{channel.channel_name}')
            break

        try:
            clean_title = clean_file(video.title)
            print(f'\n--- DOWNLOADING --- \nProd_{video_cpt + 1}')

            # INIT REPO
            video_directory = os.path.join(base_directory, f'Prod_{video_cpt + 1}')
            os.makedirs(video_directory, exist_ok=True)

            # DOWNLOAD VD
            video_download = video.streams.filter(progressive=True, file_extension='mp4').first()
            temp_video_path = video_download.download(output_path=video_directory)
            # EXTRACT MP3
            v_clip = VideoFileClip(temp_video_path)
            mp3_output = os.path.join(video_directory, f'audio.mp3')
            v_clip.audio.write_audiofile(mp3_output)

            v_clip.close()
            os.remove(temp_video_path)

            #DOWNLOAD COVER
            cover_url = video.thumbnail_url
            response = requests.get(cover_url)
            cover_output_path = os.path.join(video_directory, f'cover.jpg')

            with open(cover_output_path, 'wb') as file:
                file.write(response.content)
            # Resize and crop cover to square
            resize_image(cover_output_path, cover_output_path)

            # METADATA
            metadata_file = os.path.join(video_directory, 'metadata.txt')
            with open(metadata_file, 'w', encoding='utf-8') as file:
                file.write(f'--- VIDEO URL --- \n{video.watch_url}\n')
                file.write(f'\n--- TITLE --- \n{clean_title}\n')
                file.write(f'\n--- DESCRIPTION --- \n{video.description}\n')
                file.write('-' * 50 + '\n')
            video_cpt += 1 
        except Exception as e:
            print(f"Error processing {video.title} : {str(e)}")
            continue
