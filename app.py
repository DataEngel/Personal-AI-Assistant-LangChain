from dotenv import load_dotenv
import os
from langchain_openai import OpenAI  # Updated import

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Initialize the OpenAI model
llm = OpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

# Test the model
response = llm.invoke("Hello, how are you?")  # Use .invoke() instead of __call__
print(response)