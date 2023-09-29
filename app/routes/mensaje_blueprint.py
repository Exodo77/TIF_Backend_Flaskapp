from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje', __name__)

mensaje_bp.route('/obtener_mensajes_canal/<int:canalID>', methods=['GET'])(MensajeController.obtener_mensajes)
mensaje_bp.route('/enviar_mensaje', methods=['POST'])(MensajeController.enviar_mensaje)
