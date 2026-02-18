import sys
from anipy_api import provider, anime
from anipy_api.download import Downloader
from anipy_api.provider import LanguageTypeEnum
from pathlib import Path
from fastapi import APIRouter

anime_router = APIRouter(prefix="/anime", tags=["users"]) 

ANIME_MEDIA_DIR = "media/"

print("=== SCRIPT LoaderBoo para autodescargas ===")

# Link prueba: http://127.0.0.1:8000/anime/search_anime/Frieren
@anime_router.get("/search_anime/{anime_title}")
def anime_search(anime_title: str):
    """
    Function in charge of handling the search of anime episodes given its title
    'anime_title'. 
    The function shall return the list of animes in a format suitable for its 
    representation in the frontend. 
    """

    # Initialize allanime provider
    anime_provider = provider.get_provider("allanime")

    # Search for the argument 'anime_title'
    results = anime_provider.get_search(anime_title)
    # provider.get_search() devuelve una lista de objetos de la clase 'ProviderSearchResult'
    # estos cuentan con identifier, name, languages (dub o sub)
    
    if len(results) == 0:
        print("[ANIME] Anime not found in your search")
        return -1
    
    # TODO: Preparar resultados para mostrarlos en el frontend

    #for res in results:
    return results

def progress_callback(percentage: float): 
    """
    Function that will be called by the downloader to update 
    progress of the Download/type conversion tasks of the 
    downloader
    # TODO: show interactive progress on the frontend from the given percentage 
    """
    print(f"Progress: {percentage:.1f}%", end="\r")

def info_callback(message: str): 
    print(f"Message from the downloader: {message}")

def error_callback(message: str): 
    print(f"Soft error from the downloader: {message}", file=sys.stderr)

def save_anime_entry_to_history():
    """
    TODO
    Callback that will be called by the Downloader at the time of
    finishing a download to store an anime entry into the history 
    table of the DB
    """
    pass

# Link prueba: http://127.0.0.1:8000/anime/download_anime/Sousou no Frieren/ReHMC7TQnch3C6z8j/1
@anime_router.get("/download_anime/{anime_name}/{anime_id}/{ep}")
def anime_downloader(anime_name: str, anime_id: str, ep: int):
    """
    TODO: Paralelizar downloaders ?¿ Ver si ocurre.
    Function in charge of handling the download of the anime 
    episode given its name, id, available languages (SUB/DUB) 
    and the episode number.
    """
    anime_provider = provider.get_provider("allanime")

    anime_langs = {LanguageTypeEnum.SUB} # Not a problem as I always download SUB anime

    anime_season = anime.Anime(anime_provider, anime_name, anime_id, anime_langs)

    episode_stream = anime_season.get_video(
        episode=ep,
        lang=LanguageTypeEnum.SUB,
        preferred_quality="worst"
    )

    downloader = Downloader(progress_callback, info_callback, error_callback)

    # TODO: Query a la base de datos para asegurar que no se está descargando previamente
    # TODO: Query al directorio media para asegurar que no se descarga varias veces el 
    # mismo archivo
    download_path = downloader.download( 
        stream=episode_stream,
        download_path=Path(ANIME_MEDIA_DIR + anime_name + " Episode " + str(ep) + ".mp4"),
        container=".mp4", 
        max_retry=3,
        ffmpeg=False,
        #post_dl_cb=save_anime_entry_to_history
    )

    return 0

