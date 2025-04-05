# Neuradeep

Neuradeep is a Telegram based chatbot designed to answer agriculture-related queries, along with general questions. 
It uses a custom dataset that I’ve prepared, containing accurate and up-to-date information specific to my region.

> Note: The dataset is currently very small, but I’m adding more data regularly to improve its accuracy and performance.


## Technologies Used

- **Python**
- **MiniLM** (from HuggingFace Transformers)
- **ChromaDB** (Vector Database)
- **Phi-2** (Small language model)
- **Telegram Bot API**



## How It Works

Neuradeep is built using a **Retrieval-Augmented Generation (RAG)** pipeline:

1. **Document Ingestion**  
   The documents are chunked and embedded using **MiniLM** (a small transformer-based model) and stored in **ChromaDB**.

2. **Querying**  
   When a user asks a question, it’s embedded and compared with existing chunks using ChromaDB to retrieve the most relevant context.

3. **Answer Generation**  
   The retrieved context and the user’s question are sent to **Phi-2**, a lightweight LLM, which then generates a relevant and context-aware response.

---

## Repository

https://github.com/qubitsculptor/Neuradeep

