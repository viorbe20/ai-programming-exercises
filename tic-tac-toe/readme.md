# Tic-Tac-Toe

## Índice
[1. Introducción el juego](#1-introducción-al-juego)
[2. Clase *Player*](#2-clase-player)
[3. Clase *RandomComputerPlayer*](#3-clase-randomcomputerplayer)
[4. Clase *HumanPlayer*](#4-clase-humanplayer)
[5. Clase *TicTacToe*](#5-clase-tictactoe)
[6. Función *Play*](#6-función-play)

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

[Índice](#índice)

### 5. Clase *TicTacToe*
La clase TicTacToe representa el juego y tiene métodos para realizar movimientos, verificar ganadores y mostrar el tablero.

1. Método Constructor. Inicializa la instancia del juego con un tablero de 3x3 y establece la variable *current_winner* en None.
2. *print_board(self)*. Imprime el estado actual del tablero en formato visual.
3. *print_board_nums()*.Imprime el tablero con números para ayudar a los jugadores a seleccionar una casilla.
4. *available_moves(self)*. Devuelve una lista con los índices de casillas disponibles en el tablero.
5. *empty_squares(self)*. Verifica si hay casillas vacías en el tablero y devolviendo *True* o *False* dependiendo del caso.
6. *num_empty_squares(self)*. Devuelve el número exacto de casillas vacías en el tablero.
7. *make_move(self, square, letter)*. Realiza un movimiento válido asignando una casilla al jugador correspondiente (X o O). Devuelve *True* si el movimiento es válido y *False* si no lo es.
8. *winner(self, square, letter)*. Verifica si el último movimiento hecho es un movimiento ganador, comporbando todas las posibilidades de 3 en línea en filas, columnas y diagonales.

[Índice](#índice)

### 6. Función *play*
La función play toma una instancia de TicTacToe y dos jugadores como argumentos y ejecuta el juego hasta que hay un ganador o un empate.