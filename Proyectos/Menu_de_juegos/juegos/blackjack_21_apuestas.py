# Crupier está obligado a pedir carta siempre que su puntuación sume 16 o menos, y obligado a plantarse si suma 17 o más.
# En el caso del crupier, los ases valen 11 mientras no se pase de 21, y 1 en caso contrario
# Las cartas numéricas suman su valor, las figuras suman 10 y el 'as' vale 11 o 1
import random
cartas = ['as', 'dos', 'tres', 'cuatro', 'cinco', 'seis',
          'siete', 'ocho', 'nueve', 'diez', 'jota', 'reina', 'rey']


def apuesta_usuario():
    preg = True
    while preg:
        try:
            rta_apuesta = int(input(
                '¿Cuanto deseas apostar? \n1._ $0 \n2._ $10 \n3._ $20 \n4._ $50 \n5._ $100 \n#: '))
            if rta_apuesta == 1:
                apuesta = 0
                preg = False
            elif rta_apuesta == 2:
                apuesta = 10
                preg = False
            elif rta_apuesta == 3:
                apuesta = 20
                preg = False
            elif rta_apuesta == 4:
                apuesta = 50
                preg = False
            elif rta_apuesta == 5:
                apuesta = 100
                preg = False
        except ValueError:
            print(
                "Ingreso Incorrectamente la respuesta, debe ingresar numero entre 1 y 5")
            preg = True
    return apuesta


def obtener_nueva_carta():
    maxi = len(cartas)
    indice = random.randint(0, maxi)-1
    return cartas[indice]


def valor_mano(mano):
    """Calcula el valor de mano, elige el valor del AS de acuerdo situación"""
    valor_mano = 0
    hay_as = False
    for carta in mano:
        valor_carta = cartas.index(carta)+1
        if valor_carta > 10:
            valor_carta = 10
        if carta == 'as':  # busca si la mano tiene un 'as' en ella
            hay_as = True
        valor_mano += valor_carta
    if hay_as and valor_mano <= 11:  # comprobamos si el valor de la mano es menor a 10 y si hay un 'as' presente el valor del 'as' pasa a ser 11
        valor_mano += 10
    return valor_mano


def juega_crupier():
    while valor_mano(mano_crupier) < 17:
        nueva_carta = obtener_nueva_carta()
        mano_crupier.append(nueva_carta)
    return mano_crupier


def print_resultado():
    print(f'Tu mano posee las cartas {
        mano_player}, valor de la mano es {valor_mano(mano_player)}')
    print(f'El crupier tiene las cartas {
        mano_crupier} sumaron: {valor_mano(mano_crupier)}')


continuar = True
saldo = 1000
apuesta = 0
print('='*100)
print(' Bienvenidos a Jack Black Informatorio 2024')
print('-'*100)

while continuar:
    suma_apuesta = 0
    # inicializamos la mano del jugador y de la computadora con dos cartas cada uno
    mano_player = [obtener_nueva_carta(), obtener_nueva_carta()]
    # mano_player = ['dos', 'dos']  # para testear
    mano_crupier = [obtener_nueva_carta(), obtener_nueva_carta()]
    print(f' Su saldo total es $$$ {saldo} ')
    apuesta = apuesta_usuario()  # opciones de valores de apuesta de susuario
    suma_apuesta += apuesta
    saldo -= apuesta
    repartir = True
    while repartir:  # juega el jugador
        # si el jugador hace BlackJack, sumando 21 con un 'as y carta q vale 10, gana la partida
        if valor_mano(mano_player) == 21:
            print_resultado()
            print('¡¡¡Black Jack!!! \n¡Felicidades Ganaste la mano, Sumaste 21!')
            saldo += (suma_apuesta*2)
            print(f"Ganaste $ {suma_apuesta*2} \n saldo total es $$$ {saldo} ")
            print('-'*100)
            break
        else:
            print(f'Tu mano posee las cartas {
                mano_player}, valor de la mano es {valor_mano(mano_player)}')
            print(f'La carta Visible del Crupier es: {mano_crupier[0]}')
            # preguntamos si quiere otra carta o se planta y la apuesta
            respuesta = input("¿Desea Repartir nueva carta, S o N?, ").upper()
            if respuesta == "S":  # si responde si, se le asigna nueva carta
                apuesta = apuesta_usuario()
                suma_apuesta += apuesta
                saldo -= apuesta
                nueva_carta = obtener_nueva_carta()
                mano_player.append(nueva_carta)
                # si el jugador se pasa de 21 termina la partida
                if valor_mano(mano_player) > 21:
                    juega_crupier()  # funcion para q el crupier juegue cartas
                    print(f'tu Nueva carta es: {nueva_carta}')
                    print(
                        '¡¡¡Termino la partida, te pasaste de 21, has perdido!!!')
                    print_resultado()  # imprime los resultados con esta
                    print(f"Perdiste $ {
                          suma_apuesta} y tu saldo total es $$$ {saldo}")
                    break
                else:
                    print(f'tu Nueva carta es: {nueva_carta}')
                continue
            elif respuesta == "N":
                # turno de la pc,decide si pedir nueva carta o no, si sumatoria es menor a 17
                juega_crupier()  # funcion para q el crupier juegue cartas
            else:
                respuesta = input(
                    "¡¡¡ERROR!!!! Ingrese solo (S para continuar, N para terminar): ").upper()
    # desde aca comparamos resultados
            if valor_mano(mano_crupier) == 21 and valor_mano(mano_player) < 21:
                print('¡¡¡Perdiste el crupier las tiene mejores!!!')
                print_resultado()
                print(f"Perdiste $ {
                      suma_apuesta} y tu saldo total es $$$ {saldo}")
                break
            elif valor_mano(mano_crupier) > 21:
                print("¡¡¡Ganaste!!! El crupier se paso de rosca y sumo mas de 21")
                saldo += (suma_apuesta*2)
                print(f"Ganaste $ {suma_apuesta *
                      2}, saldo total es $$$ {saldo} ")
                print_resultado()
                break
            elif valor_mano(mano_crupier) == valor_mano(mano_player):
                print("¡¡¡Empate!!!")
                saldo += suma_apuesta
                print(f'Su saldo total es $$$ {saldo}')
                print_resultado()
                break
            elif valor_mano(mano_crupier) < valor_mano(mano_player):
                print("¡¡¡Ganaste!!!")
                saldo += (suma_apuesta*2)
                print(f'Ganaste $ {suma_apuesta *
                      2},y tu saldo total es $$$ {saldo}')
                print_resultado()
                break
            elif valor_mano(mano_player) == 21:
                print('¡¡¡Black Jack!!! \n¡Felicidades Ganaste la mano, Sumaste 21!')
                saldo += (suma_apuesta*2)
                print(f'Ganaste $ {suma_apuesta *
                      2}, y tu saldo total es $$$ {saldo}')
                print_resultado()
                break
            else:  # cuando el crupier tiene mejores cartas que jugador
                print('¡¡¡Perdiste el crupier las tiene mejores!!!')
                print(f"Perdiste $ {
                      suma_apuesta}, y tu saldo total es $$$ {saldo}")
                print_resultado()
                break
    print('-'*100)
# chequeamos si se desea seguir Jugando
    rta = True
    while rta:
        respuesta = input("¿Desea repartir nueva mano?, S o N? ").upper()
        if respuesta == "S":
            continuar = True
            rta = False
        elif respuesta == "N":
            continuar = False
            print("Saliendo del Programa....")
            print("="*100)
            break
        else:
            print("¡¡¡ERROR!!!! Ingrese solo (s para continuar, n para terminar): ")
            rta = True
    print('='*100)
