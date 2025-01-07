# Similarity TEST

This project provides an API that computes the similarity between two strings using various algorithms (e.g., **cosine**, **levenshtein**, **jaccard**, etc.). It includes:

1. A **server** with FastAPI that exposes the API.
2. **Unit tests** for validating the similarity computation methods and error handling.

## Installation

- Using PIP :

```bash
pip install -r requirements.txt
```
 
## Running the Server

you can start the server with this command , it will open by default port 8000:
```bash
uvicorn --reload app.main:app
```


## Accessing the Documentation and test endpoints: 
Once the server is running, open your browser to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Using the API

### Example Request

- **Endpoint**: `POST /similarity`
- **Request Body** (in JSON):
  ```json
  {
    "string1": "cat",
    "string2": "bag",
    "algorithms": ["cosine", "levenshtein"]
  }
  ```
- **Sample Response** (in JSON):
  ```json
  {
    "cosine": 0.95,
    "levenshtein": 0.8
  }
  ```
  ---

- Endpoint: `GET similarity/list`

- **Sample Response** (in JSON):
  ```json
  [
  "cosine",
  "levenshtein",
  "jaccard",
  "damereau_levenshtein"
    ]
  ```

## Testing

1. **Unit tests** (via `unittest`):
   ```bash
   python -m unittest discover -s tests -v
   ```
