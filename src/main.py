from fastapi import FastAPI
from anime_downloader import anime_router
from music_downloader import music_router

app = FastAPI()
app.include_router(anime_router)
app.include_router(music_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

