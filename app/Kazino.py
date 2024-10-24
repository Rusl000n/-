from random import randint
import emoji

def kazzzino(zakkk):
    k = [0, 0, 0]
    i = 0
    while i !=3:
        zak = int(randint(1,4))
        k[i] = zak
        if zak == 1:
            zak = '🍎'
        elif zak == 2:
            zak = '💎'
        elif zak == 3:
            zak = '🇷🇺'
        else:
            zak = '🚽'
        zakkk += '   ' + zak
        i += 1
    if len(set(k)) == 1:
        return (zakkk + '\n Ура, ура, это победа!!!🥳🥳🥳')
    else:
        return (zakkk + '\n О нет, попробуй еще раз😬')

