import sys
from anipy_api import provider, anime
from anipy_api.download import Downloader
from anipy_api.provider import LanguageTypeEnum
from pathlib import Path
from fastapi import APIRouter

anime_router = APIRouter(prefix="/anime", tags=["users"]) 

ANIME_MEDIA_DIR = "../../media/"
GLOBAL_PROVIDER = "allanime"


print("=== SCRIPT LoaderBoo para autodescargas ===")

# Link prueba: http://127.0.0.1:8000/anime/search_anime/Frieren
@anime_router.get("/search_anime/{anime_title}")
def search_anime(anime_title: str):
    """
    Function in charge of handling the search of anime episodes given its title
    'anime_title'. 
    The function shall return the list of animes in a format suitable for its 
    representation in the frontend. 
    """
    results = []

    # Initialize allanime provider
    anime_provider = provider.get_provider(GLOBAL_PROVIDER)

    # Search for the argument 'anime_title'
    search_results = anime_provider.get_search(anime_title)
    # provider.get_search() devuelve una lista de objetos de la clase 'ProviderSearchResult'
    # estos cuentan con identifier, name, languages (dub o sub)
    
    if len(search_results) == 0:
        print("[ANIME] Anime not found in your search")
        return -1
    
    for r in search_results:
        anime_res = anime.Anime(anime_provider, r.name, r.identifier, r.languages)
        info_results = anime_res.get_info()
        ep_info = anime_res.get_episodes(LanguageTypeEnum.SUB)
        res_elem = {}

        res_elem["identifier"] = r.identifier
        res_elem["name"] = r.name
        res_elem["year"] = info_results.release_year
        res_elem["status"] = info_results.status    # 1 -> Upcoming; 2 -> Ongoing; 3 -> Completed
        res_elem["image"] = info_results.image
        res_elem["episodes"] = len(ep_info)

        results.append(res_elem)
    
    # TODO: Preparar resultados para mostrarlos en el frontend

    return results

# Link prueba: http://127.0.0.1:8000/anime/get_anime_info/ReHMC7TQnch3C6z8j
@anime_router.get("/get_anime_info/{anime_id}")
def get_anime_info(anime_id: str):
    """
    Function that will get specific information from an anime
    by providing 'anime_id' parameter
    """
    anime_provider = provider.get_provider(GLOBAL_PROVIDER)
    anime_info = anime_provider.get_info(anime_id)
    anime_langs = {LanguageTypeEnum.SUB} # Not a problem as I always download SUB anime

    anime_obj = anime.Anime(anime_provider, anime_info.name,
                            anime_id, anime_langs)
    
    ep_info = anime_obj.get_episodes(LanguageTypeEnum.SUB) 

    api_response = {}

    api_response["name"] = anime_info.name
    api_response["year"] = anime_info.release_year
    api_response["status"] = anime_info.status    # 1 -> Upcoming; 2 -> Ongoing; 3 -> Completed
    api_response["image"] = anime_info.image
    api_response["episodes"] = len(ep_info)

    return api_response


def progress_callback(percentage: float): 
    """
    Function that will be called by the downloader to update 
    progress of the Download/type conversion tasks of the 
    downloader
    TODO: show interactive progress on the frontend from the given percentage 
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
@anime_router.post("/download_anime/{anime_name}/{anime_id}/{ep}")
def download_anime(anime_name: str, anime_id: str, ep: int):
    """
    TODO: Paralelizar downloaders ?¿ Ver si ocurre.
    Function in charge of handling the download of the anime 
    episode given its name, id, available languages (SUB/DUB) 
    and the episode number.
    """

    print(f"[INFO] STARTING ANIME DOWNLOAD {anime_name} Episode {ep}")

    anime_provider = provider.get_provider(GLOBAL_PROVIDER)

    anime_langs = {LanguageTypeEnum.SUB} # Not a problem as I always download SUB anime

    anime_season = anime.Anime(anime_provider, anime_name, anime_id, anime_langs)

    episode_stream = anime_season.get_video(
        episode=ep,
        lang=LanguageTypeEnum.SUB,
        preferred_quality="best"
    )
    downloader = Downloader(progress_callback, info_callback, error_callback)

    # TODO: Query a la base de datos para asegurar que no se está descargando previamente
    # TODO: Query al directorio media para asegurar que no se descarga varias veces el 
    # mismo archivo (opcional)
    download_path = downloader.download( 
        stream=episode_stream,
        download_path=Path(ANIME_MEDIA_DIR + anime_name + "/" + anime_name + " Episode " + str(ep) + ".mp4"),
        container=".mp4", 
        max_retry=3,
        ffmpeg=True,
        #post_dl_cb=save_anime_entry_to_history
    )

    return 0

