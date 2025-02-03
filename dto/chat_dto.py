from pydantic import BaseModel

from typing import Literal
  
class ChatMessage(BaseModel):
  role: Literal['system', 'user']
  content: str

class RequestChatDto(BaseModel):
  messages: list[ChatMessage]