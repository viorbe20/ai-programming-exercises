# Tic-Tac-Toe

## Índice
[1. Introducción el juego](#1-introducción-al-juego)
[2. Clase *Player*](#2-clase-player)
[3. Clase *RandomComputerPlayer*](#3-clase-randomcomputerplayer)
[4. Clase *HumanPlayer*](#4-clase-humanplayer)


### 1. Introducción al juego 

Esta versión del juego está diseñada para dos jugadores: humano vs. máquina 

### 2. Clase *Player*
La clase *Player* es la clase base para los jugadores del juego, y tiene dos subclases: *RandomComputerPlayer* y *HumanPlayer*. Representa a un jugador genérico en el juego de tres en línea. Cada jugador tiene un carácter asignado ('X' u 'O') que se define al crear la instancia.

#### Métodos:
1. Método Constructor. Inicializa la instancia del jugador con su letra asignada ('X' u 'O').
2. get_move(self, game). Método implementado por las subclases y se encarga de obtener el movimiento del jugador.

[Índice](#índice)

### 3. Clase *RandomComputerPlayer*
Hereda de la clase *Player* y representa al ordenador como jugador. La selección de las casillas se hará de manera aleatoria.

#### Métodos
1. Método Constructor. Llama al constructor de la clase madre e inicializa la instancia del jugador del ordenador.
2. *get_move(self, game)*. Método para elegir una casilla vacía aleatoria en el tablero.

[Índice](#índice)

### 4. Clase *HumanPlayer*:
Hereda de la clase *Player* y representa a un jugador humano. Elige una posición libre y la introduce mediante teclado .

#### Métodos
1. Método Constructor. Llama al constructor de la clase base e inicializa la instancia del jugador humano.
2. *get_move(self, game)*. Método que solicita al usuario introducir una posición válida en el tablero.
En este caso, el código comprueba que las posiciones introducidas sean válidas. En caso contrario, solicita al usuario que introduzca una posición correcta.
