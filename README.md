# Agentic Healthcare Assistant for Medical Task Automation

An AI-powered virtual medical assistant built using LangChain, LangGraph, Groq LLM, FAISS, and Streamlit.

## Features
- **Chat Assistant** - Conversational AI for healthcare queries
- **Patient Records** - View and update patient medical histories
- **Book Appointment** - Schedule appointments with specialists
- **Medical Search** - RAG-powered search over medical documents

## Tech Stack
- LangChain / LangGraph - Agent framework
- Groq (llama3) - LLM
- FAISS - Vector database for RAG
- HuggingFace Embeddings - Text embeddings
- Streamlit - Web UI
- OpenPyXL - Patient records management

## Setup Instructions
1. Clone the repository
2. Create a virtual environment and install dependencies:

pip install -r requirements.txt
pip install streamlit langchain langchain-text-splitters python-dotenv

3. Create a `.env` file with your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

4. Run the app:
streamlit run app.py