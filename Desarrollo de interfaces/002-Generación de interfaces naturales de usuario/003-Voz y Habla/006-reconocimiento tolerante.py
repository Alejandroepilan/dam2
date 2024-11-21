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
      if "insertar" in text:
        print("operación de insertar reconocida, vamos a inserar un nuevo registro")
      elif "listar" in text:
        print("operación de listar reconocida, vamos a por la lista de clientes")
      elif "actualizar" in text:
        print("operación de actualizar reconocida, vamos a actualizar un cliente")
      elif "eliminar" in text:
        print("operación de listar reconocida, vamos a eliminar un cliente")
      else:
        print("Lo que has dictado no ha sido reconocido")
    except sr.RequestError:                                             
      print("Error 1")
    except sr.UnknownValueError:
      print("Error 2")
    reconocer()

reconocer()                                                                 