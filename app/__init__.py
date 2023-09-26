from flask import Flask
from configuracion import credenciales
from configuracion import SECRET_KEY  # Importa la clave secreta desde tu archivo de configuración
from .routes.auth import auth  # Importa tu Blueprint de autenticación
from .routes.servidor_blueprint import servidor_bp 
from .routes.canal_blueprint import canal_bp
from .routes.mensaje_blueprint import mensaje_bp

def create_app():
    """Crea y configura la aplicación de Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config.from_object(credenciales)
    # Registra tus Blueprints aquí
    app.register_blueprint(auth)
    app.register_blueprint(servidor_bp)
    app.register_blueprint(canal_bp)
    app.register_blueprint(mensaje_bp)
    return app
