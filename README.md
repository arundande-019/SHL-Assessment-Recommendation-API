# SHL Assessment Recommendation API

This project is a semantic recommendation system that suggests relevant SHL assessments based on a user’s query.

Instead of simple keyword matching, this system uses sentence embeddings to understand the meaning of the input query and return the most relevant assessment URLs.

---

## How It Works

- The dataset contains job-related queries and their corresponding SHL assessment links.
- Each query in the dataset is converted into a vector embedding using the "all-MiniLM-L6-v2" model from Sentence Transformers.
- When a user submits a new query, it is also converted into an embedding.
- Cosine similarity is calculated between the user query embedding and stored query embeddings.
- The system returns the top 5 most relevant SHL assessments.

This approach enables semantic search rather than exact keyword matching.

---

## Technologies Used

- FastAPI – API development
- Sentence Transformers – Semantic embeddings
- Scikit-learn – Cosine similarity
- Pandas & NumPy – Data processing
- Docker – Containerization
- Hugging Face Spaces – Deployment

---

## Project Structure

- app.py – FastAPI application
- requirements.txt – Project dependencies
- Gen_AI Dataset.xlsx – Dataset used for recommendations
- Dockerfile – Container configuration

---

## How to Run Locally

1. Install dependencies:

pip install -r requirements.txt

2. Run the API:

uvicorn app:app --reload

3. Open in your browser:

http://127.0.0.1:8000/docs

---

## Live Deployment

The API is deployed on Hugging Face Spaces:

https://arundande-shl-assessment-api.hf.space/

---

## API Endpoint

POST /recommend

Example request:

{
  "query": "Python developer with machine learning skills"
}

The API responds with the top 5 recommended SHL assessment URLs in structured JSON format.

---

## Key Highlights

- Semantic search using embeddings
- Cosine similarity ranking
- REST API using FastAPI
- Dockerized application
- Public cloud deployment
