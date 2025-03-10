from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import pyttsx3

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Initialize the OpenAI model
llm = OpenAI(api_key=openai_api_key, model="gpt-4")

# Add memory for contextual conversations
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Add a custom prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful AI assistant. Answer the following question: {question}"
)

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
        # Use the custom prompt template
        formatted_input = prompt.format(question=user_input)
        response = conversation.predict(input=formatted_input)
        print(f"Assistant: {response}")
        speak(response)  # Convert the response to speech
    except Exception as e:
        print(f"Error: {e}")