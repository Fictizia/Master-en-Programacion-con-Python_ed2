#Problema:
    
    #----------------/// LOGICA JUGADOR ////-----------------
    #Tenemos a un jugador que aleatoriamente se le generan 5 pokemons con sus diferentes nombres, ataques, defenesas y vidas. ✅
    #Cada mascota tiene sus propias habilidades (Caracteristicas). ✅ 
    #El jugador puede elegir al pokemon que quiera para combatir ✅

    #--------------/// LOGICA CPU ////------------------
    # Generara un pokemon aleatorio con sus diferentes caracteristicas
    # Cada vez generara un pokemon aleatorio distinto. (Gane o pierda)

    #-------------/// LOGICA DEL JUEGO ///--------------------
    # Los combates son por turnos, es decir, una vez ataca uno hace todos los calculos necesarios y ataque el otro
        # .- Posibles problemas derivados {
            #¿Que pasa si de un ataque muere el adversario ( podremos crear un Except que si ocurre eso salga directamente.)
            
        #}
    # Este ciclo de cambios solo terminara una vez uno de los dos pokemon hayan perdido. Si el pokemon del jugador pierde lo pierde.

    # Ejercicio para nota, guardar los datos en JSON ( para esto necesitamos checkear si existe uno y si exsite uno utilizar esos mismos datos.)


import random

def pokemons():
    bulbasur =  {'nombre': 'Bulbasur', 'ataque': 10, 'defensa': 5, 'vida': 15}
    charmander = {'nombre': 'Charmander', 'ataque': 19, 'defensa': 2, 'vida': 15}
    squirtle = {'nombre': 'Squirtle', 'ataque': 5, 'defensa': 19, 'vida': 15} 
    charizard = {'nombre': 'Charizard', 'ataque': 20, 'defensa': 25, 'vida': 15} 
    venasur = {'nombre': 'Venasur', 'ataque': 30, 'defensa': 25, 'vida': 15} 
    dragonite = {'nombre': 'Dragonite', 'ataque': 50, 'defensa': 30, 'vida': 15} 
    pikachu = {'nombre': 'Pikachu', 'ataque': 12, 'defensa': 8, 'vida': 15} 

    items = [bulbasur, charmander, squirtle, charizard, venasur, dragonite, pikachu]
    pokemons = random.sample(items, 5)
   
    #1.- Debemos tener la capacidad de generar 5 pokemon aleatorios y asignarlos. (Esto lo podemos hacer con clases o con un diccionario.)
    def pokemon_aleatorios_jugador(pokemons):
        # print(pokemons)
        print('Te han tocado : ----> ' + pokemons[0].get('nombre'), 'Ataque: ' + str(pokemons[0].get('ataque')), 'Defensa: ' +  str(pokemons[0].get('defensa')), 'Vida: ' + str(pokemons[0].get('vida')))
        print('Te han tocado : ----> ' + pokemons[1].get('nombre'), 'Ataque: ' + str(pokemons[1].get('ataque')), 'Defensa: ' +  str(pokemons[1].get('defensa')), 'Vida: ' + str(pokemons[1].get('vida')))
        print('Te han tocado : ----> ' + pokemons[2].get('nombre'), 'Ataque: ' + str(pokemons[2].get('ataque')), 'Defensa: ' +  str(pokemons[2].get('defensa')), 'Vida: ' + str(pokemons[2].get('vida')))
        print('Te han tocado : ----> ' + pokemons[3].get('nombre'), 'Ataque: ' + str(pokemons[3].get('ataque')), 'Defensa: ' +  str(pokemons[3].get('defensa')), 'Vida: ' + str(pokemons[3].get('vida')))
        print('Te han tocado : ----> ' + pokemons[4].get('nombre'), 'Ataque: ' + str(pokemons[4].get('ataque')), 'Defensa: ' +  str(pokemons[4].get('defensa')), 'Vida: ' + str(pokemons[4].get('vida')))

    pokemon_aleatorios_jugador(pokemons)
    
    def elegir(pokemon_aleatorios_jugador):
        pokemon1 = pokemons[0]
        pokemon2 = pokemons[1]
        pokemon3 = pokemons[2]
        pokemon4 = pokemons[3]
        pokemon5 = pokemons[4]

        eleccion1 = pokemon1.get('nombre')
        eleccion2 = pokemon2.get('nombre')
        eleccion3 = pokemon3.get('nombre')
        eleccion4 = pokemon4.get('nombre')
        eleccion5 = pokemon5.get('nombre')
        
        elegir_pokemon = [eleccion1, eleccion2, eleccion3, eleccion4, eleccion5]
        seleccionar_tu_pokemon = input("Elige a tu pokemon: ")         

        # elegir_pokemon = pokemon1.get('nombre') or  or pokemon3.get('nombre') or pokemon4.get('nombre') or pokemon5.get('nombre')
        if seleccionar_tu_pokemon == seleccionar_tu_pokemon in elegir_pokemon:
            print('QUE EMPIEZE EL COMBATE')
        else:
            print('No tienes a ese Pokemon')
            elegir(pokemon_aleatorios_jugador)
        # Problema le puedes pasar lo que te de la gana 

    elegir(pokemon_aleatorios_jugador)
    elegir = pokemon_aleatorios_jugador

    def pokemon_aleatorio_cpu(pokemons):
        print('Te enfrentas a : ----> ' + pokemons[0].get('nombre'), 'Ataque: ' + str(pokemons[0].get('ataque')), 'Defensa: ' +  str(pokemons[0].get('defensa')), 'Vida: ' + str(pokemons[0].get('vida')))
    
    pokemon_aleatorio_cpu(pokemons)
    
    #  def combate(elegir, pokemon_aleatorio_cpu):
        # pokemon_aleatorio_cpu
        
        
        # Ataca simpre primero cpu
        # ataque cpu = Numerorandom +ataque pokemon_cpu - (defensa_pokemon_elegido)
        # Si n+atp > dpcpu
            # atp - vidacpu
        # Else:
            # continue
        # ataque pokemon_elegido = Numerorandom +ataque pokemon_cpu - (defensa_pokemon_elegido)
        # Si n+atp > dpcpu
            # atp - vidacpu
        # Else:
            # continue
        
            

    # elegir_pokemon = input('Que pokemon quieres elegir: ')


        #print('producto')
        # Con esto hemos he dicho que por cada pokemon que se encuentre en un diccionario  ( que podemos importar lo muestre, bien vamos a probrarlo.)
pokemons()