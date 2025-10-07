import pyttsx3 as psx
import speech_recognition as sr
import pywhatkit as pk
import yfinance as yf
import pyjokes as pj
import webbrowser as wb
import datetime
import wikipedia

# escuchar microfono y devolver el audio en texto

def transformar_audio_a_texto():

    # almacenar recognizer
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:
        # tiempo de escucha
        r.pause_threshold = 0.8

        # informar comienzo de grabación
        print("Ya puedes hablar")

        # guardar audio
        audio = r.listen(origen)
        
        try:
            # buscar en google
            pedido = r.recognize_google(audio, languaje = "es-co")

            # prueba de ingreso de audio a texto
            print(f"Dijiste: {pedido}")

            # devolver pedido
            return pedido
        
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups... no entendi")

            # devolver error
            return "Sigo esperando"
        
        # en  caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups... no hay servicio")

            # devolver error
            return "Sigo esperando"
        
        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups... algo a salido mal")

            # devolver error
            return "Sigo esperando"

transformar_audio_a_texto()