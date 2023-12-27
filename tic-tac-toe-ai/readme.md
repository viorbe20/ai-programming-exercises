# Tic-Tac-Toe-AI

Este proyecto es una recreación del juego Tic Tac Toe basado en un tutorial de YouTube. 

## Créditos
  - Canal: [freeCodeCamp.org](enlace_al_video)
  - Creadora: Kylie Ying
  - Enlace al video: [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&t=14s)

## Índice 
[1. Objetivo](#1-objetivo)

### 1. Objetivo
El objetivo de este ejercicio es crear un juego de Tic-Tac-Toe donde la máquina nunca pierde. Para esto se utilizará el algoritmo *Minimax*, el cual representa una decisión construida sobre la idea de maximizar las posibilidades de que la máquina gane y minimizar las posibilidades de que el oponente pierda en cada uno de los pasos del juego. 

En cada jugada se intentarán recrear todos los movimientos decidiendo así cuál es el más óptimo para nuestro cometido. Mediante la *utility function* estimaremos los resultados cuando la partida finalice ya sea porque alguno gane o por empate.

Esta función se compone de:

> **Utility Function**
>> elemento1 * elemento2 = resultado
> - elemento1
>      - 0: en caso de empate
>      - 1: gana X
>      - -1: gana O 
> - elemento2: número de casillas vacías más 1

![Utility function](./img/utility-function.png)

El valor 3 será el valor buscado para maximizar X.






