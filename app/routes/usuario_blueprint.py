from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..controllers.usuario_controlller import UserController  # Importa el controlador

auth = Blueprint('auth', __name__)

auth.route('/login', methods=['GET', 'POST'])(UserController.login)
auth.route('/register', methods=['GET', 'POST'])(UserController.register)
auth.route('/welcome')(UserController.welcome)
auth.route('/perfil', methods=['GET'])(UserController.perfil)
auth.route('/modificar_dato', methods=['PUT'])(UserController.modificar_dato)
auth.route('/cambiar_contrasena', methods=['PUT'])(UserController.cambiar_contrasena)