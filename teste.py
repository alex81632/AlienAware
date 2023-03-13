import pyttsx3

# Inicializa o motor de fala
engine = pyttsx3.init()

# Define a velocidade do motor de fala

engine.setProperty('rate', 150)

# Define o volume do motor de fala

engine.setProperty('volume', 1.0)

# Define o idioma do motor de fala

engine.setProperty('voice', 'brazil')

# Fala a frase

engine.say("Olá Mundo! Estou testando as funções do módulo pyttsx3.")

# Executa o motor de fala

engine.runAndWait()