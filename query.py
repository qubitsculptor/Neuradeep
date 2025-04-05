import chromadb
from chromadb.config import Settings

# Initialize Chroma client (persistent mode)
client = chromadb.PersistentClient(path="db")  # replace with actual path
collection = client.get_collection(name="agri-qa")  # same name used in ingest.py

# Your query
query = "How do I treat chilli seeds before sowing?"

# Get results
results = collection.query(
    query_texts=[query],
    n_results=1
)

print("Q:", query)
print("A:", results["documents"][0][0])
