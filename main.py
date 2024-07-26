from typing import List

from fastapi import FastAPI

from api.animeflv import AnimeFLV, wrap_request
from models.anime_info import AnimeInfo
from models.download_info import EpisodeInfoDownload, DownloadLinkInfo
from models.episode_info import EpisodeInfo

app = FastAPI()


@app.get("/search_anime/{name}", summary="Permite buscar animes", response_model=List[AnimeInfo])
async def root(name: str):
    with AnimeFLV() as api:
        data = wrap_request(api.search, name, expected=[])
    return data


@app.get("/episode_info_download/{name}", summary="Permite buscar los episodios con sus descargas de un anime", response_model=List[EpisodeInfoDownload])
async def say_hello(name: str):
    with AnimeFLV() as api:
        data: List[EpisodeInfo] = wrap_request(api.get_anime_info, name, expected=[]).episodes

        r: List[EpisodeInfoDownload] = []

        for e in data:
            download = wrap_request(api.get_links, f'{e.anime}-{e.id}', expected=[])
            r.append(EpisodeInfoDownload(id=e.id, anime=e.anime, image_preview=e.image_preview, downloads=download))
    return r
