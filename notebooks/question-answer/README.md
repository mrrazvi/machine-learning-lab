# Question Answering System

## System Architecture (RAG Based QA)

User Question
    ↓
Embedding Model (Query -> Vector) (Qwen 3)
    ↓
Vector Database (Semantic Retrieval)
    ↓
Top-K Relveant Passages
    ↓
LLM (Answer Constrained to Retrieved Context)
    ↓
Answer + Source Refference
