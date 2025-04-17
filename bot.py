import os
import telebot
import chromadb
from dotenv import load_dotenv
import requests

# Load .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found. Please check your .env file.")

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Chroma client and collection
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_collection(name="agri-qa")

# Greeting responses
greetings = ["hi", "hello", "hey", "yo", "sup", "wassup", "whatsup", 
             "namaste", "greetings", "ayo", "what's good", "howdy", "yo wassup", "wassup dawg"]

# Store user-specific message history
user_histories = {}

# Function to query Phi-2 via Ollama
def query_phi(prompt):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'phi',
                'prompt': prompt,
                'stream': False
            }
        )
        return response.json().get('response', 'Sorry, I couldn’t generate a response.')
    except Exception as e:
        return f"Error querying Phi model: {str(e)}"

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I’m Neuradeep 🌾 — your smart agri-assistant. Ask me anything about farming!")

# Message handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.strip().lower()
    user_id = message.from_user.id

    # Initialize history for the user if it's their first message
    if user_id not in user_histories:
        user_histories[user_id] = []

    if user_input in greetings:
        bot.reply_to(message, "Hey there! 🌱 I’m Neuradeep. Ask me anything about agriculture.")
        return

    # Step 1: Update user history and limit it to the last 6 messages
    user_histories[user_id].append(user_input)
    if len(user_histories[user_id]) > 6:
        user_histories[user_id].pop(0)  # Remove the oldest message if we exceed 6

    # Step 2: Fetch context from ChromaDB based on the user's input
    results = collection.query(query_texts=[user_input], n_results=1)

    if results and results['documents'] and results['documents'][0]:
        context = results['documents'][0][0]
        # Create prompt with the last 6 messages and the relevant context
        context_window = "\n".join(user_histories[user_id])  # Combine all recent messages
        prompt = f"""You are an expert agriculture assistant called Neuradeep.
Use the following context to answer the user's question naturally.

Context:
{context_window}

Context from ChromaDB:
{context}

Question: {user_input}
Answer:"""
        answer = query_phi(prompt)
    else:
        # Fallback: Ask Phi directly if no relevant doc
        context_window = "\n".join(user_histories[user_id])  # Use only the recent messages as context
        prompt = f"""You are an expert agriculture assistant called Neuradeep.
Answer this question to the best of your knowledge:

Context:
{context_window}

Question: {user_input}
Answer:"""
        answer = query_phi(prompt)

    bot.reply_to(message, answer)

# Start bot
print("🤖 Neuradeep is running on Telegram...")
bot.infinity_polling()






