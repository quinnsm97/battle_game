from game.characters import Player

def game_loop():
    p1 = Player(input("Name Player 1: "))
    p2 = Player(input("Name Player 2: "))
    print(p1)
    print(p2)

def main():
    game_loop()

if __name__ == "__main__":
    main()