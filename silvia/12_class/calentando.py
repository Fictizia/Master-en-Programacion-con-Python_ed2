# Pasada una lista numérica de 10 elementos random, ordenar los números de mayor a menor

import random

list_to_sort = list()

def create_list():
    for _ in range (10):
        list_to_sort.append(random.randrange(1, 101))

def sort_list(list):
    list_to_sort.sort()
    list_to_sort.reverse()
    return list_to_sort

def main():
    create_list()
    print(f'Lista para ordenar: {list_to_sort}')
    sort_list(list_to_sort)
    print(f'Lista ordenada: {list_to_sort}')

main()




