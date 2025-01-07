from fastapi import FastAPI, HTTPException, status
from app.schemas import SimilarityRequest
from app.utils.similarity import Similarity

app = FastAPI()

#check server is running
@app.get("/health")
def health():
    return {"status": "ok"}

#get all similarity methods
@app.get("/similarity/all")
def get_similarity_methods():
    return Similarity.get_similarity_methods()

#calculate similarity between two strings
@app.post("/similarity")
def calculate_similarity(similarity_request: SimilarityRequest):

    #check if both strings are non-empty
    if not similarity_request.string1 or not similarity_request.string2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both string1 and string2 must be non-empty."
        )

    #check if at least one algorithm is provided
    if not similarity_request.algorithms or len(similarity_request.algorithms) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"You must provide at least one valid algorithm from the set: "
                f"{', '.join(Similarity.get_similarity_methods())}"
            )
        )
    
    #calculate similarity
    try:
        similarity = Similarity.calculate_similarity(
            similarity_request.algorithms,
            similarity_request.string1,
            similarity_request.string2
        )

    #catch invalid algorithms or other exceptions
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    return similarity

