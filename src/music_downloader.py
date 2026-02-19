from youtube_search import YoutubeSearch
from fastapi import APIRouter
from yt_dlp import YoutubeDL
import yt_dlp

music_router = APIRouter(prefix="/music", tags=["users"]) 

ANIME_MUSIC_MEDIA_DIR = "music/"

print("=== SCRIPT LoaderBoo para autodescargas ===")

# Link prueba: http://127.0.0.1:8000/music/search_music/Frieren Opening 1
@music_router.get("/search_music/{video_title}")
def music_search(video_title: str):
    """
    Function in charge of handling the search of music in youtube given its title
    'video_title'. 
    The function shall return the list of music results in a format suitable for its 
    representation in the frontend. 
    """
    results = YoutubeSearch(video_title, max_results=10).to_dict()

    return results


def save_music_entry_to_history():
    """
    TODO
    Callback that will be called by the Downloader at the time of
    finishing a download to store an anime entry into the history 
    table of the DB
    """
    pass

# Link prueba: http://127.0.0.1:8000/music/download_music/QoGM9hCxr4k
@music_router.get("/download_music/{video_url_suffix}")
def music_downloader(video_url_suffix: str):
    """
    TODO: add progress hooks: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#adding-logger-and-progress-hook
    Function in charge of handling the download of the anime 
    episode given its name, id, available languages (SUB/DUB) 
    and the episode number.
    """
    print(f"url_suffix: {video_url_suffix}")
    video_url = "https://www.youtube.com/watch?v=" + video_url_suffix

    yt_dlp.postprocessor

    ytd_options = {
        'paths' : {"home" : ANIME_MUSIC_MEDIA_DIR},
        'outtmpl' : '%(title)s.%(ext)s',
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    yt_downloader = YoutubeDL(ytd_options)
    yt_downloader.download(video_url)

    return 0

#print(music_search("Frieren"))
#print(type(music_search("Frieren")))
#music_downloader("/watch?v=QoGM9hCxr4k")
#help(yt_dlp.YoutubeDL)
"""
 |  paths:             Dictionary of output paths. The allowed keys are 'home'
 |                     'temp' and the keys of OUTTMPL_TYPES (in utils/_utils.py)
 |  outtmpl:           Dictionary of templates for output names. Allowed keys
 |                     are 'default' and the keys of OUTTMPL_TYPES (in utils/_utils.py).
 |                     For compatibility with youtube-dl, a single string can also be used
"""