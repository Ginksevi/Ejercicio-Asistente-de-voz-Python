import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
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

# funcion central del asistente
def pedido():

    # Activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el microfono y guardar el audio en un str
        solicitud = transformar_audio_a_texto().lower()

        if "abrir youtube" in solicitud:
            voz_asistente("Claro, ya estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abrir navegador" in solicitud:
            voz_asistente("Claro, estoy en eso")
            webbrowser.open("https://www.google.com/")
            continue
        elif "que día es hoy" in solicitud:
            pedir_dia()
            continue
        elif "que hora es" in solicitud:
            pedir_hora()
            continue
        elif "busca en wikipedia" in solicitud:
            voz_asistente("Buscandola informacion en wikipedia")
            solicitud = solicitud.replace("wikioedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(solicitud, sentences=1)
            voz_asistente("Wikipedia dice lo siguiente")
            voz_asistente(resultado)
            continue
        elif "busca en internet" in solicitud:
            voz_asistente("Ya mismo estoy en eso")
            solicitud = solicitud.replace("busca en internet", "")
            pywhatkit.search(solicitud)
            voz_asistente("Esto es lo que e encontrado")
            continue
        elif "reproducir" in solicitud:
            voz_asistente("Claro, empezare a reproducirlo")
            pywhatkit.search(solicitud)
        elif "chiste" in solicitud:
            voz_asistente(pyjokes.get_joke("es"))
            continue
        elif "precio" in solicitud:
            accion = solicitud.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                voz_asistente(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                voz_asistente("Discupe, no la e encontrado")
                continue
        elif "adiós" in solicitud:
            voz_asistente("Esta bien, que descanses, cualquier otra cosa que necesites hazmelo saber, estare atenta")
            break

