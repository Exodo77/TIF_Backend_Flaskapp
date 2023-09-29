from ..BaseDatos import DatabaseConnection
from configuracion import credenciales

global cursor,conn


class Mensaje:
    def __init__(self, mensajeID, canalID, userID,contenido,fecha):
        self.mensajeID = mensajeID
        self.canalID = canalID
        self.userID = userID
        self.contenido=contenido
        self.fecha=fecha


    @classmethod
    def lista_mensaje(cls,canal_id):
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM mensaje WHERE canalID = %s"
            cursor.execute(query, (canal_id,))
            mensajes = cursor.fetchall()
            print("La lista de mensajes:",mensajes)
            return mensajes
        except Exception as e:
            return []
    
    @classmethod
    def crear_mensaje(cls,canal,user,cont):
        try :
            query = "INSERT INTO mensaje(canalID,userID,contenido) VALUES(%s,%s,%s)"
            val=(canal,user,cont)
            DatabaseConnection.insert_data(query,val)
            return True
        except Exception as e:
            print("Error al crea los mensajes:", e)
            return False
