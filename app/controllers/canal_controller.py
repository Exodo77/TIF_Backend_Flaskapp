from flask import request, jsonify
from ..models.canal_model import Canal

class CanalController:

    @classmethod
    def obtener_canales_servidor(cls, servidor_id):
        """OBTIENE LOS CANALES DE LOS SERVIDORES"""
        print("Llego asta obtener canales servidor")
        try:
            canales=Canal.obtener_canales(servidor_id)
            # Devuelve una respuesta JSON con los canales
            return jsonify(canales), 200
        except Exception as e:
            # Devuelve una respuesta JSON con un mensaje de error si hay un problema
            response = {'message': 'Error al obtener los canales del servidor'}
            return jsonify(response), 500

    @classmethod    
    def crear_canal(cls):
        """CREA UN CANAL"""
        try:
            data = request.json
            nombre_canal = data.get('nombre_canal')
            servidor_id = int(data.get('servidor_id'))#servidor_id lo obtiene como un string
            resul =Canal.crear_canal(servidor_id, nombre_canal)
                # Devuelve una respuesta JSON exitosa si el canal se crea con éxito
            return jsonify({'message': 'Canal creado con éxito'}), 200
        except Exception as e:
            # Devuelve una respuesta JSON con un mensaje de error si hay un problema
            return jsonify({'message': 'Error en crear canal'}), 500
