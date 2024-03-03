import math
import time
from jugador import Humano, Computadora

#Líbrerias para animación
import time
from turtle import *
import turtle

class TicTacToe():
    def __init__(self):
        self.tablero = self.crear_tablero()
        self.ganador_actual = None

    @staticmethod
    def crear_tablero():
        return [' ' for _ in range(9)]

    def imprimir_tablero(self):
        time.sleep(1)
        t = turtle.Turtle()
        t.width(3)  #Grosor de 3 píxeles
            
        turtle.title("Práctica 1 | Tic Tac Toe")
        turtle.Screen().bgcolor("black")
        turtle.Screen().setup(600, 600)
        Screen()._root.resizable(False, False)
        coordenadasX = -225 #Para setear la cuadrícula en -225 de X
            
        t.up()
        t.goto(-225,250)
        t.down()

        for i in range(0, 3):
            #Cuadricula inicial
            t.color('black') #El mismo color del fondo para esconder el desplazamiento
            t.speed(-100) #Velocidad de la tortuga
            t.color('#074DD9')
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            coordenadasX = coordenadasX + 150
            t.up()
            t.goto(coordenadasX,250)
            t.down()
        t.hideturtle()

        coordenadasX2 = -225

        t.up()
        t.goto(-225,100)
        t.down()

        for i in range(0, 3):
            #Segunda Fila
            t.color('black')
            t.speed(-100)
            t.color('#074DD9')
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            coordenadasX2 = coordenadasX2 + 150
            t.up()
            t.goto(coordenadasX2,100)
            t.down()
        coordenadasX3 = -225

        t.up()
        t.goto(-225,-50)
        t.down()

        for i in range(0, 3):
            #Tercer Fila
            t.color('black')
            t.speed(-100)
            t.color('#074DD9')
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)
            coordenadasX3 = coordenadasX3 + 150
            t.up()
            t.goto(coordenadasX3,-50)
            t.down()
        t.hideturtle()

        #Dibujamos letras
        for i in range(9):
            fila = i // 3
            col = i % 3
            x = -225 + col * 160 + 60
            y = 250 - fila * 160 - 60
            if self.tablero[i] == 'X':
                self.DX(x, y)
            elif self.tablero[i] == 'O':
                self.DO(x, y)
                
    def DX(self, x, y):
        t = turtle.Turtle()
        t.up()
        t.goto(-225, 250)
        t.down()
        t.color('black')
        t.speed(0)
        t.color('#F2E205')
        t.penup()
        t.goto(x - 30, y - 30)
        t.pendown()
        t.width(5)
        t.goto(x + 30, y + 30)
        t.penup()
        t.goto(x + 30, y - 30)
        t.pendown()
        t.goto(x - 30, y + 30)
        t.penup()
        t.hideturtle()

    def DO(self, x, y):
        t = turtle.Turtle()
        t.color('black')
        t.speed(0)
        t.color('#05F2DB')
        t.penup()
        t.goto(x, y - 30)
        t.pendown()
        t.width(5)
        t.circle(30)
        t.penup()
        t.hideturtle()

    #Mostramos posiciones en el tablero
    @staticmethod
    def posicion():
        print('\n✭ Posiciones Del Tablero:\n')
        # 0 | 1 | 2
        posicion = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for fila in posicion:
            print('| ' + ' | '.join(fila) + ' |')

    #Actualizamos tablero y verificamo ganador
    def movimiento(self, cuadrado, letra):
        if self.tablero[cuadrado] == ' ':
            self.tablero[cuadrado] = letra
            if self.ganador(cuadrado, letra):
                self.ganador_actual = letra
            return True
        return False

    def ganador(self, cuadrado, letra):
        #Verificamos la fila
        fila_ind = math.floor(cuadrado / 3)  #Índice de fila
        fila = self.tablero[fila_ind*3:(fila_ind+1)*3]  #Extraemos fila

        if all([s == letra for s in fila]):  #Comprobamos si todas las posiciones de la fila tienen la misma letra
            return True
        
        #Verificamos columna
        col_ind = cuadrado % 3  #Índice de columna
        columna = [self.tablero[col_ind+i*3] for i in range(3)]  #Extraemos la columna del tablero
        if all([s == letra for s in columna]):  #Comprobamos si todas las posiciones de la columna tienen la misma letra
            return True
        
        #Verificamos diagonales
        if cuadrado % 2 == 0:  #Solo para cuadrados en posiciones diagonales
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]]  #Primer diagonal
            if all([s == letra for s in diagonal1]):  #Comprobamos si todas las posiciones tienen la misma letra
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]]  #Segunda diagonal
            if all([s == letra for s in diagonal2]):  #Comprobamos si todas las posiciones tienen la misma letra
                return True
        return False  #Mientras no se cumplan => No hay ganador

    def vacios(self):
        return ' ' in self.tablero

    def num_vacios(self):
        return self.tablero.count(' ')

    def mov_disponible(self):
        return [i for i, x in enumerate(self.tablero) if x == " "]


def juego(juego, JugadorX, JugadorO, Resultado=True):

    if Resultado:
        juego.posicion()  #Posición inicial del tablero

    letra = 'X'  #Inicia jugador X
    while juego.vacios():  #Mientras haya casillas vacías en el tablero
        if letra == 'O':
            cuadrado = JugadorO.obt_movimiento(juego)  #Jugador O realiza un movimiento
        else:
            cuadrado = JugadorX.obt_movimiento(juego)  #Jugador X realiza un movimiento
        if juego.movimiento(cuadrado, letra):  #Intenta realizar el movimiento en el tablero

            if Resultado:
                print('\nꕥ   El Jugador "' + letra + '" hace un movimiento en el cuadrado {}'.format(cuadrado))
                juego.imprimir_tablero()
                print('')

            if juego.ganador_actual:  #Verificamos si hay un ganador después del movimiento
                if Resultado:
                    print('\n⋆ ★ ¡El jugador "' + letra + '" es el ganador! ⋆ ★\n')
                    turtle.exitonclick()
                return letra  #Finaliza el juego y devuelvemos la letra del jugador ganador
            letra = 'O' if letra == 'X' else 'X'  #Cambiamos de jugador

        time.sleep(.8)  #Espera antes del próximo movimiento

    if Resultado:
        print("\n★ ¡EMPATE!\n")
        turtle.exitonclick()
    return None

if __name__ == '__main__':
    print("\n----------------Práctica 1 | Juego Del Gato (tic tac toe)----------------\n")
    decision = input("1. Humano vs Computadora\n2. Computadora vs Computadora\n3. Salir\n\n")

    if decision == '1':
        JugadorX = Computadora('X')
        JugadorO = Humano('O')
        t = TicTacToe()
        juego(t, JugadorX, JugadorO, Resultado=True)

    elif decision == '2':
        JugadorX = Computadora('X')
        JugadorO = Computadora('O')
        t = TicTacToe()
        juego(t, JugadorX, JugadorO, Resultado=True)
    
    elif decision == '3':
        print("\n¡Hasta luego! ♥\n")
        exit()

    else:
        print("\n☢ ERROR: Ingrese una opción válida \n\n")
        print("\n¡Hasta luego! ♥\n")
        exit()