from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

# Load dataset
df = pd.read_excel("Gen_AI Dataset.xlsx")
grouped_df = df.groupby("Query")["Assessment_url"].apply(list).reset_index()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
query_embeddings = model.encode(grouped_df["Query"].tolist())

class QueryInput(BaseModel):
    query: str

def recommend_assessments(user_query, top_k=3):
    user_embedding = model.encode([user_query])
    similarities = cosine_similarity(user_embedding, query_embeddings)
    top_indices = np.argsort(similarities[0])[-top_k:][::-1]

    recommended_urls = []
    for idx in top_indices:
        recommended_urls.extend(grouped_df.iloc[idx]["Assessment_url"])

    return list(set(recommended_urls))[:5]

@app.get("/")
def home():
    return {"message": "SHL Recommendation API Running"}

@app.post("/recommend")
def recommend(input: QueryInput):
    results = recommend_assessments(input.query)
    return {"recommended_assessments": results}
