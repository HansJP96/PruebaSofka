import json
import os.path as archivo
import time

from categorias import Categorias
from jugadores import Jugador


class Ronda:
    opciones = ["a", "b", "c", "d"]

    def __init__(self, jugador: Jugador):
        """
            Constructor de la clase Ronda.\n
            Recibe un objeto de la clase de Jugador e inicializa atributos con base a la informacion del jugador en caso
            de que exista o se inicializa con los atributos por defecto de la clase jugador.

            :type jugador: Jugador
            :parameter jugador: Objeto
        """
        self.participante = jugador
        self.ronda = jugador.estado_partida[0]
        self.premio_acumulado = jugador.estado_partida[1]
        self.inc_premio = 100 if jugador.estado_partida == 0 else 50 * self.ronda + 50
        self.resp_correcta = ""
        self.max_ronda = Categorias().len_categorias()

    def jugar(self):
        """
        Metodo de inicializacion para cada ronda, en caso de ser la primera ronda se evita interaccion con el
        usuario, en caso contrario pregunta al usuario si desea continuar jugando o desea retirarse.

        :return: [Boolean, int]
        """
        if self.ronda == 1:
            return [True, self.ronda]
        elif self.participante.estado_partida[0] != 1:
            self.participante.estado_partida[0] = 1
            return [True, self.ronda]
        elif self.ronda <= self.max_ronda:
            continuar = ""
            while continuar != "s" and continuar != "n":
                continuar = input("Desea continuar jugando? (s/n): ")
                print()
                check = any(x in ["s", "n"] for x in continuar)
                if not check:
                    print("Por favor su respuesta debe ser s o n.\n [s=Si , n=No]\n")
            if continuar == "s":
                return [True, self.ronda]
            else:
                return [False, self.ronda]
        else:
            return [False, self.ronda]

    def pasar_ronda(self):
        """
            Metodo para avanzar de ronda en caso de que el jugador acierta correctamente las respuestas a las preguntas.
            No retorna valor.
        """
        self.ronda += 1

    def pregunta(self):
        """
            Metodo que inicializa la Clase Categorias para elegir la categoria de preguntas y posteriormente
            seleccionar la pregunta a mostrar al jugador.
            No retorna valor.
        """
        mostrar_pregunta = Categorias(self.ronda)
        self.resp_correcta = mostrar_pregunta.listar_pregunta()

    def select_resp(self):
        """
        Metodo que permite al usuario digitar una respuesta con base a la pregunta que se imprime y retorna su valor.

        :return: String
        """
        time.sleep(1)
        while True:
            seleccion = input("Cual de las opciones es la correcta? (a,b,c,d)\nR: ")
            print()
            if seleccion in self.opciones:
                break
            else:
                print("Respuesta no valida.\nPor favor seleccione la respuesta entre a,b,c,d.\n")
                time.sleep(1)
        return seleccion

    def resp_acertada(self, resp_seleccionada: str):
        """
        Metodo que recibe como parametro la respuesta seleccionada por el jugador y verifica si coincide con la
        respuesta verdadera para la pregunta dada.

        :type resp_seleccionada: str
        :returns: Boolean
        """
        if resp_seleccionada == self.resp_correcta:
            self.premio_ronda()
            self.inc_premio += 50
            return True
        else:
            return False

    def premio_ronda(self):
        """
            Metodo que gestiona los premios otorgados al jugador con base a la ronda en la que se encuentra.
        """
        if self.ronda == 1:
            self.premio_acumulado = self.inc_premio
        else:
            self.premio_acumulado = self.premio_acumulado + self.inc_premio

    def guardar_jugador(self):
        """
            Metodo que guarda la informacion final del jugador en el archivo data.json.
            Si el jugador existia previamente, actualiza su historial con la informacion de la partida actual.
            Por el contrario añade al jugador al archivo con la informacion actual de la partida.
        """
        path = "data/data.json"
        listado_jugadores = []
        if archivo.exists(path):
            with open(path, "r") as jugadores:
                try:
                    listado_jugadores = json.load(jugadores)
                    for jugador in listado_jugadores:
                        if jugador["cedula"] == self.participante.cedula:
                            jugador["nombre"] = self.participante.nombre
                            jugador["estado_partida"] = self.participante.estado_partida
                            jugador["partidas_totales"] = self.participante.partidas_totales
                            jugador["partidas_ganadas"] = self.participante.partidas_ganadas
                            jugador["partidas_perdidas"] = self.participante.partidas_perdidas
                            break
                    else:
                        listado_jugadores.append(self.participante.__dict__)
                except json.JSONDecodeError:
                    pass
        with open(path, "w+") as nuevo:
            if len(listado_jugadores) != 0:
                json.dump(listado_jugadores, nuevo, indent=4, sort_keys=True)
            else:
                json.dump([self.participante.__dict__], nuevo, indent=4, sort_keys=True)

    def juego_ganado(self):
        """
        Metodo que actualiza los atributos de la clase Jugador antes de guardar la informacion del mismo cuando ha
        ganado exitosamente el juego.
        """
        self.participante.partidas_totales += 1
        self.participante.partidas_ganadas += 1
        self.participante.estado_partida = [1, 0]

    def juego_perdido(self):
        """
        Metodo que actualiza los atributos de la clase Jugador antes de guardar la informacion del mismo cuando ha
        perdido el juego.
        """
        self.participante.partidas_totales += 1
        self.participante.partidas_perdidas += 1
        self.participante.estado_partida = [1, 0]

    def juego_pausado(self):
        """
        Metodo que actualiza los atributos de la clase Jugador antes de guardar la informacion del mismo cuando el
        jugador se ha retirado voluntariamente. Actualiza la informacion de la partida actual para que el jugador
        pueda retornar en la ronda donde se retiro.
        """
        self.participante.estado_partida[0] = self.ronda
        self.participante.estado_partida[1] = self.premio_acumulado
