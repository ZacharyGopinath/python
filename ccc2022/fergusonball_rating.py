# finished question

#score = +5
#foul = -3
#if all players 40 points, add "+" after rating


def rating():
    total = 0
    N = input()
    for i in range(int(N)):
        S = input()
        F = input()
        if ((int(S) * 5) - (int(F) * 3)) > 40:
            total = total + 1
    if int(N) == total:
        total = str(total) + "+"
    print(total)

rating()
