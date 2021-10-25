from jugadores import Jugador
from ronda import Ronda
'''
    El archivo main es el script principal que permite la ejecutacion de la aplicacion.
    Por favor no modifque la ubicacion de los archivos .py y subcarpetas.
'''
persona = Jugador()
persona.set_identificacion()

partida = Ronda(persona)
print(f"Muy bien participante {persona.nombre.capitalize()}\n ¡¡¡ Vamos a empezar a jugar !!!")
input("Presione enter para seguir\n")

while True:
    estado, ronda = partida.jugar()
    if estado:
        partida.pregunta()
        respuesta = partida.select_resp()
        verificacion = partida.resp_acertada(respuesta)
        if verificacion:
            if ronda < 5:
                print(
                    f"Felicidades ha completado con exito la ronda {ronda} con un acumulado de {partida.premio_acumulado} $. "
                    f"\nPreparese para la ronda {ronda + 1} por un premio de {partida.inc_premio} $ !!!!\n")
                partida.pasar_ronda()
            else:
                partida.pasar_ronda()
        else:
            print("Que lastima, ha perdido en esta ronda.\nSuerte para la proxima ;)\n")
            partida.juego_perdido()
            partida.guardar_jugador()
            break
    else:
        if ronda > 5:
            print(
                f"Enhorabuena {persona.nombre}, usted acaba de ganar este concurso y se llevará nada menos que {partida.premio_acumulado} "
                f"$ !!!!")
            partida.juego_ganado()
            partida.guardar_jugador()
        else:
            print("Regrese cuando se sienta mas seguro.\n")
            partida.juego_pausado()
            partida.guardar_jugador()
        break
