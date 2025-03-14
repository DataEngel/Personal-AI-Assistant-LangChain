# Personal AI Assistant with Text-to-Speech

This project creates a Personal AI Assistant using OpenAI's GPT-4 model integrated with LangChain, and converts the assistant's responses to speech using the `pyttsx3` library. The assistant maintains conversational context across multiple turns and provides both text-based and voice-based interactions.

## Features

- **Conversational AI**: Uses OpenAI's GPT-4 model for natural language understanding and generation.
- **Memory**: The assistant remembers the conversation history to provide contextual responses.
- **Text-to-Speech**: The assistant can read out loud its responses using `pyttsx3` for text-to-speech conversion.
- **Environment Variables**: The OpenAI API key is stored securely in a `.env` file.
- **Exit Command**: Type "exit" to terminate the conversation.

## Requirements

- Python 3.x
- Install required libraries using `pip`:

```bash
pip install python-dotenv openai langchain pyttsx3
