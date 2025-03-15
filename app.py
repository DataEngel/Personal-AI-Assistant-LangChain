# Importación de librerías necesarias
from dotenv import load_dotenv  # Para cargar variables de entorno desde un archivo .env
import os  # Para interactuar con variables del sistema
from langchain_openai import ChatOpenAI  # Cliente de OpenAI para modelos de lenguaje
from langchain.memory import ConversationBufferMemory  # Memoria para mantener contexto en la conversación
from langchain_core.runnables.history import RunnableWithMessageHistory  # Para gestionar el historial de mensajes
from langchain.prompts import PromptTemplate  # Para definir plantillas de prompts (aunque no se usa en este código)
import pyttsx3  # Librería para convertir texto a voz

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Obtener la clave de API de OpenAI desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verificar si la clave de API fue cargada correctamente
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please check your .env file.")

# Inicializar el modelo de OpenAI GPT-4 Turbo con la clave de API
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4-turbo")

# Inicializar memoria para almacenar el historial de la conversación
memory = ConversationBufferMemory(return_messages=True)

# Función para recuperar el historial de una sesión específica
def get_session_history(session_id: str):
    return memory  # En este caso, siempre devuelve la misma memoria (sin segmentación por sesión)

# Envolver el modelo de lenguaje con historial de mensajes
conversation = RunnableWithMessageHistory(llm, get_session_history=get_session_history)

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
        # Enviar la entrada del usuario al modelo y obtener la respuesta
        response = conversation.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config={"configurable": {"session_id": "default"}}  # Usa un ID de sesión predeterminado
        )
        
        # Extraer la última respuesta del asistente de la conversación
        assistant_reply = response["messages"][-1]["content"]
        
        # Mostrar la respuesta en pantalla
        print(f"Assistant: {assistant_reply}")
        
        # Convertir la respuesta en voz y reproducirla
        speak(assistant_reply)
    
    except Exception as e:
        # Manejo de errores en caso de que falle la interacción con el modelo
        print(f"Error: {e}")
