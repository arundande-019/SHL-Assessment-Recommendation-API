# SHL Assessment Recommendation API

This project is a semantic recommendation system built to suggest relevant SHL assessments based on a user's query.

Instead of simple keyword matching, this system uses sentence embeddings to understand the meaning of the query and find the most relevant assessment URLs.

## How It Works

- The dataset contains different job-related queries and their corresponding SHL assessment links.
- Each query is converted into a vector embedding using the "all-MiniLM-L6-v2" model from Sentence Transformers.
- When a user sends a new query, it is also converted into an embedding.
- Cosine similarity is used to compare the user query with stored queries.
- The API returns the top 5 most relevant SHL assessment URLs.

## Technologies Used

- FastAPI (for building the API)
- Sentence Transformers (for semantic embeddings)
- Scikit-learn (for cosine similarity)
- Pandas & NumPy (for data handling)

## Project Files

- main.py – FastAPI application
- requirements.txt – Project dependencies
- Gen_AI Dataset.xlsx – Dataset used for recommendations

## How to Run the Project

1. Install dependencies:
   pip install -r requirements.txt

2. Run the API:
   uvicorn main:app --reload

3. Open this in your browser:
   http://127.0.0.1:8000/docs

## API Endpoint

POST /recommend

Example request:

{
  "query": "Python developer with machine learning skills"
}

The API responds with a list of recommended SHL assessment URLs.
