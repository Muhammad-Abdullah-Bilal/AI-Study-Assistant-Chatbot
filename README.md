# 🤖 AI Study Assistant Chatbot

An intelligent FastAPI-based chatbot designed to help students understand academic topics clearly and simply. This application uses advanced AI models through Groq and maintains conversation history using MongoDB for personalized learning experiences.

---

## ✨ Features

- **AI-Powered Responses** - Uses Groq's LLM for intelligent, educational explanations
- **Conversation History** - Stores chat history per user in MongoDB
- **Context-Aware** - Considers previous conversation context for better responses
- **Student-Friendly** - Explains concepts step-by-step with examples
- **RESTful API** - Easy-to-use FastAPI endpoints
- **CORS Enabled** - Supports cross-origin requests for web and mobile clients
- **Persistent Storage** - MongoDB integration for long-term conversation history

---

## 🛠️ Technology Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI/LLM**: [Groq](https://groq.com/) with [LangChain](https://langchain.com/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **Language**: Python 3.8+

---

## 📋 Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- A Groq API key (get it from [Groq Console](https://console.groq.com/))
- MongoDB Atlas account or local MongoDB instance

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muhammad-Abdullah-Bilal/AI-Study-Assistant-Chatbot.git
   cd AI-Study-Assistant-Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

Create a `.env` file in the project root directory with the following environment variables:

```env
GROQ_API_KEY=your_groq_api_key_here
MONGODB_URI=your_mongodb_connection_string_here
```

### Getting Your API Keys

- **Groq API Key**: Visit [Groq Console](https://console.groq.com/), sign up, and generate an API key
- **MongoDB URI**: 
  - For MongoDB Atlas: Create a cluster and get the connection string from the connect dialog
  - For local MongoDB: `mongodb://localhost:27017/chat`

---

## 🏃 Running the Application

Start the FastAPI server with:

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

---

## 📚 API Endpoints

### 1. Welcome Endpoint
**GET** `/`

Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the AI Study Assistant Chatbot API!"
}
```

### 2. Chat Endpoint
**POST** `/chat`

Send a question to the AI Study Assistant.

**Request Body:**
```json
{
  "user_id": "student_123",
  "question": "Explain photosynthesis"
}
```

**Response:**
```json
{
  "response": "Photosynthesis is the process by which plants convert light energy into chemical energy... [detailed explanation]"
}
```

---

## 💡 Usage Example

### Using Python (requests library)
```python
import requests

url = "http://localhost:8000/chat"
payload = {
    "user_id": "student_001",
    "question": "What is the water cycle?"
}

response = requests.post(url, json=payload)
print(response.json())
```

### Using cURL
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "student_001", "question": "Explain Newton'\''s laws of motion"}'
```

### Using FastAPI Docs
1. Open http://localhost:8000/docs
2. Click on the `/chat` endpoint
3. Click "Try it out"
4. Enter your `user_id` and `question`
5. Click "Execute"

---

## 📁 Project Structure

```
AI-Study-Assistant-Chatbot/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked in git)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## 🔧 Configuration Details

### LLM Model
The chatbot uses `openai/gpt-oss-20b` model via Groq. You can modify the model in `app.py`:

```python
llm = ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-20b")
```

### System Prompt
The AI's behavior is defined by the system prompt in the `prompt` variable. Customize it to change the assistant's personality and focus.

---


## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| fastapi | Web framework |
| uvicorn | ASGI server |
| langchain | LLM orchestration |
| langchain_groq | Groq integration |
| langchain_core | Core LLM functionality |
| langchain_community | Additional integrations |
| pymongo | MongoDB driver |
| python-dotenv | Environment variable management |
| python-multipart | Form data parsing |
| pydantic | Data validation |
| numpy | Numerical computing |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🚀 Future Enhancements

- [ ] Add user authentication
- [ ] Implement conversation rating system
- [ ] Add support for multiple languages
- [ ] Implement rate limiting
- [ ] Add conversation export feature
- [ ] Create web dashboard for analytics
- [ ] Add voice input/output capabilities

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://langchain.readthedocs.io/)
- [Groq API Documentation](https://groq.com/docs)
- [MongoDB Documentation](https://docs.mongodb.com/)

---

**Happy Learning! 📖✨**
