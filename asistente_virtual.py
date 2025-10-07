import pyttsx3
import speech_recognition as sr
import pywhatkit as pk
import yfinance as yf
import webbrowser
import datetime
import wikipedia

# escuchar microfono y devolver el audio como texto
def transformar_audio_a_texto():

    

    # almacenar reognizer
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:

        # tiempo de escucha
        r.pause_threshold = 0.8

        # comienzo de grabacion
        print("Te escucho")

        # guardar audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio)

            # prueba de escucha
            print(f"Dijiste: {pedido}")

            # devolver pedido
            return pedido
        
        # en caso de no comprender el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups... no entendi")

            # devolver error
            return "Sigo esperando"
        
        # en caso de no devolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups... no hay servicio")

            # devolver error
            return "Sigo esperando"
        
        # error inesperado
        except ImportError():

            # prueba de que no comprendio el audio
            print("ups... algo salio mal")

            # devolver error
            return "Sigo esperando"

# funcion para que el asistente pueda ser escuchado
def voz_asistente(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

voz_asistente("Hola mundo")