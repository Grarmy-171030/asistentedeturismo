#Creador CoolfaceJerkCity
from pywhatkit.main import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import pyjokes
import os
import wikipedia
from tkinter import*
from PIL import Image,ImageTk
horas_invertidas = 20;
main_window=Tk()
main_window.title("Sandra VA")
main_window.geometry("800x450")
main_window.resizable(0,0) 
main_window.configure(bg='#BB377D')

comandos= """
    Comandos que puedes usar:
    -Reproduce...(algo)
    -Busca...(algo)
    -Chiste...(es)
    -fecha(hoy es)
    -hora(son las)

"""

label_title=Label(main_window, text= "Sandra VA" , bg="#FBD3E9",fg="#000000", 
                      font=('Apple Garamond',30,'bold'))
label_title.pack(pady=10)
Canvas_comandos=Canvas(bg="#BB377D",height=200,width=195)
Canvas_comandos.place(x=0 , y=0)
Canvas_comandos.create_text(90,80,text=comandos,fill="#000000", font=' Garamond 10')

text_info=Text(main_window,bg="#BB377D",fg="#000000")
text_info.place(x=0,y=170,height=280,width=198)
Sandra_photo=ImageTk.PhotoImage(Image.open("Sandra_photo.png"))
window_photo=Label(main_window,image=Sandra_photo)
window_photo.pack(pady=5)
def mexican_voice():
    change_voice(0)
def spanish_voice():
    change_voice(1)
def english_voice():
   change_voice(2)
def change_voice(id):
    engine.setProperty('voice',voices [id].id)
    engine.setProperty('rate',145)
    talk("Hola soy Sandra!")
name = 'Sandra'

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def red_and_talk():
    text=text_info.get("1.0", "end")
    talk(text)
def write_text(text_wiki):
    text_info.insert(INSERT,text_wiki)
def listen(texto):
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                print("Usted dijo: " + rec)                                                
    except:
        pass

    return rec

    

#def basic_functions():
 #   rec = listen('Funciones básicas...')
def run_Sandra():
    #Música y Videos en YT
    rec = listen('Escuchando...')
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)  
    #Hora
    elif 'dime la hora actual' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
                    
    #Fecha
    elif 'dime la fecha actual' in rec:
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Hoy es " + fecha) 

    #Buscador 
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        talk('Buscando '+ order)
        pywhatkit.search(order)
    #Chistes
    elif 'dime un chiste' in rec:
        talk(pyjokes.get_joke('es'))
    
    elif 'créditos' in rec:
        webbrowser.open('https://www.youtube.com/watch?v=_KprFCkj2SU')

#def advanced_functions():
    #rec = listen('Funciones avanzadas...')

    #Ejecución de aplicaciones.exe
    elif 'ejecuta' in rec:
        order = rec.replace('ejecuta','')
        talk('Abriendo '+ order)
        app = order+'.exe'
        os.system(app)

    #Creación de directorios
    elif 'crea el directorio' in rec:
        home = "C:\\Users\\INTEL\\Desktop\\Tareas\\3er SEMESTRE\\Lenguaje de Programacion II\\#Miscelaneos\\"            
        order = rec.replace('crea el directorio','')

        if os.path.exists(order):
            talk("El directorio ya existe")

        else:
            mrk = os.mkdir(home+order)
            talk("Se creo el directorio correctamente")

    #Eliminación de directorios
    elif 'borra el directorio' in rec:
        order = rec.replace('borra el directorio','')
        if os.path.exists(order):
            rd = os.rmdir(order)
            talk("Se elimino el directorio correctamente")
        else:
            talk("El directorio no existe")

    #Creación de archivos de texto
    elif 'crea el archivo' in rec:
        order = rec.replace('crea el archivo','')
        order = order+'.txt'
        if os.path.exists(order):
            talk("El archivo ya existe")

        else:    
            archivo = open(order,"w")
            archivo.close()
            talk("Se creo el archivo correctamente")
                    
    #Eliminación de archivos de texto
    elif 'borra el archivo' in rec:
        order = rec.replace('borra el archivo','')
        order = order+'.txt'
        if os.path.exists(order):
            os.remove(order)
            talk("Se elimino el archivo correctamente")
        else:
            talk("El archivo no existe")

    #Redireccionamiento de sitios web
    #elif 'entra a interbank' in rec:
        #case = rec.replace('entra a', '')
        #talk("Entrando " + case)
        #webbrowser.open('https://bancaporinternet.interbank.pe/login')

    #Sin programar
    else:
        talk("No te entendi muy bien, vuelve a intentarlo")
button_voice_mx=Button(main_window, text="Voz Mex", fg="white",bg="#00bf8f",
                      font=('Apple Garamond',10,"bold"), command=mexican_voice)
button_voice_mx.place(x=625, y =80, width=100,height=30)
button_voice_es=Button(main_window, text="Voz Esp", fg="white",bg="#FBD786",
                      font=('Apple Garamond',10,"bold"), command=spanish_voice)
button_voice_es.place(x=625, y =115, width=100,height=30)
button_voice_us=Button(main_window, text="Voz USA", fg="white",bg="#f12711",
                      font=('Apple Garamond',10,"bold"), command=english_voice)
button_voice_us.place(x=625, y =150, width=100,height=30)
button_listen=Button(main_window, text="Escuchar", fg="white",bg="#E94057",
                      font=('Apple Garamond',15,"bold"),width=20,height=3,command=run_Sandra)
button_listen.pack(pady=10)
button_speak=Button(main_window, text="Hablar", fg="white",bg="#BB377D",
                      font=('Apple Garamond',10,"bold"),command= red_and_talk)
button_speak.place(x=625, y =190, width=100,height=30)
main_window.mainloop()
 
