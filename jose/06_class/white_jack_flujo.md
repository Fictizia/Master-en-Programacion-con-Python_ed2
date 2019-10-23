- Tenemos una baraja, con 4 palos, del 1 al 10 y J, Q, K
- Las cartas valen el número que tengan, los A == 1, J,Q,K == 10.
- Por lo tanto tenemos cuatro 1, cuatro 2..... hasta 9, y dieciséis 10s

- Comienza el juego:
    - Se reparte una carta al usuario. (nota, quitar la carta de la baraja) (se muestra puntuación)
    - Se reparte una carta a la banca. (nota, quitar la carta de la baraja)

- *Se pregunta al usuario si quiere otra carta.
    - Sí -> Se reparte una carta al usuario. (nota, quitar la carta de la baraja) (se muestra puntuación)
    - No -> Se planta y se queda con la puntuación que tenga

    Turno Banca:
    - Si tiene menos de 15 en su puntuación, recibe una carta, (se quita del mazo)
    - Si tiene 15 o más, se planta.

    TURNO AMBOS:
    - Si alguno se pasa de 21, se le da la victoria al otro
    - Si alguno llega JUSTO a 21, gana AUTOMATICAMENTE (EL OTRO NO INTERACTUA).

- Si ambos se plantan el mas cercano a 21 SIN PASARSE, gana.
- Si ambos tienen la misma puntuación gana la banca.

- Se pregunta al usuario si quiere otra carta.... (Volver al punto con *)


