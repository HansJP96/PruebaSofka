import json
import os.path as archivo
import time


class Jugador:
    def __init__(self):
        """
            Constructor para la clase Jugador.
            Esta clase no recibe parametros, se establecen atributos predefinidos
            para cada jugador y se modifican a medida que se ejecuta el script.
        """
        self.nombre = ""
        self.cedula = ""
        self.estado_partida = [1, 0]
        self.partidas_totales = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0

    def get_nombre(self):
        """
            No recibe parametros y retorna el nombre del jugador actual.
        :return Nombre de jugador
        """
        return self.nombre.capitalize()

    def set_identificacion(self):
        """
            Al ejecutarse solicita al jugador que digite sus datos nombre y cedula. Si anteriormente habia jugado,
            extrae la informacion del archivo data.json y actualiza el estado del jugador, si el jugador es nuevo
            modifica los parametros de nombre y cedula del constructor de clase.

            No recibe parametros, se inicializan variables temporales para el manejo de la informacion.

        """
        counter = 0
        nombre = ""
        cedula = ""
        while nombre == "" or cedula == "" or not cedula.isdigit():
            if counter == 0:
                nombre, cedula = input(
                    "¡ Bienvenido al Concurso de Preguntas y Respuestas !\nPor favor, ingrese un nombre y cedula (sin "
                    "puntos o comas) para empezar:\n(Nota: Si ha participado antes, asegurese de digitar la misma "
                    "cedula, el nombre no sera modificado)\nNombre:\t"), input(
                    "Cedula:\t")
                counter += 1
            else:
                print(
                    "¡ Por favor ingrese un informacion valida !\nLa cedula debe estar formado solo por numeros digitos")
                nombre, cedula = input("Nombre:\t"), input("Cedula:\t")
        check = self.check_jugador(cedula)
        if check:
            print("Usted ya habia participado anteriormente, estos eran sus datos:\n")
            print(self.datos_jugador())
            time.sleep(3)
            if self.estado_partida[0] != 1:
                print(
                    f"Comenzara su juego en la ronda {self.estado_partida[0]} y tiene acumulado {self.estado_partida[1]}.\n")
                time.sleep(2)
            else:
                print(f"Para esta ronda 1 usted jugara por un premio de 100 $ !!!\n")
                time.sleep(2)
        else:
            self.nombre = nombre
            self.cedula = cedula
            print(f"Para esta ronda 1 usted jugara por un premio de 100 $ !!!\n")
            time.sleep(2)

    def check_jugador(self, cedula: str):
        """
            Verifica la existencia del jugador en el archivo data.json y retorna False o True.

        :param cedula: String
        :return: Boolean
        """
        path = "data/data.json"
        if archivo.exists(path):
            with open(path, "r") as jugadores:
                try:
                    listado_jugadores = json.load(jugadores)
                    for informacion in listado_jugadores:
                        if informacion["cedula"] == cedula:
                            self.nombre = informacion["nombre"]
                            self.cedula = informacion["cedula"]
                            self.estado_partida = informacion["estado_partida"]
                            self.partidas_totales = int(informacion["partidas_totales"])
                            self.partidas_ganadas = int(informacion["partidas_ganadas"])
                            self.partidas_perdidas = int(informacion["partidas_perdidas"])
                            return True
                    else:
                        return False
                except json.JSONDecodeError:
                    return False
        else:
            return False

    def datos_jugador(self):
        """
            Genera un String con la informacion del jugador en caso de que exista en el archivo data.json

        :return: String
        """
        return (f"Nombre: {self.nombre}\nCedula: {self.cedula}\nEstado de partida previa: {self.estado_partida}\n"
                f"Partidas totales: {self.partidas_totales}\nPartidas ganadas: {self.partidas_ganadas}\n"
                f"Partidas perdidas: {self.partidas_perdidas}\n")
