import random
from rich import print


class GameAttributes:
    def __init__(self) -> None:
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
   
        self.map_get_position = {
                '0 0' : 1,
                '0 1' : 2,
                '0 2' : 3,
                '1 0' : 4, 
                '1 1' : 5,
                '1 2' : 6,
                '2 0' : 7,
                '2 1' : 8,
                '2 2' : 9
            }
        
        self.valid_str = {'X', 'O'}
        self.valid_ans = {'yes', 'y', 'no', 'n'}
        self.char: str = ''
        self.comp_char = ''
        self.pos: int = 0
        self.moves =[x for x in range(1, 10)]
        
        self.player_X = 0
        self.player_O = 0
        self.total_point = 0
        self.winer = ''

        #validators variables
        self.msg: str = ''
    
        
class GameFuctions(GameAttributes):
    def __init__(self) -> None:
        super().__init__()
               
    def draw_board(self):
        """ Draws Board"""
        line_through = '___'
        v = [line_through for _ in range(3)]
        count = 0
        for row in self.board:
            yield ' | '.join(row)
            
            if count != 2:
                st2 = ''.join(v)
                yield st2
            count += 1     

    def check_wins(self):
        """ Check for wins in Coloums, Rows and Vertical """
        board = self.board

        # Coloums wins
        if (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' '
            and board[0][0] == board[0][1] == board[0][2]):
                winer = board[0][0]
                print()
                return 'win', f'Winner is "{winer}", win at Coloumn 1', winer

        elif (board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' '
            and board[1][0] == board[1][1] == board[1][2]):
                winer = board[1][0]
                print()
                return 'win', f'Winner is "{winer}", win at Coloumn 2', winer

        elif (board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' '
            and board[2][0] == board[2][1] == board[2][2]):
                winer = board[2][0]
                print()
                return 'win', f'Winner is "{winer}", win at Coloumn 3', winer
        
        # Rows wins
        elif (board[0][0] != ' ' and board[1][0] != ' ' and board[2][0] != ' '
            and board[0][0] == board[1][0] == board[2][0]):
                winer = board[0][0]
                print()
                return 'win', f'Winner is "{winer}", win at Row 1', winer

        elif (board[0][1] != ' ' and board[1][1] != ' ' and board[2][1] != ' '
            and board[0][1] == board[1][1] == board[2][1]):
                winer = board[0][1]
                print()
                return 'win', f'Winner is "{winer}", win at Row 2', winer

        elif (board[0][2] != ' ' and board[1][2] != ' ' and board[2][2] != ' '
            and board[0][2] == board[1][2] == board[2][2]):
                winer = board[0][2]
                print()
                return 'win', f'Winner is "{winer}", win at Row 3', winer

        # vertical wins
        elif (board[0][0] != ' ' and board[1][1] != ' ' and board[2][2] != ' '
            and board[0][0] == board[1][1] == board[2][2]):
                winer = board[0][0]
                print()
                return 'win', f'Winner is "{winer}",  vertical win at the RIGHT', winer
        
        elif (board[0][2] != ' ' and board[1][1] != ' ' and board[2][0] != ' '
            and board[0][2] == board[1][1] == board[2][0]):
                winer = board[0][2]
                print()
                return 'win', f'Winner is "{winer}",  vertical win at the LEFT', winer
        
        elif self.fullBoard():
            return  'tie', '\n It\'s a tie game \n', None
             
        else:
            return 'No match', None, None
        
    def fullBoard(self):
        return all(row != ' ' for rows in self.board for row in rows)

    def calculate_score(self):
        """ Calculates scores or point """
        if self.player_X > self.player_O:
            self.total_point = self.player_X
            print(f'\n\n Highest Point = [bold green]{self.total_point}[/bold green] \n [bold green]{self.winer}[/bold green] wins this round :smile: \n\n Sad to see you go :cry: \n\n')       

        elif self.player_O > self.player_X:
            self.total_point = self.player_O
            print(f'\n\n Highest Point = [bold green] {self.total_point}[/bold green] \n [bold green]{self.winer}[/bold green] wins this round :smile: \n\n Sad to see you go :cry: \n\n')       

        elif self.player_O == self.player_X:
            self.total_point = f'"X": {self.player_X} "O": {self.player_O}'
            print(f'\n\n Tie Game [bold green]{self.total_point}[/bold green] \n\n Sad to see you go :cry: \n\n')       

    def cleanBoard(self):
        """ Reset Board """
        for i in range(len(self.board)):
            for y in range(len(self.board[i])):
                if self.board[i][y] == 'X' or self.board[i][y] == 'O':
                    self.board[i][y] = ' '
        return self.board    

    def reset_moves(self):
        """ Reset moves """
        self.moves = [x for x in range(1, 10)]
        return self.moves

    def replay(self):
        """ Restart game """
        while True:
            try:
                question = str(input('\nWould you like to replay: ')).lower().strip()
                self.msg = '\nYou are to enter "yes", "y", "no", "n"'
                self.validator(value=question, item=self.valid_ans)
                break
            except ValueError as e:
                print(f"\n [bold red] {e} [/bold red] \n")

        if question == 'yes' or question == 'y':
            print("\n\n [green] Restarting the game.... \n\n Cleaning the board..., Reseting computer moves... \n\n Done[/green] :smile::smile::smile: \n\n")
            
            self.cleanBoard()
            self.reset_moves()
			
            self.main(not_replay = False)
        else:
            self.calculate_score()

    def go_first(self):
        """ Player decide wether to go first or not"""
        while True:
            try:
                conf = str(input('\nWould you like to go first: ')).lower().strip()
                self.msg = 'You are to enter "yes", "y", "no", "n"'
                self.validator(value=conf, item=self.valid_ans)
                break
            except ValueError as e:
                print(e)

        if conf == 'yes' or conf == 'y':
            print('Scores: \n', self.player_X, '\n', self.player_O, '\n')
        elif conf == 'no' or conf == 'n':
            self.computer_player()
            for line in self.draw_board():
                print(line)
    
    def validator(self, value: str=None, position: int=None, item: set=None,
                           character: bool = True, positions: bool=False):
        """ 
        Validates Players inputs must be "X" OR "O" 
        and to Validate position number and insert into table or board 
        """
        if character:
            if not all(cha in item for cha in value):
                raise ValueError(self.msg)

        if positions:
            key_find = [key for key, value in self.map_get_position.items() 
                                            if value == position]
            split_string = key_find[0].split()
        
            row, col = int(split_string[0]), int(split_string[1])
            if self.board[row][col] == ' ':
                self.board[row][col] = value

            else:
                raise ValueError(self.msg)
            return self.board

    def check_moves(self):
        board = self.board
        m_p =[]
        value_find = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    m_p.append(f'{i} {j}')
                    value_find = [value for key, value in self.map_get_position.items() 
                                  for mp in m_p if key == mp]
        for v in value_find:
            self.moves.append(v)
        return self.moves


