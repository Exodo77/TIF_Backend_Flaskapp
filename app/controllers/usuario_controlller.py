from flask import render_template, request, redirect, url_for, flash, session, jsonify
from datetime import datetime
from passlib.hash import sha256_crypt
from ..models.auth.usuario_model import Usuario  # Importa la clase Usuario

class UserController:

    @classmethod
    def login(cls):
        """FUNCION DE LOGUEO"""
        if request.method == 'POST':
            data = request.json  # Utiliza request.json para obtener los datos enviados
            if data:
                email = data.get('correo')
                password = data.get('contrasena')
                user = Usuario.iniciar_sesion(email, password)

                if user:
                    session['user_id'] = user['user_id']
                    session['user_name'] = user['user_name']
                    return jsonify({"message": "Sesión iniciada"}), 200
                else:
                    return jsonify({"message": "Credenciales incorrectas. Inténtalo de nuevo."}), 401
            else:
                return jsonify({"message": "Datos de inicio de sesión no proporcionados"}), 400
        return render_template('login.html')
    
    @classmethod
    def register(cls):
        """FUNCION DE REGISTRO"""
        if request.method == 'POST':
            data = request.json  # Utiliza request.json para obtener los datos enviados
            if data:
                username = data.get('username')
                name = data.get('name')
                lastname = data.get('lastname')
                password = data.get('password')
                email = data.get('email')
                dia = int(data.get('dia'))
                mes = int(data.get('mes'))
                anio = int(data.get('anio'))

                existing_user = Usuario.obtener_usuario_por_correo(email)

                if existing_user:
                    return jsonify({"message": "El correo electrónico ya está en uso."}), 400
                else:
                    fecha_nacimiento_str = f"{anio}-{mes:02d}-{dia:02d}"
                    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
                    if Usuario.registrar_usuario(username, name, lastname, email, password, fecha_nacimiento):
                        return jsonify({"message": "Registro exitoso. Ahora puedes iniciar sesión."}), 200
                    else:
                        return jsonify({"message": "Error en el registro. Inténtalo de nuevo."}), 500
            else:
                return jsonify({"message": "Datos de registro no proporcionados"}), 400

        return render_template('register.html')

    @classmethod
    def welcome(cls):
        """FUNCION DE BIENVENIDA"""
        if 'user_id' in session:
            user_id = session['user_id']
            user_name = session['user_name']
            # Obtener la lista de servidores a los que pertenece el usuario
            servidores = Usuario.obtener_servidores_del_usuario(user_id)
            print(servidores)#id del servidor
            no_pertenece_a_servidor = not servidores  # True si no pertenece a ningún servidor, False si pertenece a al menos uno
            return render_template('welcome.html', user_name=user_name, user_id=user_id, servidores=servidores, no_pertenece_a_servidor=no_pertenece_a_servidor)
        else:
            flash("Debes iniciar sesión para ver esta página.")
            return redirect(url_for('auth.login'))
        
    @classmethod
    def perfil(cls):
        """RETORNA LOS DATOS DE UN USUARIO"""
        print("Llego hasta perfil")
        user_id = request.args.get('user_id')
        user=Usuario.get(user_id)
        usuario = {
            "userID": user[0],
            "nombreusuario": user[1],  # Reemplaza con el nombre del autor si es necesario
            "nombre": user[2],  # Reemplaza con el contenido del mensaje
            "apellido": user[3],
            "correo": user[4],
            "contraseña":user[5],
            "fecha_naciimiento": user[6].strftime("%Y-%m-%d %H:%M:%S"),
            "imagenURL": user[7]
        }
        # Verifica si la imagenURL es None o si no existe en la carpeta
        if usuario["imagenURL"] is None: 
            usuario["imagenURL"] = "/static/imag/user.png"
        return render_template('perfil.html', usuario=usuario)
    
    @classmethod
    def modificar_dato(cls):
        """MODIFICA LOS DATOS DE UN USUARIO"""
        print("Llego hasta modificar dato")
        data = request.json  # Utiliza request.json para obtener los datos enviados
        dato=data.get('nuevoDato')
        tipo=data.get('tipo')
        user_id = int(data.get('user_id'))
        resp=Usuario.modificar_dato(user_id,tipo,dato)
        if resp:
            return jsonify({"message": "Datos del usuario modificado correctamente"}), 200
        else:
            return jsonify({"message": "Error al modificar los datos"}), 400

    @classmethod
    def cambiar_contrasena(cls):
        """CAMBIA LA CONTRASEÑA DEL USUARIO HASHEADA"""
        print("Llego hasta cambiar contraseña")
        data = request.json  # Utiliza request.json para obtener los datos enviados
        actual=data.get('contrasenaActual')
        nuevaContrasena=data.get('nuevaContrasena')
        nuevaContrasena = sha256_crypt.hash(nuevaContrasena)
        user_id =int(data.get('user_id'))
        resp=Usuario.verifircar_contraseña(actual,user_id)
        if resp: 
            Usuario.modificar_dato(user_id,"contraseña",nuevaContrasena)
            return jsonify({"message": "Se ha modificado la Contraseña"}), 200
        else:
            return jsonify({"message": "Contraseña actual incorrecta"}), 400