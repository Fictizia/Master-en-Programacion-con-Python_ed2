from random    import randint
from mascotas  import mascota1, mascota2, mascota3, mascota4, mascota5
from maquina   import maquina

mascotas = [mascota1, mascota2, mascota3, mascota4, mascota5]

def imprimir_mascotas():
    print(" ====================== MASCOTAS DISPONIBLES  ===================== ")
    print("                                                                    ")
    for index, mascota in enumerate(mascotas):
        print(f'{index} .-> {mascota}')
        print("                                                                    ")
    print(" ================================================================== ")
    print("                                                                    ")

def seleccionar_mascota():
    indice_seleccion = int(input(" Introduce el número de la mascota: "))
    mascota = mascotas[indice_seleccion]
    return mascota

def imprimir_maquina():
    print("                                                                ")
    print(" =========================== MÁQUINA ========================== ")
    print("                                                                ")
    print(f'{maquina}')
    print("                                                                ")
    print(" ============================================================== ")
    print("                                                                ")

def ataque_mascota(mascota):
    vida_quitada = (mascota.ataque + randint(1, 5)) - (maquina.defensa + randint(1, 5))
    maquina.vida = maquina.vida - vida_quitada
    return maquina.vida

def defensa_maquina(mascota):
    maquina.defensa = (mascota.defensa + randint(1, 5)) - (maquina.ataque + randint(1, 5))
    mascota.vida = mascota.vida - maquina.defensa
    return mascota.vida

def comprobar_vida_mascota(vida_mascota):
    if vida_mascota > 0:
        return True
    #
    print("                                         ")
    print(" +++++++++++++++++++++++++++++++++++++++ ")
    print(f'   ** HAS PERDIDO - Vida mascota: {vida_mascota}')
    print(" +++++++++++++++++++++++++++++++++++++++ ")
    print("                                         ")
    return False

def comprobar_vida_maquina(vida_maquina):
    if vida_maquina > 0:
        return True
    #
    print("                                         ")
    print(" +++++++++++++++++++++++++++++++++++++++ ")
    print(f'   ** HAS GANADO ** - Vida máquina: {vida_maquina}')
    print(" +++++++++++++++++++++++++++++++++++++++ ")
    print("                                         ")
    return False


def main():

    maquina.vida = ataque_mascota(mascota)

    mascota.vida = defensa_maquina(mascota)

    print("                                                                                                          ")
    print(" -------------------------------------------------------------------------------------------------------- ")
    print(f' MASCOTA: {mascota.nombre.upper()} / Ataque: {mascota.ataque} / Defensa: {mascota.defensa} / Vida: {mascota.vida} ')
    print(f' MÁQUINA:  Ataque: {maquina.ataque} / Defensa: {maquina.defensa} / Vida: {maquina.vida} ')
    print(" -------------------------------------------------------------------------------------------------------- ")
    print("                                                                                                          ")

    if not comprobar_vida_mascota(mascota.vida):
        return

    if not comprobar_vida_maquina(maquina.vida):
        return

    sigue_jugando = input(' ¿Atacas de nuevo?:  (S/N)' )
    if sigue_jugando.upper() == 'S':
        main()

# ================================================

imprimir_maquina()
imprimir_mascotas()

mascota = seleccionar_mascota()

main()

