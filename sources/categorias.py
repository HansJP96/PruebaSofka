from lista import lista_categorias
from preguntas import Preguntas


class Categorias:
    lista_Categorias = lista_categorias()

    def __init__(self, ronda=1):
        """
        Constructor para la clase Cateogrias.\n Recibe como parametro la ronda del jugador para gestionar la
        categoria de preguntas que corresponden a la ronda.

        :param ronda: int
        """
        self.ronda = ronda
        self.categoria = list(self.lista_Categorias)[self.ronda]

    def listar_pregunta(self) -> str:
        """
        Metodo que inicianilza la calse Preguntas y  devuelve la pregunta seleccionada de forma aletoria con su
        informacion respectiva como pregunta, opciones y respuesta.

        :return: Respuesta correcta de la pregunta
        """
        categoria_actual = Preguntas(self.lista_Categorias[self.categoria])
        print(f"Ronda {self.ronda}: Categoria de {self.categoria}")
        respuesta = categoria_actual.elegir_pregunta()
        return respuesta

    def len_categorias(self) -> int:
        """
            Metodo que calcula el tamaño de lista de categorias "lista_Categorias"

        :return: int
        """
        tamano = len(self.lista_Categorias) - 1
        return tamano
