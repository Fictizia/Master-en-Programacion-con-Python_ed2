num = 1

def change_numn(num):
    num += 5
    return num

second_num = change_numn(num)
print(num) # chachi
print(second_num)

player = {'name': 'jose'}

def change_player(new_player):
    new_player['name'] = 'Alberto'

change_player(player)
print(player)
