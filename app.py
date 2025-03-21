import os
import pyttsx3
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Load environment variables
load_dotenv()

# Retrieve OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# Initialize OpenAI GPT-4 Turbo model
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4-turbo")

# Initialize conversation memory
memory = ConversationBufferMemory(return_messages=True)

# Function to manage session history
def get_session_history(session_id: str):
    return memory  # Currently, the same memory is used for all sessions

# Wrap the model with conversation history
conversation = RunnableWithMessageHistory(llm, get_session_history=get_session_history)

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main interaction loop
def chat_assistant():
    print("Welcome to your AI Assistant. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break  # Exit the loop

        try:
            # Send user input to the model and get a response
            response = conversation.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config={"configurable": {"session_id": "default"}},  # Default session ID
            )
            
            assistant_reply = response["messages"][-1]["content"]  # Get the last message from the assistant
            
            print(f"Assistant: {assistant_reply}")
            speak(assistant_reply)  # Convert response to speech
        
        except Exception as e:
            print(f"Error: {e}")

# Run the chatbot
if __name__ == "__main__":
    chat_assistant()
