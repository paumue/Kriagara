#weli mit krieg gewinnen fehlt --> fixed
#do data analysis, make graphs

from random import shuffle

def mix_cards():
    cards = [- 10,1,2,3,4,5,6,7,8]
    deck = cards * 4
    deck[0] = 10
    shuffle(deck)
    player1 = deck[0:int(len(deck)/2)]
    player2 = deck[18:len(deck)]
    return player1, player2



def play_game():
    players = mix_cards()
    i = 0
    counter = 0
    while len(players[0]) != 0 and len(players[1]) != 0:

        if abs(players[0][i]) == abs(players[1][i]):

            if len(players[0]) > 2 and len(players[1]) > 2:

                while len(players[0]) > i + 4 and len(players[1]) > i + 4 and players[0][i + 2] == players[1][i + 2]:
                    i += 2
                if players[0][i + 2] > players[1][i+2]:

                    i += 2
                    while i >= 0:
                        players[0].append(players[1][0 + i])
                        players[1].remove(players[1][0 + i])
                        i -= 1

                elif players[0][i +2] < players[1][i + 2]:
                    i += 2
                    while i >= 0:
                        players[1].append(players[0][0 + i])
                        players[0].remove(players[0][0 + i])

                        i -= 1
                else:
                    break

        elif players[0][i] > players[1][i]:
            players[0].append(players[1][i])
            players[1].remove(players[1][i])

        elif players[0][i] < players[1][i]:
            players[1].append(players[0][i])
            players[0].remove(players[0][i])

        else:
            return "Error"

        shuffle(players[0])
        shuffle(players[1])
        counter += 1
    return counter


list = []
for x in range(0,10000):

    list.append(play_game())

av = sum(list)/len(list)
max = max(list)
min = min(list)
print("Average: " + str(av) + " Max: " + str(max) + " Min: " + str(min))
