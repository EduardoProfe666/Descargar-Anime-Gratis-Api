from typing import Union, Optional, List

from pydantic import BaseModel

from models.episode_info import EpisodeInfo


class AnimeInfo(BaseModel):
    id: Union[str, int]
    title: str
    poster: Optional[str] = None
    banner: Optional[str] = None
    synopsis: Optional[str] = None
    rating: Optional[str] = None
    genres: Optional[List[str]] = None
    debut: Optional[str] = None
    type: Optional[str] = None
    episodes: Optional[List[EpisodeInfo]] = None