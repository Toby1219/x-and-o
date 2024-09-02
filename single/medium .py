import random
from rich import print

class GameAttributes:
    """
    This class contains all values and attributes use to build the game
    """
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
        
        self.maps_win = {
                # Top to Bottom Rows
                'row_one': [1, 4, 7],
                'row_two': [2, 5, 8],
                'row_three': [3, 6, 9],
                
                # Columns Left to Right
                'column_one': [1, 2, 3],
                'column_two': [4, 5, 6],
                'column_three': [7, 8, 9],

                # Diagonals
                'main_diag': [1, 5, 9],  # Top-left to bottom-right
                'anti_diag': [3, 5, 7]   # Top-right to bottom-left
            }
        
        self.valid_str = {'X', 'O'}
        self.valid_ans = {'yes', 'y', 'no', 'n'}
        self.char: str = ''
        self.comp_char: str = ''
        self.pos: int = ''

        self.comp_pos: int = ''
        self.moves: list = GameFuctions.get_paths(self.maps_win)
        
        self.player_X = 0
        self.player_O = 0
        self.total_point = 0
        self.winer = ''

        #validators variables
        self.msg: str = ''
    
        
class GameFuctions(GameAttributes):
    """ This class contains all game function  """
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
    
    @staticmethod
    def get_paths(map_paths)->list[int]:
        """ Generate paths for dictionary above """
        value = [v for k, v in map_paths.items()]
        move =  random.choice(value)
        return move 
    
    def reset_moves(self):
        """ Reset moves """
        self.moves.clear()
        self.moves = self.get_paths(self.maps_win)
        return self.moves

    def replay(self):
        """ Restart game """
        while True:
            try:
                question = str(input('\nWould you like to replay: ')).lower().strip()
                self.msg = '\nYou are to enter "yes", "y", "no", "n"'
                self.validator(value=question, item=self.valid_ans, character=True)
                break
            except ValueError as e:
                print(f"\nError line 178: [bold red] {e} [/bold red] \n")

        if question == 'yes' or question == 'y':
            print("\n\n [green]     Restarting the game.... \n\n  Cleaning the board..., Reseting computer moves...[/green] \n\n\t    Done :smile::smile::smile: \n\n")
            
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
                self.validator(value=conf, item=self.valid_ans, character=True)
                break
            except ValueError as e:
                print('Error line 199: ', e)

        if conf == 'yes' or conf == 'y':
            print('Scores: \n', self.player_X, '\n', self.player_O, '\n')
        elif conf == 'no' or conf == 'n':
            self.computer_player()
            for line in self.draw_board():
                print(line)
    
    def validator(self, value: str=None, position: int=None, item: set=None,
                           character: bool = False, positions: bool=False):
        """ 
        Validates Players inputs must be "X" OR "O" 
        and to Validate position number before insert into table or board 
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
        
        # removed checked move

class Player(GameFuctions):
    """ This class contains every function and controls of the player"""
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
                    self.validator(value=self.char, item=self.valid_str, character=True)
                    break
                except ValueError as e:
                    print(f"Error line 262: {e}")

        if user_position:
            while True:                
                try:
                    self.pos = int(input('\nEnter number 1-9: '))
                    self.msg = f'{self.pos} has been taken chose another position'
                    try:
                        self.validator(value=self.char, position=self.pos, positions=True)
                        break
                    except ValueError as e:
                        print(f"\nError line 276: [bold red]{e}[/bold red]")
                        continue
                except:
                    print(f"Error line 279: [bold red]Invalid Number:[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")


class ComputerAi(GameFuctions):
    """ This class contains every function and controls of the manager """
    def __init__(self) -> None:
        super().__init__()
    
    def check_empty_space(self, index:list[int])->list[str]:
            """check empty space and returns the character in the empty space either (X, O, or " ") """
            empty_spaces_character=[]
            for i in range(len(index)):
                x = int(index[i][0])
                y = int(index[i][2])
                empty_space = self.board[x][y]
                empty_spaces_character.append(empty_space)
            return empty_spaces_character

    def convert_positions(self, index:list, keys=False, values=False)->list:
        """ Convert index to numbers and also numbers to index """
        if keys:
            key =[k for k, v in self.map_get_position.items() if v in index ]
            return key
        if values:
            value = [v for k, v in self.map_get_position.items() if k in index]
            return value
        
    def get_wining_path(self)->list[int]:
        """ Generate winng paths """
        value_get =[v for k, v in self.maps_win.items()]
        path = random.choice(value_get)
        return path

    def removal(self, index_: list)->list[str]:
        """ Remove already played position and return not played position in line with winnig path """
        tobeRemoved = []
        #only returns index of all empty space
        for i in range(len(index_)):
            row = int(index_[i][0])
            col = int(index_[i][2])
            if self.board[row][col] == self.comp_char:
                tobeRemoved.append(f"{row} {col}")
                
         #ensures that there is element in list before process   
        if len(tobeRemoved) <= 2:
            for ind in range(len(tobeRemoved)):
                row = int(tobeRemoved[ind][0])
                col = int(tobeRemoved[ind][2])
                if self.board[row][col] == self.comp_char:
                    index_.remove(f"{row} {col}")
            return index_
        else:
            return 'Nothing to be removed....'

    def validate_position(self, path:list[int])->bool:
        """ Validate computer moves only """
        converted_number = self.convert_positions(index=path, keys=True)
        check_pos = self.check_empty_space(converted_number) 
          
        if (' ' in check_pos and self.comp_char in check_pos 
        and check_pos.count(self.comp_char) >=1 and self.char not in check_pos):
            return True
        else:
            return False
        
    def find_open_space(self):
        """ find open space """
        open_sapce = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if (self.board[row][col] == ' ' 
                    and self.board[row][col] != 'x' 
                    and self.board[row][col] != 'o'):
                    open_sapce.append(f"{row} {col}")
        move = self.convert_positions(index=open_sapce, values=True)
                
        return move
    

    def move_manager(self)->list[int]:
        """ Ensures all is well with computer moves """
        move = []
        validateTwo = True
        count = 0
        paths = self.get_wining_path()
        valid_path = self.validate_position(path=paths)
        while not valid_path:
            paths = self.get_wining_path()
            valid_path = self.validate_position(path=paths)
            count += 1
            if count == 20:
                move = self.find_open_space()
                validateTwo = False
                break 
    
        if validateTwo:
            remove_indexs=self.convert_positions(index=paths, keys=True)
            remove_index = self.removal(index_=remove_indexs)
            move = self.convert_positions(index=remove_index, values=True)
        return move
            
        
    #Computer Function
    def computer_player(self):
        """
        Computer player (HARD mode it has learned the game)
        """
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        else:
            self.comp_char = 'X'
    
        #Delete player position from computer to avoid conflit
        if self.pos in self.moves:
            self.moves.remove(self.pos)      
        
        if len(self.moves) == 0:
            self.moves = self.move_manager()
            self.comp_pos = random.choice(self.moves)
            self.validator(value=self.comp_char, position=self.comp_pos, 
                                item=self.valid_str, positions=True, character=True)
            self.moves.remove(self.comp_pos)
        else:
            self.comp_pos = random.choice(self.moves)
            self.validator(value=self.comp_char, position=self.comp_pos, 
                                item=self.valid_str, positions=True, character=True)
            self.moves.remove(self.comp_pos)
 
class GameBuild(Player, ComputerAi):
    """ This is the builder for the entire game """
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
                print(f'[bold red]Error from main: {e}[/bold red]')
                break
          
        self.replay()


if __name__ == '__main__':
    GameBuild()
    #print(GameBuild.__mro__)

