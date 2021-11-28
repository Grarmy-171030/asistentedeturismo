## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Grarmy-171030/asistentedeturismo/edit/Grarmy-171030-patch-1/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.
#Creador CoolfaceJerkCity
de  pywhatkit . búsqueda de importación principal  
importar  speech_recognition  como  sr
importar  pyttsx3
importar  pywhatkit
importar  fecha y hora
importar  navegador web
importar  pyjokes
importar sistema  operativo
importar  wikipedia
desde  tkinter  import *
de la  imagen de importación PIL  , ImageTk 
horas_invertidas  =  20 ;
ventana_principal = Tk ()
ventana_principal . título ( "Sandra VA" )
ventana_principal . geometría ( "800x450" )
ventana_principal . redimensionable ( 0 , 0 )
ventana_principal . configurar ( bg = '# BB377D' )

comandos =  "" "
    Comandos que puedes usar:
    -Reproducir ... (algo)
    -Busca ... (algo)
    -Chiste ... (s)
    -fecha (hoy es)
    -hora (hijo las)
"" "

label_title = Etiqueta ( ventana_principal , texto =  "Sandra VA" , bg = "# FBD3E9" , fg = "# 000000" ,
                      font = ( 'Apple Garamond' , 30 , 'negrita' ))
label_title . paquete ( pady = 10 )
Canvas_comandos = Canvas ( bg = "# BB377D" , alto = 200 , ancho = 195 )
Canvas_comandos . lugar ( x = 0 , y = 0 )
Canvas_comandos . create_text ( 90 , 80 , text = comandos , fill = "# 000000" , font = 'Garamond 10' )

text_info = Texto ( ventana_principal , bg = "# BB377D" , fg = "# 000000" )
text_info . lugar ( x = 0 , y = 170 , alto = 280 , ancho = 198 )
Sandra_photo = ImageTk . PhotoImage ( Imagen . Abierta ( "Sandra_photo.png" ))
window_photo = Etiqueta ( ventana_principal , imagen = Sandra_photo )
ventana_foto . paquete ( pady = 5 )
def  voz_mexicana ():
    change_voice ( 0 )
def  spanish_voice ():
    change_voice ( 1 )
def  english_voice ():
   change_voice ( 2 )
def  change_voice ( id ):
    motor . setProperty ( 'voz' , voces [ id ]. id )
    motor . setProperty ( 'tasa' , 145 )
    hablar ( "Hola soy Sandra!" )
nombre  =  'Sandra'

oyente  =  sr . Reconocedor ()
motor  =  pyttsx3 . init ()
voces  =  motor . getProperty ( 'voces' )
motor . setProperty ( 'voz' , voces [ 0 ]. id )
def  hablar ( texto ):
    motor . decir ( texto )
    motor . runAndWait ()
def  red_and_talk ():
    text = text_info . get ( "1.0" , "end" )
    hablar ( texto )
def  write_text ( text_wiki ):
    text_info . insertar ( INSERT , text_wiki )
def  escuchar ( texto ):
    prueba :
        con  sr . Micrófono () como  fuente :
            hablar ( "Te escucho" )
            voz  =  oyente . escuchar ( fuente )
            rec  =  oyente . Recognition_google ( voz , idioma = 'es-ES' )
            rec  =  rec . inferior ()
            si el  nombre  en  rec :
                rec  =  rec . reemplazar ( nombre , '' )
                print ( "Usted dijo:"  +  rec )                                                
    excepto :
        aprobar

    volver  rec

    

#def funciones_básicas ():
 # rec = listen ('Funciones básicas ...')
def  run_Sandra ():
    # Música y Videos en YT
    rec  =  listen ( 'Escuchando ...' )
    si  'reproducir'  en  rec :
        música  =  rec . reemplazar ( 'reproducir' , '' )
        hablar ( 'Reproduciendo' +  música )
        pywhatkit . playonyt ( música )  
    #Hora
    elif  'dime la hora actual'  en  rec :
        hora  =  fecha y hora . fecha y hora . ahora (). strftime ( '% I:% M% p' )
        hablar ( "Son las"  +  hora )
                    
    #Fecha
    elif  'dime la fecha actual'  en  rec :
        fecha  =  fecha y hora . fecha y hora . ahora (). strftime ( '% d /% m /% Y' )
        hablar ( "Hoy es"  +  fecha )

    # Buscador 
    elif  'busca'  en  rec :
        order  =  rec . reemplazar ( 'busca' , '' )
        hablar ( 'Buscando' +  orden )
        pywhatkit . buscar ( orden )
    #Chistes
    elif  'dime un chiste'  en  rec :
        hablar ( pyjokes . get_joke ( 'es' ))
    
    elif  'créditos'  en  rec :
        navegador web . abierto ( 'https://www.youtube.com/watch?v=_KprFCkj2SU' )

