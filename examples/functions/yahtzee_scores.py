#!/usr/bin/env python3
def print_score(player, **scores):
    total_score = 0
    print("Player:", player)
    fmt = "{0:>15}: {1}"
    for category, score in scores.items():
        print(fmt.format(category, score))
        total_score += score
    print(fmt.format("Total", total_score))


print_score("Aiden", Aces=4, Twos=8, FullHouse=25, LgStraight=40)
print_score("Cindy", Twos=4, LgStraight=40, Chance=24, ThreeOfAKind=21)
