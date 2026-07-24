choose best embedding->https://huggingface.co/spaces/mteb/leaderboard


choose best vector->https://superlinked.com/vector-db-comparison
we are using Qdrant for vector db


ui:
streamlit run .\ui\app.py

backend
uvicorn app.main:app --reload --port 8000