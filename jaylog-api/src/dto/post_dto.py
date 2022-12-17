from pydantic import BaseModel
from datetime import datetime
class ResMainPost(BaseModel):
    
    class _Writer(BaseModel):
        idx : int
        id : str
        profileImage : str
        
        class Config:
            orm_mode = True
            
        @staticmethod
        def toDto
        
    idx: int
    thumbnail: str | None
    title: str
    summary: str
    likeCount: int
    createDate: datetime
    writer: _Writer