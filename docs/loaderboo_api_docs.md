
# LoaderBoo API description

The API has been developed in [FastAPI](https://fastapi.tiangolo.com/), which is a framework based in Python.

The API is conformed of 3 files at this moment 
1. **main.py**: This is the main file in which the API is initialized.
2. **anime_downloader.py**: Module in charge of exposing two important functions related to the search and download of anime episodes through anipy_api which at the moment uses allanime as a provider.
3. **music_downloader.py**: Module in charge of exposing two important functions related to the search and download of music through YouTube, the search function is based on [youtube_search](https://github.com/joetats/youtube_search) python library and the download function is based on [yt-dlp](https://github.com/yt-dlp/yt-dlp)
