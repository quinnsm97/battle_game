from game.characters import Player
from game.actions import attack, defend
from rich import print

def game_loop():
    p1 = Player(input("Name Player 1: "))
    p2 = Player(input("Name Player 2: "))
    print(p1)
    print(p2)

    turn = 0
    while p1.is_alive() and p2.is_alive():
        attacker, defender = (p1, p2) if turn == 0 else (p2, p1)

        print(f"\n[bold cyan]{attacker.name}'s turn![/bold cyan]")
        print("[yellow]1. Attack  2. Defend[/yellow]")
        choice = input("Choose: ")

        if choice == "1":
            damage = attack(attacker, defender)
            print(f"[bold green]{attacker.name}[/bold green] attacks [bold red]{defender.name}[/bold red] for [bold]{damage}[/bold] damage")
        elif choice == "2":
            defend(attacker)
            print(f"[italic][green]{attacker.name}[/green] is defending![/italic]")
        else:
            print("[red]Invalid move. Turn skipped.[/red]")

        p1.defense = 5
        p2.defense = 5

        turn = 1 - turn

    print("\n[bold magenta]Game Over![/bold magenta]")
    winner = p1 if p1.is_alive() else p2
    print(f"[bold underline green]{winner.name} wins![/bold underline green]")

def main():
    game_loop()

if __name__ == "__main__":
    main()