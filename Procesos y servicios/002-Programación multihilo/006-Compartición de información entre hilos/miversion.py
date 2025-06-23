from flask import Flask, request, jsonify                            
from flask_cors import CORS

mensajes = []                                               

app = Flask(__name__)                                       
CORS(app)

@app.route('/')                                             
def inicio():                                               
    return "Hola mundo"                                     
    
@app.route('/dame')                                         
def dame():                                                 
    global mensajes                                         
    return jsonify(mensajes)                                    

@app.route('/toma')                                         
def toma():                                                 
    global mensajes                                         
    mensaje = request.args.get('mensaje')                   
    usuario = request.args.get('usuario')                   
    mensajes.append({'mensaje':mensaje,'usuario':usuario})  
    return str({"mensaje":"ok"})                            

if __name__ == '__main__':                                  
    app.run(debug=True, host='127.0.0.1')               
