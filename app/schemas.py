from pydantic import BaseModel

class SimilarityRequest(BaseModel):
    string1: str
    string2: str
    algorithms: list[str]