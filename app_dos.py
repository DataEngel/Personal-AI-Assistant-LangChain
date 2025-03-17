# Importación de librerías necesarias
from dotenv import load_dotenv  # Para cargar variables de entorno desde .env
import os  # Para interactuar con variables del sistema
from llama_index.llms.openai import OpenAI  # Cliente OpenAI en LlamaIndex
from llama_index.memory import ChatMemoryBuffer  # Memoria para mantener el historial de la conversación
import pyttsx3  # Librería para convertir texto a voz

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API de OpenAI desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verificar si la clave de API fue cargada correctamente
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Inicializar el modelo de OpenAI GPT-4 Turbo con la clave de API
llm = OpenAI(model="gpt-4-turbo", api_key=openai_api_key)

# Inicializar memoria para almacenar el historial de la conversación
memory = ChatMemoryBuffer()

# Función para convertir texto a voz usando pyttsx3
def speak(text):
    engine = pyttsx3.init()  # Inicializa el motor de texto a voz
    engine.say(text)  # Agrega el texto a la cola de reproducción
    engine.runAndWait()  # Reproduce el audio generado

# Bucle principal de interacción con el asistente
print("Welcome to your Personal AI Assistant. Type 'exit' to end the conversation.")

while True:
    # Solicitar entrada del usuario
    user_input = input("You: ")
    
    # Si el usuario escribe 'exit', se termina el programa
    if user_input.lower() == "exit":
        print("Goodbye!")
        break  # Sale del bucle while
    
    try:
        # Agregar entrada del usuario a la memoria
        memory.put("user", user_input)

        # Generar respuesta con el modelo usando el historial de memoria
        response = llm.complete(memory.get_history())

        # Agregar respuesta del asistente a la memoria
        memory.put("assistant", response.text)

        # Mostrar la respuesta en pantalla
        print(f"Assistant: {response.text}")

        # Convertir la respuesta en voz y reproducirla
        speak(response.text)

    except Exception as e:
        # Manejo de errores en caso de que falle la interacción con el modelo
        print(f"Error: {e}")
