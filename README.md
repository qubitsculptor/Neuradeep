# Neuradeep 🌾 - Smart Agriculture Assistant Bot

Neuradeep is a Telegram-based chatbot designed to answer agriculture-related queries, along with general questions. It uses a custom dataset that I’ve prepared, containing accurate and up-to-date information specific to my region.

Note: The dataset is currently very small, but I’m adding more data regularly to improve its accuracy and performance.

## New Feature: Context-Aware Conversations

### What's New?
We’ve recently added a **context awareness** feature to Neuradeep! Now, the bot can remember up to the last **6 user messages** during a conversation. This helps the bot understand the conversation flow better and respond in a more natural and relevant way.

### How it works:
- **Message History**: The bot stores the last 6 messages from each user.
- **Contextual Responses**: The bot uses this stored context along with its database to generate more accurate, context-aware responses.

Previously, Neuradeep would only use the current user query and database context for answering questions. Now, with context-awareness, the bot can take into account previous user inputs to keep the conversation smooth and coherent.

---

## Technologies Used

- Python
- MiniLM (from HuggingFace Transformers)
- ChromaDB (Vector Database)
- Phi-2 (Small language model)
- Telegram Bot API

---

## How It Works

Neuradeep is built using a Retrieval-Augmented Generation (RAG) pipeline:

1. **Document Ingestion**  
   The documents are chunked and embedded using MiniLM (a small transformer-based model) and stored in ChromaDB.

2. **Querying**  
   When a user asks a question, it’s embedded and compared with existing chunks using ChromaDB to retrieve the most relevant context.

3. **Answer Generation**  
   The retrieved context and the user’s question are sent to Phi-2, a lightweight LLM, which then generates a relevant and context-aware response.

4. **Context Awareness**  
   The bot now tracks the last 6 user messages, enabling it to provide more personalized and fluid conversations based on previous exchanges.

---

## NOTE:
This bot is not hosted publicly 24/7. If you try interacting with it on Telegram and it doesn’t respond, it's likely because the server is not currently running. To use the bot yourself, you’ll need to clone this repo and run it locally or deploy it to a hosting platform.

---

## Run the bot:

1.**Clone the repo:**
  [Neuradeep GitHub Repo](https://github.com/qubitsculptor/Neuradeep)

2.**Install dependencies:**
  pip install -r requirements.txt

3.**Set up the .env file with your BOT_TOKEN from @BotFather on Telegram.**

4.**Run the bot:**
  python bot.py




