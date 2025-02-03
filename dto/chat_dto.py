from pydantic import BaseModel

from enum import Enum
 
class ChatUserType(Enum):
  role_user = 'user'
  role_system = 'system'
  
class ChatMessage(BaseModel):
  role: ChatUserType
  content: str

class RequestChatDto(BaseModel):
  messages: list[ChatMessage]