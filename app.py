from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.prompts import PromptTemplate
import pyttsx3

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Initialize the OpenAI model
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4-turbo")

# Add memory for contextual conversations
memory = ConversationBufferMemory(return_messages=True)

# Function to retrieve session history
def get_session_history(session_id: str):
    return memory

# Wrap LLM with message history
conversation = RunnableWithMessageHistory(llm, get_session_history=get_session_history)

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main conversation loop
print("Welcome to your Personal AI Assistant. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    try:
        response = conversation.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"configurable": {"session_id": "default"}}
        )
        assistant_reply = response["messages"][-1]["content"]
        print(f"Assistant: {assistant_reply}")
        speak(assistant_reply)
    except Exception as e:
        print(f"Error: {e}")
