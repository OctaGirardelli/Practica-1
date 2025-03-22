import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

puntaje = 0

#Se eligen al azar 3 preguntas(en tuplas)
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question in questions_to_ask:

    # Se muestra la pregunta y las respuestas posibles
    print(question[0])
    for i, answer in enumerate(question[1]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Se verifica si la respuesta es un número entero positivo
        if not user_answer.isdigit():
            print("Respuesta no válida")
            sys.exit(1)
        
        user_answer = int(user_answer) - 1

        # Se verifica si es un numero de respuesta válido
        if not(0 <= user_answer < len(question[1])):  #Con esta condicion pueden añadirse preguntas de mas o menos que 4 respuestas
            print("Respuesta no válida")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == question[2]:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
            puntaje -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(question[1][question[2]])

    # Se imprime un blanco al final de la pregunta
    print()

print(f"Fin del juego, tu puntaje fue: {0 if puntaje < 0 else puntaje}")  #No se permiten puntajes negativos