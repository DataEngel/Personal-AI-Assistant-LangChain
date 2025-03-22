import os
import pyttsx3
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.memory import ChatMemoryBuffer


def load_api_key():
    """Loads the API key from the .env file."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("ERROR: OPENAI_API_KEY not found in the .env file.")
    return api_key


def initialize_llm(api_key: str):
    """Initializes the LLM model with the provided API key."""
    return OpenAI(model="gpt-4-turbo", api_key=api_key)


def initialize_tts_engine():
    """Initializes and configures the text-to-speech engine."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)   # Speaking speed
    engine.setProperty("volume", 1.0)  # Max volume
    return engine


def speak(text, engine):
    """Converts text to speech and plays it."""
    engine.say(text)
    engine.runAndWait()


def get_response(user_input, llm, memory):
    """Generates a response from the LLM based on the chat memory."""
    try:
        memory.put("user", user_input)
        response = llm.complete(memory.get_history())
        memory.put("assistant", response.text)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"


def main():
    print("\n👋 Welcome to your AI Assistant. Type 'exit' to quit.\n")

    api_key = load_api_key()
    llm = initialize_llm(api_key)
    memory = ChatMemoryBuffer(token_limit=1000)
    tts_engine = initialize_tts_engine()

    while True:
        try:
            user_input = input("🟢 You: ").strip()
            if user_input.lower() == "exit":
                print("👋 Goodbye!")
                break

            if not user_input:
                continue

            response = get_response(user_input, llm, memory)
            print(f"🤖 Assistant: {response}\n")
            speak(response, tts_engine)

        except KeyboardInterrupt:
            print("\n👋 Keyboard interruption detected. Closing assistant.")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
