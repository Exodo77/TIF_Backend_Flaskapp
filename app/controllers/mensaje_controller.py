# mensaje_controller.py
from flask import request, jsonify
from ..models.mensaje_model import Mensaje
from ..models.auth.usuario_model import Usuario

class MensajeController:
    @classmethod
    def obtener_mensajes(cls, canalID):
        print(canalID)
        print("Llegó hasta obtener mensajes")
        mensajes=Mensaje.lista_mensaje(int(canalID))
        if len(mensajes) >0:
            # Formatear los mensajes en el formato deseado
            formatted_messages = []
            for mensaje in mensajes:
                formatted_message = {
                    "canalID": mensaje[0],
                    "autor": Usuario.obtener_userName(mensaje[2]),  # Reemplaza con el nombre del autor si es necesario
                    "contenido": mensaje[3],  # Reemplaza con el contenido del mensaje
                    "fecha_envio": mensaje[4].strftime("%Y-%m-%d %H:%M:%S")
                }
                formatted_messages.append(formatted_message)
                print(formatted_messages)
            return jsonify(formatted_messages),200 # Devolvemos los mensajes como JSON
        else:
            lista=[{"canalID": 0, "autor": "servidor", "contenido": "Bienvenido comienza a mandar mensajes", "fecha_envio": "2023-09-25 19:14:02"}]
            return jsonify(lista),200
    
    @classmethod
    def enviar_mensaje(cls):
        print("Llego hasta enviar_mensaje")
        data = request.json
        canal_id = data.get('canal_id')
        texto = data.get('texto')
        user_id=data.get('user_id')
        resul=Mensaje.crear_mensaje(canal_id,user_id,texto)
        print(resul)
        if resul:
            return jsonify({'message': 'Mensaje enviado con éxito'}),200
        else:
            return jsonify({'message': 'Error al enviar el mensaje'}),500
