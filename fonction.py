import os
import requests
from pytubefix import Channel
from moviepy.editor import VideoFileClip
import shutil
from picture_resize import resize_image
import re


def clean_file(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_process(channel_url, base_directory='downloads', videos_limit=3):
    #DOWNLOAD 
    channel = Channel(channel_url)
    channel_name_clean = clean_file(channel.channel_name)
    print(f'Le nom de la chaîne est : {channel.channel_name}')

    # CREATION PATH
    base_directory = os.path.join(base_directory, channel_name_clean)
    os.makedirs(base_directory, exist_ok=True)

    #INIT LIMIT VD
    video_cpt = 0

    for video in channel.videos:
        if video_cpt >= videos_limit:
            print(f"Limite de {videos_limit} vidéos atteinte pour la chaîne {channel.channel_name}.")
            break

        try:
            clean_title = clean_file(video.title)
            print(f'Téléchargement de {clean_title}...')

            # INIT REPO
            video_directory = os.path.join(base_directory, f'Prod_{video_cpt + 1}')
            os.makedirs(video_directory, exist_ok=True)
            audio_directory = os.path.join(video_directory, 'audio')
            cover_directory = os.path.join(video_directory, 'cover')
            os.makedirs(audio_directory, exist_ok=True)
            os.makedirs(cover_directory, exist_ok=True)

            # DOWNLOAD VD
            video_download = video.streams.filter(progressive=True, file_extension='mp4').first()
            temp_video_path = video_download.download(output_path=os.path.join(video_directory, 'temp'))
            # EXTRACT MP3
            v_clip = VideoFileClip(temp_video_path)
            mp3_output = os.path.join(audio_directory, f'{clean_title}.mp3')
            v_clip.audio.write_audiofile(mp3_output)

            v_clip.close()
            os.remove(temp_video_path)
            try:
                if os.path.exists(temp_video_path):
                    shutil.rmtree(temp_video_path)
                    print(f"Le répertoire {temp_video_path} a été supprimé.")
            except Exception as e:
                print(f"Erreur lors de la suppression du répertoire {temp_video_path} : {str(e)}")

            #DOWNLOAD COVER
            cover_url = video.thumbnail_url
            response = requests.get(cover_url)
            cover_output_path = os.path.join(cover_directory, f'{clean_title}.jpg')
            with open(cover_output_path, 'wb') as file:
                file.write(response.content)
            # CALL PICTURE_RESIZE
            resize_image(cover_output_path, cover_output_path)

            # METADATA
            metadata_file = os.path.join(video_directory, 'metadata.txt')
            with open(metadata_file, 'w', encoding='utf-8') as file:
                file.write(f'Titre: {clean_title}\n')
                file.write(f'URL de la vidéo: {video.watch_url}\n')
                file.write(f'Description: {video.description}\n')
                file.write(f'Nom de la chaîne: {channel.channel_name}\n')
                file.write(f'URL de la chaîne: {channel_url}\n')
                file.write('-' * 50 + '\n')
            print(f"Le traitement est terminé pour {clean_title}")
            video_cpt += 1 
            print(f"Compteur de vidéos téléchargées: {video_cpt}")
        except Exception as e:
            print(f"Erreur lors du traitement de {video.title} : {str(e)}")
            continue
