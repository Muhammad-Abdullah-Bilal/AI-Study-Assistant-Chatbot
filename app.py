import datetime
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)
db = client["chat"]
collection = db["users"]

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Study Assistant.

Your role:
- Help students understand study-related topics clearly and simply.
- Explain concepts step-by-step with examples when needed.
- Answer based on previous conversation context if available.
- Be concise, accurate, and student-friendly.
- If a question is unclear, ask for clarification.
- If the user asks something outside academics, politely guide them back to study topics.

Rules:
- Give a clear, concise answer first (5–8 lines).
- Use bullet points when possible.
- If the user wants more detail, expand step-by-step.
- Maintain academic relevance.
- Be friendly and student-focused.

Tone:
- Friendly
- Supportive
- Clear and educational
"""
        ),
        ("placeholder", "{history}"),
        ("user", "{question}")
    ]
)

llm = ChatGroq(api_key = groq_api_key, model="openai/gpt-oss-20b")
chain = prompt | llm


from langchain_core.messages import HumanMessage, AIMessage

def get_history(user_id):
    chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []

    for chat in chats:
        if chat["role"] == "user":
            history.append(HumanMessage(content=chat["message"]))
        else:
            history.append(AIMessage(content=chat["message"]))

    return history


# def get_history(user_id):
#     chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
#     history = []

#     for chat in chats:
#         history.append((chat["role"], chat["message"]))
#     return history

@app.get("/") 
def home():
    return {"message": "Welcome to the AI Study Assistant Chatbot API!"}

@app.post("/chat")
def chat(request: ChatRequest):
    history = get_history(request.user_id)
    response = chain.invoke({"history": history, "question": request.question})

    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.utcnow()
    })

    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.utcnow()
    })

    return {"response" : response.content}