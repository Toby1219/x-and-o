from .easy import ComputerAi_Easy
from .medium import ComputerAiMedium
from .hard import ComputerAiSmart
from .player import Player

from rich import print

class GameBuild(Player, ComputerAi_Easy, 
                ComputerAiMedium, ComputerAiSmart):
    def __init__(self) -> None:
        super().__init__()
        self.ai = ''
        self.valid_mode = {'easy', 'e', 'medium', 'm', 'hard', 'h'}
        self.valid_gametype = ('a vs a', 'a v a', 'p vs a', 'p v a', 'p vs p', 
                               'p v p')
        self.main_build()

    def select_mode(self):
        """ To select which kind of ai you want easy, meduim hard """
        while True:
            mode = str(input('Select Mode (easy, meduim, hard): '))
            self.msg = 'Select from (easy, meduim, hard) or (e, m, h)'
            try:
                self.validator(value=mode, item=self.valid_mode, character=True)
                break
            except ValueError as e:
                print(f'[bold red]{e}[/bold red]')
        if mode == 'easy' or mode == 'e':
            self.ai = self.computer_player
        elif mode == 'meduim' or mode == 'm':
            self.ai = self.computer_player_mid
        elif mode == 'hard' or mode == 'h':
            self.ai = self.computer_player_had
        
    def main_build(self, not_replay=True):
        """ Runs the Game """  
        self.select_mode()      
        if not_replay:
            self.player(user_char=True, user_position=False)      
        self.go_first()

        while True:
            result, message, winer = self.check_wins()
        
            self.winer = winer
            if result == 'win':
                if winer == 'X':
                    self.winer = winer
                    self.player_X += 1
                elif winer == 'O':
                    self.winer = winer
                    self.player_O += 1
                print(f'\n\n [bold blue]{message} [/bold blue] \n\n Player X = [bold blue]{self.player_X}[/bold blue] \n Player O = [bold blue]{self.player_O}[/bold blue]')
                break
            elif result == 'tie':
                print(f'\n\n [bold blue]{message}[/bold blue] \n\n')
                break
            else:   
                self.player()
                self.ai()
                for line in self.draw_board():
                    print(line)
                
        self.replay()




    