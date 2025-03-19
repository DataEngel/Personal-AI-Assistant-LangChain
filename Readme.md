# Personal AI Assistant with Text-to-Speech  

This project creates a **Personal AI Assistant** using OpenAI's **GPT-4 model**, integrated with **LangChain** and **Llama**, and converts the assistant's responses to speech using the `pyttsx3` library. The assistant maintains **conversational context across multiple turns** and provides both **text-based and voice-based interactions**.  

## Features  

- **Conversational AI**: Uses OpenAI's GPT-4 model for natural language understanding and generation.  
- **Memory**: The assistant remembers the conversation history to provide contextual responses.  
- **Text-to-Speech**: Converts the assistant's responses into speech using `pyttsx3`.  
- **Llama Integration**: Utilizes the Llama framework to optimize retrieval and indexing for enhanced knowledge management.  
- **LangChain Framework**: Ensures smooth integration and orchestration of multiple AI components.  
- **Environment Variables**: The OpenAI API key is securely stored in a `.env` file.  
- **Exit Command**: Type `"exit"` to terminate the conversation.  

## Requirements  

- **Python 3.x**  
- Install required dependencies:  

```bash
pip install python-dotenv openai langchain llama-index pyttsx3
