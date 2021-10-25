import random


class Preguntas:

    def __init__(self, categoria_preguntas: list):
        """
        Constructor para la clase Preguntas.\n Recibe como parametro la informacion de la categoria respectiva a la
        ronda de juego y gestiona la eleccion de forma aleatoria de la pregunta a mostrar al jugador.

        :param categoria_preguntas: Lista de objetos diccionario con informacion de las preguntas.
        """
        self.num_pregunta = random.randint(0, 4)
        self.lista_preguntas = categoria_preguntas

    def elegir_pregunta(self) -> str:
        """
        Metodo que selecciona la pregunta de forma aleatoria y muestra al jugador la pregunta y sus opciones.
        Devuelve la respuesta correcta para posterior verificacion con la seleccion del jugador. :return:
        """
        pregunta = self.lista_preguntas[self.num_pregunta]
        for i in pregunta:
            if i == "Respuesta":
                respuesta = pregunta[i]
                return respuesta
            else:
                if i == "Opciones":
                    for opcion in pregunta[i]:
                        self.imprimir(opcion)
                else:
                    self.imprimir(pregunta[i])

    def imprimir(self, mensaje: str):
        """
            Metodo que imprime al usuario la pregunta y sus opciones.
        :rtype: str
        """
        print(mensaje)
