# ROCK, SCISSORS AND PAPERS GAME
import random
choices = ['rock','paper','scissor']
cpu = random.choice(choices)
player = False
p_score = 0
c_score = 0
while True:
    player = input('rock or paper or scissor : ').upper()

    if player == cpu:
        print ("it's a tie".upper())
    elif player == 'rock':
        if cpu == "paper":
            print(f'you lose {cpu} covers {player}'.title())
            c_score += 1
        else:
            print(f"you win! {player} smashes {cpu}".title())
            p_score += 1


    elif player == 'paper':
        if cpu == 'scissor':
            print(f'you lose {cpu} cuts {player}'.title())
            c_score += 1
        else:
            print(f"you win! {player} covers {cpu}".title())
            p_score += 1


    elif player == 'scissor':
        if cpu == 'rock':
            print(f'you lose {cpu} smashes {player}'.title())
            c_score += 1
        else:
            print(f"you win! {player} cuts {cpu}".title())
            p_score += 1


    elif player =="End" or player == "end" or player == "e" or player == "E":
        print(f'final scores\ncpu scored {c_score}\nplayer scored {p_score}')

    

    