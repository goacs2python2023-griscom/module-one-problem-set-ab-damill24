import random
def roll_two():
    x = random.randint(1,6)
    y = random.randint(1,6)
    if x + y == 6 or x + y == 7 or x + y == 8:
        return "Win"
    else:
        return "Lose"
def main():
    print(roll_two())
main()