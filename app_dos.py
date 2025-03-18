# Import necessary libraries
from dotenv import load_dotenv  # To load environment variables from .env
import os  # To interact with system variables
from llama_index.llms.openai import OpenAI  # OpenAI client in LlamaIndex
from llama_index.memory import ChatMemoryBuffer  # Memory to maintain conversation history
import pyttsx3  # Library to convert text to speech

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key was loaded correctly
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Initialize the OpenAI GPT-4 Turbo model with the API key
llm = OpenAI(model="gpt-4-turbo", api_key=openai_api_key)

# Initialize memory to store conversation history
memory = ChatMemoryBuffer()

# Function to convert text to speech using pyttsx3
def speak(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(text)  # Add the text to the playback queue
    engine.runAndWait()  # Play the generated audio

# Main loop for interacting with the assistant
print("Welcome to your Personal AI Assistant. Type 'exit' to end the conversation.")

while True:
    # Prompt user for input
    user_input = input("You: ")
    
    # If the user types 'exit', terminate the program
    if user_input.lower() == "exit":
        print("Goodbye!")
        break  # Exit the while loop
    
    try:
        # Add user input to memory
        memory.put("user", user_input)

        # Generate a response using the model with the memory history
        response = llm.complete(memory.get_history())

        # Add the assistant's response to memory
        memory.put("assistant", response.text)

        # Display the response on the screen
        print(f"Assistant: {response.text}")

        # Convert the response to speech and play it
        speak(response.text)

    except Exception as e:
        # Handle errors in case the interaction with the model fails
        print(f"Error: {e}")
