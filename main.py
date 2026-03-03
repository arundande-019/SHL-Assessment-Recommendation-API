from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load dataset
file_path = "Gen_AI Dataset.xlsx"
train_df = pd.read_excel(file_path, sheet_name="Train-Set")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
train_queries = train_df["Query"].tolist()
train_embeddings = model.encode(train_queries)

class QueryInput(BaseModel):
    query: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend_assessments(input: QueryInput):
    query_embedding = model.encode([input.query])
    similarities = cosine_similarity(query_embedding, train_embeddings)
    top_indices = np.argsort(similarities[0])[-5:][::-1]

    results = []

    for idx in top_indices:
        results.append({
            "url": train_df.iloc[idx]["Assessment_url"],
            "name": "Assessment",
            "adaptive_support": "No",
            "description": "Recommended assessment",
            "duration": 0,
            "remote_support": "Yes",
            "test_type": ["General"]
        })

    return {"recommended_assessments": results}
