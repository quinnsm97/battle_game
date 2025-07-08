from game.characters import Player
from game.actions import attack, defend, special_attack
from game.utils import prompt_action
from rich.console import Console
from rich import print

console = Console()

def game_loop():
    p1 = Player(input("Name Player 1: "))
    p2 = Player(input("Name Player 2: "))
    print(p1)
    print(p2)

    turn = 0
    while p1.is_alive() and p2.is_alive():
        attacker, defender = (p1, p2) if turn == 0 else (p2, p1)

        attacker.defending = False
        print(f"\n[bold cyan]{attacker.name}'s turn![/bold cyan]")

        choice = prompt_action()
        while choice not in ("1", "2", "3"):
            print("[red]Invalid move. Choose 1, 2, or 3.[/red]")
            choice = prompt_action()

        if choice == "1":
            damage = attack(attacker, defender)
            console.print(f"[bold green]{attacker.name}[/bold green] attacks [bold red]{defender.name}[/bold red] for [bold]{damage}[/bold] damage")
            defender.defense = 5
            defender.defending = False

        elif choice == "2":
            attacker.defending = True
            defend(attacker)
            print(f"[italic]{attacker.name} is defending![/italic]")

        elif choice == "3":
            damage = special_attack(attacker, defender)
            defender.defense = 5
            defender.defending = False

        

        # Display health stats
        console.print(f"\n[bold yellow]Status Update:[/bold yellow]")
        console.print(f"{p1.name}: [green]{p1.health} HP[/green]")
        console.print(f"{p2.name}: [green]{p2.health} HP[/green]\n")

        turn = 1 - turn

    print("\n[bold magenta]Game Over![/bold magenta]")
    winner = p1 if p1.is_alive() else p2
    print(f"[bold underline green]{winner.name} wins![/bold underline green]")

def main():
    while True:
        game_loop()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("[bold blue]Thanks for playing![/bold blue]")
            break

if __name__ == "__main__":
    main()