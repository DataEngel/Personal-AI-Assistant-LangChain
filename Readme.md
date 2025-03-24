# Personal AI Assistant with Text-to-Speech

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project implements a **Personal Conversational AI Assistant** powered by **OpenAI's GPT-4**, with seamless integration of **LangChain** and **LlamaIndex** to support advanced context-aware interactions and retrieval-augmented generation. It features **bi-modal interaction**—both textual and vocal—leveraging the `pyttsx3` library for on-device speech synthesis.

---

## Architecture Overview

- **Language Model (LLM)**: Utilizes **GPT-4** via OpenAI's API for advanced natural language understanding and generation.
- **Memory & Context Handling**: Incorporates LangChain's **ConversationBufferMemory** to persist multi-turn dialog history for contextual coherence.
- **Retrieval-Augmented Generation (RAG)**: Integrates **LlamaIndex** for semantic search and knowledge base querying, enabling dynamic and informed responses.
- **Text-to-Speech (TTS)**: Employs `pyttsx3` for real-time, offline-capable voice synthesis of assistant responses.
- **Orchestration**: LangChain's agent framework coordinates interaction between the LLM, memory, and retriever components.
- **Environment Configuration**: Sensitive credentials (e.g., OpenAI API key) are externalized using a `.env` file, adhering to best practices for configuration management.
- **Graceful Exit**: The assistant session can be terminated cleanly using the `"exit"` keyword.

---

## Key Features

- **Context-Aware Conversation**: Retains dialogue history for coherent, ongoing interactions.
- **Voice Output**: Enhances accessibility through speech-based response delivery.
- **Knowledge Retrieval**: Leverages vector-based document indexing for enriched, fact-based assistance.
- **Modular Design**: Components are loosely coupled, allowing for easy replacement or extension (e.g., switching TTS engine or LLM provider).
- **Local Voice Rendering**: No cloud-based TTS services required, ensuring data privacy and low latency.

---

## Use Cases

- Personal productivity assistant
- Text summarization with voice feedback
- Educational tutor with spoken responses
- FAQ bot with contextual memory

---

## Installation

### Prerequisites

- **Python 3.8+**
- A valid **OpenAI API key**

### Install Dependencies

```bash
pip install python-dotenv openai langchain llama-index pyttsx3
