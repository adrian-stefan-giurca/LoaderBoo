import subprocess
from shlex import quote
#from anipy_api import provider, anime

ANIME_MEDIA_DIR = "media"

print("=== SCRIPT LoaderBoo para autodescargas ===")

def anime_downloader(anime_title: str, eps: str):
    """
    Module in charge of handling the download of anime episodes given its title
    'anime_title' and number of episode 'ep' in its season
    """

    env_var=[]
    exec_args = ["ani-cli", "-q", "1080p", "-d" , "-e", eps, anime_title]

    print(exec_args[-1])

    try: 
        output = subprocess.run(exec_args, capture_output=True, check=True, env=env_var)
    except subprocess.CalledProcessError as error:
        # TODO: Enviar este mensaje o parecido al frontend
        print("[Error] Something failed while downloading anime: ", 
        error.stdout.decode('utf-8'), error.stderr.decode('utf-8'))

    # TODO: handling de errores típicos de ani-cli: 
    # - Episodio no encontrado
    # - Descarga incompleta
    
    print(output.stdout.decode('utf-8'))

    

def test_downloader(anime_title: str, eps: str):
    """
    Testing module for downloading anime.
    """

    exec_args = ["ani-cli", "-q", "1080p", "-d" , "-e", quote(str(eps)), quote(anime_title)]

    print(exec_args)


anime_downloader("Frieren Season 2", "1")