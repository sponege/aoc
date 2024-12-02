score = 0
score2 = 0

def round(o, p): # opponent, player
    # opponent move:
    # A - Rock
    # B - Paper
    # C - Scissors
    # player move:
    # X - Rock
    # Y - Paper
    # Z - Scissors
    global score
    o = ord(o) - ord('A')
    p = ord(p) - ord('X')
    # print(o, p)
    score += p + 1 # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    if p == (o + 1) % 3: # win
        # print("Won!")
        score += 6
    elif o == p: # tie
        # print("Tie!")
        score += 3
    else: # loss
        # print("Lost!")
        return
    # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

def actual_round(o, p): # opponent, player
    # opponent move:
    # A - Rock
    # B - Paper
    # C - Scissors
    # player move:
    # X - I need to lose
    # Y - I need to tie
    # Z - I need to win
    global score2
    o = ord(o) - ord('A')
    p = ord(p) - ord('X')
    # print(o, p)
    if p == 0: # I need to lose
        choice = (o - 1) % 3
    elif p == 1: # I need to tie
        choice = o
    elif p == 2: # I need to win
        choice = (o + 1) % 3
    #print(o, p, choice)

    score2 += choice + 1 + p * 3
    print(choice + 1, "+", p * 3, "=", choice + 1 + p * 3)
    #print("Score:", score2)


while True:
    try:
        o, p = [i for i in input().split()] # opponent, player
    except EOFError:
        break
    round(o, p)
    actual_round(o, p)

# Part 1:
print(score)

# Part 2:
print(score2)
