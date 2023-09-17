import random
import os
from art import logo


def Blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    user_score = 0
    comp_cards = []
    comp_score = 0
    gap = 0

    user_lost = False
    comp_lost = False
    both_lost = False

    def DrawCard():
        rand = random.choice(cards)
        return rand

    def CheckLoser():
        nonlocal user_lost, comp_lost, both_lost, comp_score, user_score, gap

        if (not comp_lost) and (not user_lost) and (not both_lost):
            if user_score > 21 and comp_score > 21:
                both_lost = True
            elif user_score > 21:
                user_lost = True
            elif comp_score > 21:
                comp_lost = True

        elif user_score == 21 or comp_score == 21:
            gap = (user_score - 21) - (comp_score - 21)
            if gap == 0:
                both_lost = True
            elif gap < 0:
                comp_lost = True
            elif gap > 0:
                user_lost = True

    def CheckWinner():
        nonlocal user_lost, comp_lost, both_lost, comp_score, user_score, gap
        comp_score = 0
        if comp_score < 17:
            comp_cards.append(DrawCard())
            for int in comp_cards:
                comp_score += int
        gap = (user_score - 21) - (comp_score - 21)
        if comp_score > 21:
            comp_lost = True
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("Computer went over. YOU WON 👑")

        elif gap == 0:
            both_lost = True
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("Its a draw")
        elif gap > 0:
            comp_lost = True
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("YOU WON 👑👑👑")
        elif gap < 0:
            user_lost = True
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("YOU LOSE 👎👎👎")

    def HitMe():
        nonlocal user_score, comp_score, user_lost, comp_lost, both_lost
        user_score = 0
        comp_score = 0
        user_cards.append(DrawCard())
        for int in comp_cards:
            comp_score += int
        if comp_score < 17:
            comp_cards.append(DrawCard())
        comp_score = 0

        for int in user_cards:
            user_score += int
        for int in comp_cards:
            comp_score += int
        print(f"{user_cards}, current score : {user_score}")
        print(f"Computer's First Card: {comp_cards[0]}")
        CheckLoser()
        if user_lost:
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("You went over. You lose 😭")
        elif comp_lost:
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("Computer went over. YOU WON 👑")
        elif both_lost:
            print(f"Your Final Hand {user_cards}, final score: {user_score}")
            print(
                f"Computer's Final Hand {comp_cards}, final score: {comp_score}"
            )
            print("You both lost. Better luck next time.")

    print(logo)

    user_cards.append(DrawCard())
    user_cards.append(DrawCard())
    comp_cards.append(DrawCard())
    comp_cards.append(DrawCard())

    for int in user_cards:
        user_score += int
    for int in comp_cards:
        comp_score += int

    print(f"{user_cards}, current score = {user_score}")
    print(f"Computer's First Card: {comp_cards[0]}")

    while (not user_lost) and (not comp_lost) and (not both_lost):
        hit = str(input("Type 'y' to get another card, type 'n' to pass: "))
        if hit == "y":
            HitMe()
        elif hit == "n":
            CheckLoser()
            CheckWinner()


Blackjack()
