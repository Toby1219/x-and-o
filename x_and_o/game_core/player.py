from .functions import GameFunctions
from rich import print


class Player(GameFunctions):
    def __init__(self) -> None:
        super().__init__()
    

    def player(self, user_char: bool=False, user_position: bool=True):
        """
        To select wether player is "X" and cmputer is "O" or the other way round
        and to enter a valid position integer only
        """
        if user_char:
            while True:
                self.char = str(input("\nEnter X or O: ")).upper()
                self.msg = "\n[bold red]Error: [/bold red][bold yellow]you are to only enter alphabet X and O [/bold yellow]"
                try:
                    self.validator(value=self.char, item=self.valid_str, character=True)
                    break
                except ValueError as e:
                    print(f"{e}")

        if user_position:
            while True:                
                try:
                    self.pos = int(input('\nEnter number 1-9: '))
                    self.msg = f'{self.pos} has been taken chose another position'
                    try:
                        self.validator(value=self.char, position=self.pos, positions=True)
                        break
                    except ValueError as e:
                        print(f"\n [bold red]{e}[/bold red]")
                        continue
                except:
                    print(f"[bold red]Invalid Number[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")

    def playerPvP_one(self, user_position: bool=True):
            """
            Player is "X" and enter a valid position integer only
            Use in player vs player game
            """
            self.char = 'X'

            if user_position:
                while True:                
                    try:
                        self.pos = int(input('\nEnter number 1-9: '))
                        self.msg = f'{self.pos} has been taken chose another position'
                        try:
                            self.validator(value=self.char, position=self.pos, positions=True)
                            break
                        except ValueError as e:
                            print(f"\n [bold red]{e}[/bold red]")
                            continue
                    except:
                        print(f"[bold red]Invalid Number[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")

    def playerPvP_two(self, user_position: bool=True):
            """
            Player is "O" and enter a valid position integer only
            Use in player vs player game
            """
            self.char = 'O'

            if user_position:
                while True:                
                    try:
                        self.pos = int(input('\nEnter number 1-9: '))
                        self.msg = f'{self.pos} has been taken chose another position'
                        try:
                            self.validator(value=self.char, position=self.pos, positions=True)
                            break
                        except ValueError as e:
                            print(f"\n [bold red]{e}[/bold red]")
                            continue
                    except:
                        print(f"[bold red]Invalid Number[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")

