# Tic-Tac-Toe-AI

Este proyecto es una recreación del juego Tic Tac Toe basado en un tutorial de YouTube. 

## Créditos
  - Canal: [freeCodeCamp.org](enlace_al_video)
  - Creadora: Kylie Ying
  - Enlace al video: [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&t=14s)

## Índice 
[1. Introducción](#1-introducción)

### 1. Introducción
Este repositorio contiene una implementación de un juego Tic Tac Toe en Python, con la particularidad de que uno de sus jugadores es la máquina.

En este juego, el __algoritmo minimax__ será la clave para garantizar que la máquina nunca pierda en el juego, siempre ganando o empatando. El objetivo de este algoritmo es maximizar la victoria y minimizar la pérdida del oponente en cada movimiento.

Otro elemento fundamental será la __función de utilidad__, la cual mide la valía del resultado final en el árbol de decisiones del juego. Su objetivo es la optimización para ganar en la menor cantidad de pasos posibles. 

Se han implementado dos versiones: una por consola y otra con interfaz gráfica

### 2. Funciones Tic Tac Toe por consola

#### __init__()
En resumen, la función __init__ inicializa una instancia de la clase TicTacToe con un tablero vacío y sin un ganador inicial. 

#### print_board()
En cada iteración se crea una lista de sublistas, donde cada sublista representa una fila del tablero. Luego, el bucle for recorre cada fila y las imprime en el formato deseado.

#### print_board_nums()
Imprime un tablero inicial de 3x3 con números del 0 al 8.
Cada número representa una posición en el tablero, ofreciendo una referencia visual para los jugadores.

#### available_moves()
Devuelve una lista con los índices de aquellas casilla que están vacías




