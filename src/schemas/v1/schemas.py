from pydantic import BaseModel

class Operation(BaseModel):
    a: float
    b: float
