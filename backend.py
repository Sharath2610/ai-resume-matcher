import chromadb
from embeddings import embed_text

client = chromadb.PersistentClient(path="./resume_db")

collection = client.get_or_create_collection(
    name="resumes",
    metadata={"hnsw:space": "cosine"}
)

def add_resume(text, resume_id):
    embedding = embed_text(text)
    collection.add(
        ids=[resume_id],
        documents=[text],
        embeddings=[embedding]
    )

def match_resumes(job_text, top_k=3):
    job_embedding = embed_text(job_text)
    results = collection.query(
        query_embeddings=[job_embedding],
        n_results=top_k
    )
    return results
