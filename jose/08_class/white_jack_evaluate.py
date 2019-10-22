def evaluate_score(player, bank):
    # if banca or player == 21, wins, and break
    # if banca > 21, and player <= 21 player wins
    # if player > 21, and bank <= 21 bank wins
    # if both of them < 21
      # player - bank < 0 bank wins else player wins
      
    
    if bank > 21 and player < 21:
        return player
    if bank <21 and player > 21:
        return bank
    
    if bank < 21 and player < 21:
        difference = player - bank
        if difference >= 0:
            return bank
        else:
            return player

def evaluate_black_jack(player, bank):
    if bank == 21:
        return bank
    if player == 21:
        return player