class Player(GameFuctions):
    def __init__(self) -> None:
        super().__init__()

    def player(self, user_char: bool=True, user_position: bool=False):
        """
        To select wether player is "X" and cmputer is "O" or the other way round
        and to enter a valid position integer only
        """
        if user_char:
            while True:
                self.char = str(input("\nEnter X or O: ")).upper()
                self.msg = "\n[bold red]Error: [/bold red][bold yellow]you are to only enter alphabet X and O [/bold yellow]"
                try:
                    self.validator(value=self.char, item=self.valid_str)
                    break
                except ValueError as e:
                    print(f"{e}")

        if user_position:
            while True:                
                try:
                    self.pos = int(input('\nEnter number 1-9: '))
                    self.msg = f'{self.pos} has been taken chose another position'
                    try:
                        self.validator(value=self.char, position=self.pos, character=False, positions=True)
                        break
                    except ValueError as e:
                        print(f"\n [bold red]{e}[/bold red]")
                        continue
                except:
                    print(f"[bold red]Invalid Number[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")


class ComputerAi(GameFuctions):
    def __init__(self) -> None:
        super().__init__()
    
        #Computer Function
    def computer_player(self):
        """
        Computer player (Easy mode just selecting random number)
        """
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        else:
            self.comp_char = 'X'

        #generating random moves
        def gen_randomNumber(value: list) -> int:
            global comp_pos
            try:
                comp_pos = random.choice(value)
                return comp_pos
            except:
                if self.fullBoard():
                    pass
                else:
                    self.check_moves()
                  
        try:
            comp_pos = gen_randomNumber(self.moves)

            self.moves = self.moves

            if comp_pos == self.pos:
                comp_pos = gen_randomNumber(self.moves)
              
            try:
                self.validator(value=self.comp_char, position=comp_pos, character=False, positions=True)    
            except ValueError as e:
                print(f"[bold red]{e}[/bold red]")
            
            # Delete current player position from computer moves
            try:
                self.moves.remove(comp_pos)
                if self.pos in self.moves:
                    self.moves.remove(self.pos)
            except Exception as e:
                print(f"[bold red]{e}[/bold red]")

 
        except Exception as e:
            print(f"[bold red]{e}[/bold red]")
        
    
class GameBuild(Player, ComputerAi):
    def __init__(self) -> None:
        super().__init__()
        self.main()

    def main(self, not_replay=True):
        """ Runs the Game """
        if not_replay:
            self.player()
        
        self.go_first()
        
        while True:
            try:
                result, message, winer = self.check_wins()
                self.winer = winer
                if result == 'win':
                    if winer == 'X':
                        self.player_X += 1
                    elif winer == 'O':
                        self.player_O += 1
                    print(f'\n\n [bold blue]{message} [/bold blue] \n\n Player X = [bold blue]{self.player_X}[/bold blue] \n Player O = [bold blue]{self.player_O}[/bold blue]')
                    break
                elif result == 'tie':
                    print(f'\n\n [bold blue]{message}[/bold blue] \n\n')
                  
                    break
                elif result == 'No match':   
                    self.player(user_char=False, user_position=True)
        
                    self.computer_player()
    
                for line in self.draw_board():
                    print(line)
            except Exception as e:
                print(f'[bold red] {e}[/bold red]')
                break
          
        self.replay()


if __name__ == '__main__':
    GameBuild()


