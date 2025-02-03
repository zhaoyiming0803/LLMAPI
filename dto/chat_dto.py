from pydantic import BaseModel

from enum import Enum
 
class ChatUserType(Enum):
  role_user = 'user'
  role_system = 'system'

class RequestChatDto(BaseModel):
  role: ChatUserType
  content: str