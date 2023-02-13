from random import random,randint
l = ['rock','paper','scissor']
score_player = 0
score_computer = 0
computer = randint(1,3)
while True:
    player = input()
    if score_computer <= 5 and score_player <= 5:
        if computer == 1:
            if player == 'paper':
                score_player=score_player+1
            else:
                score_computer=score_computer+1
        elif computer == 2:
            if player == 'scissor':
                score_player = score_player + 1
            else:
                score_computer = score_computer + 1
        elif computer == 3:
            if player == 'rock':
                score_player = score_player+1
            else:
                score_computer = score_computer+1
        else:
            score_computer = score_computer
            score_player = score_player
    print(score_player)
    print(score_computer)



