# Practica de Q-Learning - Juego del Gato

## Objetivo
Crear un agente para el juego del gato (3x3) utilizando aprendizaje por refuerzo mediante el algoritmo Q-Learning.  
El agente debe aprender a jugar mejor conforme se repiten las partidas.

---

## Archivos del proyecto

- `gato.py`  
  Contiene la clase del juego del gato. Aqui se maneja el tablero, los turnos, la validacion de jugadas y la deteccion del ganador.

- `qlearning.py`  
  Implementa la tabla Q y la logica del algoritmo Q-Learning. Se encarga de guardar y actualizar las recompensas.

- `agent.py`  
  Define el agente que aprende a jugar. Controla la exploracion, explotacion y el aprendizaje del agente.

- `main.py`  
  Archivo principal que ejecuta el juego en consola y conecta el juego con el agente.

- `README.md`  
  Archivo de documentacion donde se explica el objetivo, reglas y funcionamiento del proyecto.


## Reglas del Juego

- El tablero es una matriz de 3x3
- El juego es por turnos
- Participan dos jugadores
- Cada jugador elige una posicion dentro del tablero
- Si la posicion ya esta ocupada, se debe elegir otra
- El juego termina cuando:
  - Un jugador completa 3 espacios consecutivos en forma horizontal o vertical
  - Ya no existen espacios disponibles (empate)

---

## Representacion del Juego

- Se usa el valor **1** para el primer jugador
- Se usa el valor **-1** para el segundo jugador
- El tablero se inicializa con ceros (0)

---

## Clase Gato

El archivo del juego contiene la clase `Gato`, la cual implementa la logica principal del juego.

### Metodos implementados

- `__init__`  
  Inicializa el tablero 3x3 y define al jugador inicial.

- `get_winner`  
  Verifica si algun jugador gano revisando primero filas y despues columnas.

- `get_state`  
  Regresa el estado actual del tablero en forma de cadena.

- `get_valid_actions`  
  Devuelve una lista con todas las coordenadas disponibles del tablero.

- `is_ended`  
  Indica si el juego termino por victoria o por empate.

- `_print`  
  Imprime el tablero en consola.

- `play(x, y)`  
  Coloca la jugada del jugador actual en la posicion indicada y cambia el turno.
  Si hay ganador, regresa el jugador ganador, de lo contrario regresa `None`.

La estructura del juego consiste en llamar repetidamente a `play` dentro de un ciclo hasta que el juego termine.

---

## Aprendizaje con Q-Learning

Para el aprendizaje se utiliza una tabla Q que almacena estimaciones de recompensa para cada par:

Donde:
- `state` es el estado actual del tablero
- `action` es la posicion seleccionada
- El valor almacenado es la recompensa estimada

---
## Conclusiones

En esta practica se implemento un agente basado en Q-Learning capaz de aprender a jugar el juego del gato.  
El agente mejora su desempeno conforme juega mas partidas, explorando al inicio y explotando el conocimiento adquirido con el tiempo.

