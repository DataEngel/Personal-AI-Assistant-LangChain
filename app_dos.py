import os
import pyttsx3
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.memory import ChatMemoryBuffer

# Cargar variables de entorno
load_dotenv()

# Obtener clave API
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("ERROR: OPENAI_API_KEY no encontrado en el archivo .env.")

# Inicializar el modelo GPT-4 Turbo
llm = OpenAI(model="gpt-4-turbo", api_key=openai_api_key)

# Inicializar memoria con un límite de mensajes almacenados
memory = ChatMemoryBuffer(token_limit=1000)  # Ajusta el límite según necesidades

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def speak(text):
    """Convierte texto en voz y lo reproduce."""
    engine.say(text)
    engine.runAndWait()

def get_response(user_input):
    """Genera una respuesta del asistente basada en la memoria de conversación."""
    try:
        memory.put("user", user_input)  # Almacenar entrada del usuario
        response = llm.complete(memory.get_history())  # Obtener respuesta del modelo
        memory.put("assistant", response.text)  # Almacenar respuesta
        return response.text
    except Exception as e:
        return f"Error en la respuesta del asistente: {e}"

# Bucle principal de interacción
print("\n👋 Bienvenido a tu Asistente AI. Escribe 'exit' para salir.\n")

while True:
    user_input = input("🟢 Tú: ")

    if user_input.strip().lower() == "exit":
        print("👋 ¡Hasta luego!")
        break

    response = get_response(user_input)

    print(f"🤖 Asistente: {response}\n")
    speak(response)  # Convertir la respuesta en voz
