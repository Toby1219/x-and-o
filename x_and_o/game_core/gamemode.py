from .easy import ComputerAi_Easy
from .medium import ComputerAiMedium
from .hard import ComputerAiSmart
from .player import Player
import time
from rich import print

class GameBuild(Player, ComputerAi_Easy, 
                ComputerAiMedium, ComputerAiSmart):
    def __init__(self) -> None:
        super().__init__()

        self.main_build()
        
    def main_build__player(self, not_replay=True):
        """ Runs the game type p vs ai """
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
                print()
                for line in self.draw_board():
                    print(line)
                print()

                self.player_two()
                print()
                for line in self.draw_board():
                    print(line)
                print()

        
    def main_build_comp(self):
        """ Runs game type ai vs ai or p vs p """
        self.comp_char = ''
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
                self.player_one()
                
                print()
                for line in self.draw_board():
                    print(line)
                print()
                
                time.sleep(self.time)
                self.player_two()
                
                print()
                for line in self.draw_board():
                    print(line)
                print()

    def main_build(self):
        """ Runs entire Game """
        self.select_mode()
        returned = self.game_type()
        cou = 0
        while True:
            if returned == 0:
                self.cleaner()
                self.main_build__player()
                self.replay(self.main_build__player, not_replay=False)
            elif returned == 1:
                self.main_build_comp()
                self.replay(self.main_build_comp)
            cou += 1

            _continue = str(input('Whould You like to continue current game: ')).lower()

            if cou == 5 or _continue in ['no', 'n']:
                break
            else:
                continue

        que = str(input('would you like to restart the entire Game: ')).lower()
        if que in ['yes', 'y']:
            self.cleaner()
            self.main_build()
        




    