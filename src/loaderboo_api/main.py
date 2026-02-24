from fastapi import FastAPI
from anime_downloader import anime_router
from music_downloader import music_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(anime_router)
app.include_router(music_router)

origins = [
    "http://localhost:5173",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

