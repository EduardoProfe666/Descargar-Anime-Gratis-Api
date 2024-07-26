from typing import Union, Optional, List

from pydantic import BaseModel


class DownloadLinkInfo(BaseModel):
    server: str
    url: str


class EpisodeInfoDownload(BaseModel):
    id: Union[str, int]
    anime: str
    image_preview: Optional[str] = None
    downloads: Optional[List[DownloadLinkInfo]] = None
