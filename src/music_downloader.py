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

class FakeLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def download_progress_hook(download_progress: dict):
    """
    Function in charge of notifying the progress of the download, it will be 
    called each time there is progress on the download task and its parameter
    'download_progress' is a dictionary with at least the following entries:
    * status: "downloading", "error", or "finished".
    * info_dict: The extracted info_dict

    If status is "downloading" or "finished" there will be also:
    * filename: The final filename (always present)
    * tmpfilename: The filename we're currently writing to
    * downloaded_bytes: Bytes on disk
    * total_bytes: Size of the whole file, None if unknown
    * total_bytes_estimate: Guess of the eventual file size, None if unavailable.
    * elapsed: The number of seconds since download started.
    * eta: The estimated time in seconds, None if unknown
    * speed: The download speed in bytes/second, None if unknown
    * fragment_index: The counter of the currently downloaded video fragment.
    * fragment_count: The number of fragments (= individual files that will be merged)

    This function is guaranteed to be called at least once with status on "finished"
    if the download is successfull.
    TODO: show interactive progress on the frontend from the given percentage 
    """

    if download_progress["status"] == "downloading":
        if download_progress["total_bytes"] is not None:
            progress_pct = download_progress["downloaded_bytes"] / download_progress["total_bytes"] * 100
            print(f"Downloading {download_progress["filename"]} | Progress: {progress_pct:.1f}%")
        else:
            print(f"Downloading {download_progress["filename"]}\nProgress: Unknown")
    elif download_progress["status"] == "finished":
        # Ejecutar save_music_entry_to_history()
        print(f"Finished downloading {download_progress["filename"]}")
    elif download_progress["status"] == "error":
        pass
    else:
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
        'progress_hooks': [download_progress_hook],
        'logger': FakeLogger(),
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    yt_downloader = YoutubeDL(ytd_options)

    # TODO: Query a la base de datos para asegurar que no se está descargando previamente
    # TODO: Query al directorio media para asegurar que no se descarga varias veces el 
    # mismo archivo (opcional)
    
    yt_downloader.download(video_url)

    return 0

#print(music_search("Frieren"))
#print(type(music_search("Frieren")))
music_downloader("QoGM9hCxr4k")
#help(yt_dlp.YoutubeDL)
"""
 |  paths:             Dictionary of output paths. The allowed keys are 'home'
 |                     'temp' and the keys of OUTTMPL_TYPES (in utils/_utils.py)
 |  outtmpl:           Dictionary of templates for output names. Allowed keys
 |                     are 'default' and the keys of OUTTMPL_TYPES (in utils/_utils.py).
 |                     For compatibility with youtube-dl, a single string can also be used
...
 |  progress_hooks:    A list of functions that get called on download
 |                     progress, with a dictionary with the entries
 |                     * status: One of "downloading", "error", or "finished".
 |                               Check this first and ignore unknown values.
 |                     * info_dict: The extracted info_dict
 |
 |                     If status is one of "downloading", or "finished", the
 |                     following properties may also be present:
 |                     * filename: The final filename (always present)
 |                     * tmpfilename: The filename we're currently writing to
 |                     * downloaded_bytes: Bytes on disk
 |                     * total_bytes: Size of the whole file, None if unknown
 |                     * total_bytes_estimate: Guess of the eventual file size,
 |                                             None if unavailable.
 |                     * elapsed: The number of seconds since download started.
 |                     * eta: The estimated time in seconds, None if unknown
 |                     * speed: The download speed in bytes/second, None if
 |                              unknown
 |                     * fragment_index: The counter of the currently
 |                                       downloaded video fragment.
 |                     * fragment_count: The number of fragments (= individual
 |                                       files that will be merged)
 |
 |                     Progress hooks are guaranteed to be called at least once
 |                     (with status "finished") if the download is successful.
"""