#def funciones_avanzadas ():
    #rec = listen ('Funciones avanzadas ...')

    # Ejecución de aplicaciones.exe
    elif  'ejecuta'  en  rec :
        order  =  rec . reemplazar ( 'ejecuta' , '' )
        hablar ( 'Abriendo' +  orden )
        aplicación  =  orden + '.exe'
        os . sistema ( aplicación )

    # Creación de directorios
    elif  'crea el directorio'  en  rec :
        home  =  "C: \\ Users \\ INTEL \\ Desktop \\ Tareas \\ 3er SEMESTRE \\ Lenguaje de Programacion II \\ #Miscelaneos \\ "            
        order  =  rec . reemplazar ( 'crea el directorio' , '' )

        si  os . camino . existe ( orden ):
            hablar ( "El directorio ya existe" )

        otra cosa :
            mrk  =  os . mkdir ( inicio + pedido )
            talk ( "Se creo el directorio correctamente" )

    # Eliminación de directorios
    elif  'borra el directorio'  en  rec :
        order  =  rec . reemplazar ( 'borra el directorio' , '' )
        si  os . camino . existe ( orden ):
            rd  =  os . rmdir ( orden )
            hablar ( "Se elimino el directorio correctamente" )
        otra cosa :
            hablar ( "El directorio no existe" )

    # Creación de archivos de texto
    elif  'crea el archivo'  en  rec :
        order  =  rec . reemplazar ( 'crea el archivo' , '' )
        orden  =  orden + '.txt'
        si  os . camino . existe ( orden ):
            hablar ( "El archivo ya existe" )

        otra cosa :    
            archivo  =  abrir ( orden , "w" )
            archivo . cerrar ()
            talk ( "Se creo el archivo correctamente" )
                    
    # Eliminación de archivos de texto
    elif  'borra el archivo'  en  rec :
        order  =  rec . reemplazar ( 'borra el archivo' , '' )
        orden  =  orden + '.txt'
        si  os . camino . existe ( orden ):
            os . eliminar ( ordenar )
            talk ( "Se elimino el archivo correctamente" )
        otra cosa :
            hablar ( "El archivo no existe" )

    #Redireccionamiento de sitios web
    #elif 'entra a interbancario' en rec:
        #case = rec.replace ('entra a', '')
        #talk ("Entrando" + caso)
        # webbrowser.open ('https://bancaporinternet.interbank.pe/login')

    #Sin programar
    otra cosa :
        talk ( "No te entendi muy bien, vuelve a intentarlo" )
button_voice_mx = Botón ( ventana_principal , texto = "Voz Mex" , fg = "blanco" , bg = "# 00bf8f" ,
                      font = ( 'Apple Garamond' , 10 , "negrita" ), comando = voz_mexicana )
button_voice_mx . lugar ( x = 625 , y  = 80 , ancho = 100 , alto = 30 )
button_voice_es = Botón ( ventana_principal , texto = "Voz Esp" , fg = "blanco" , bg = "# FBD786" ,
                      font = ( 'Apple Garamond' , 10 , "negrita" ), command = spanish_voice )
button_voice_es . lugar ( x = 625 , y  = 115 , ancho = 100 , alto = 30 )
button_voice_us = Botón ( ventana_principal , texto = "Voz USA" , fg = "blanco" , bg = "# f12711" ,
                      font = ( 'Apple Garamond' , 10 , "negrita" ), command = english_voice )
button_voice_us . lugar ( x = 625 , y  = 150 , ancho = 100 , alto = 30 )
button_listen = Botón ( ventana_principal , texto = "Escuchar" , fg = "blanco" , bg = "# E94057" ,
                      fuente = ( 'Apple Garamond' , 15 , "negrita" ), ancho = 20 , alto = 3 , comando = ejecutar_Sandra )
button_listen . paquete ( pady = 10 )
button_speak = Botón ( ventana_principal , texto = "Hablar" , fg = "blanco" , bg = "# BB377D" ,
                      font = ( 'Apple Garamond' , 10 , "negrita" ), command =  red_and_talk )
button_speak . lugar ( x = 625 , y  = 190 , ancho = 100 , alto = 30 )
ventana_principal . mainloop ()
 
