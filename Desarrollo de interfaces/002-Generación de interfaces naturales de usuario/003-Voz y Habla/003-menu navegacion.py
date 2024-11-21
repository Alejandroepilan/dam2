import speech_recognition as sr                                             

reconocimiento = sr.Recognizer()                                            

def reconocer():                                                            
  with sr.Microphone() as origen:                                         
    print("Ajustando ruido de fondo")                                   
    reconocimiento.adjust_for_ambient_noise(origen, duration=1)         
    print("Tus opciones:")
    print("1.-INSERTAR un nuevo registro")
    print("2.-LISTAR registros")
    print("3.-ACTUALIZAR un registro")
    print("4.-ELIMINAR un registro")
    print("Escuchamos...")                                              
    audio = reconocimiento.listen(origen)                               

    try:                                                                
      print("Reconociendo...")                                        
      text = reconocimiento.recognize_google(audio, language="es-ES")                   
      print(f"Reconocido: {text}")                                    
    except sr.RequestError:                                             
      print("Error 1")
    except sr.UnknownValueError:
      print("Error 2")

reconocer()                                                                 