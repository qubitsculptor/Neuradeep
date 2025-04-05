import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

# Load your dataset
df = pd.read_csv("chatbot_agri.csv", encoding='latin1')

chroma_client = chromadb.PersistentClient(path="db")

collection = chroma_client.get_or_create_collection(name="agri-qa")

# Load model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings and store in ChromaDB
for i, row in df.iterrows():
    embedding = model.encode(row["Question"]).tolist()
    collection.add(
        documents=[row["Answer"]],
        metadatas=[{"source": "chatbot_agri.csv"}],
        ids=[str(i)],
        embeddings=[embedding]
    )

# Persist DB to disk
print("Data has been ingested into ChromaDB.")


# Show first few rows
print(df.head())

