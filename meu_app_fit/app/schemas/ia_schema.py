

from pydantic import BaseModel


class CoachRequest(BaseModel):
    mensagem: str | None= ""
    
    
class PlanoRequest(BaseModel):
    mensagem: str | None = ""