from game.characters import Player
from game.actions import attack, defend

def game_loop():
    p1 = Player(input("Name Player 1: "))
    p2 = Player(input("Name Player 2: "))
    print(p1)
    print(p2)

    turn = 0
    while p1.is_alive() and p2.is_alive():
        attacker, defender = (p1, p2) if turn == 0 else (p2, p1)

        print(f"\n{attacker.name}'s turn!")
        print("1. Attack  2. Defend")
        choice = input("Choose: ")

        if choice == "1":
            damage = attack(attacker, defender)
            print(f"{attacker.name} attacks {defender.name} for {damage} damage")
        elif choice == "2":
            defend(attacker)
            print(f"{attacker.name} is defending!")
        else:
            print("Invalid move. Turn skipped.")

        turn = 1 - turn

    print("Game Over!")
    winner = p1 if p1.is_alive() else p2
    print(f"{winner.name} wins!")

def main():
    game_loop()

if __name__ == "__main__":
    main()