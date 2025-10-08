import pyttsx3
import speech_recognition as sr
import pywhatkit as pk
import yfinance as yf
import webbrowser
import datetime
import wikipedia

# voz del asistente
id_sabina = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"

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
    engine.setProperty("voice", id_sabina)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar el dia de la semana
def pedir_dia():

    # variable con datos de hoy
    dia = datetime.datetime.today()

    # variable del dia de la semana
    dia_semana = dia.weekday()

    # diccionario de los dias
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sábado",
                  6:"Domingo"}
    
    # decir dia de la semana
    voz_asistente(f"Hoy es {calendario[dia_semana]}")

# informar la hora
def pedir_hora():
    
    #variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos"
    # decir la hora
    voz_asistente(hora)

# funcion saludo inicial
def saludo_inicial():

    # variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 18:
        momento = "Buenas noches"
    elif 6 <= hora.hour <13:
        momento = "Buenos dias"
    else:
        momento = "Buenas tardes"

    # decir saludo
    voz_asistente(f"{momento}, soy Sabrina tu asistente personal")

saludo_inicial()