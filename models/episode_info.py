from typing import Optional, Union

from pydantic import BaseModel


class EpisodeInfo(BaseModel):
    id: Union[str, int]
    anime: str
    image_preview: Optional[str] = None