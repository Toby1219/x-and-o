from .board import Board
from rich import print

class GameAttributes(Board):
    def __init__(self) -> None:
        super().__init__()

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
        
        #validator attribs
        self.valid_str = {'X', 'O'}
        self.valid_ans = {'yes', 'y', 'no', 'n'}
        self.msg: str = ''
        
        #player attribs
        self.char: str = ''
        self.pos: int = ''

        #computer attribs
        self.comp_char: str = ''
        self.comp_pos: int = ''
        
        self.player_X = 0
        self.player_O = 0
        self.total_point = 0
        self.winner = ''

        self.player_one = None
        self.player_two = None
        self.mode = ''
        self.time = 0
        self.valid_mode = {'easy', 'e', 'medium', 'm', 'hard', 'h'}
        self.valid_gametype = ('ai vs ai', 'ai v ai', 'a vs a', 'a v a',  
                               'player vs player',  'player v player', 'p vs p', 
                               'p v p', ' ', 'none')

class GameFunctions(GameAttributes):
    def __init__(self) -> None:
        super().__init__()

    def fullBoard(self):
        return all(self.board[rows][col] != ' ' for rows in range(3) for col in range(3)) 

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

    def cleaner(self):
        """ Reset certain data for gametype and game mode"""
        self.player_O = 0
        self.player_X = 0
        self.comp_char = ''
        self.char = ''
        self.cleanBoard()
        self.reset_moves()

    def replay(self, *func, **kwargs):
        """ Restart game """
        while True:
            try:
                question = str(input('\nWould you like to replay: ')).lower().strip()
                self.msg = '\nYou are to enter "yes", "y", "no", "n"'
                self.validator(value=question, item=self.valid_ans, character=True)
                break
            except ValueError as e:
                print(f"\n [bold red] {e} [/bold red] \n")

        if question == 'yes' or question == 'y':
            print("\n\n [green] Restarting the game.... \n\n Cleaning the board..., Reseting computer moves... \n\n Done[/green] :smile::smile::smile: \n\n")
            
            self.cleanBoard()
            self.reset_moves()
            
            func[0](**kwargs)
        else:
            self.calculate_score()

    def cleanBoard(self):
        """ Reset Board """
        for i in range(len(self.board)):
            for y in range(len(self.board[i])):
                if self.board[i][y] == 'X' or self.board[i][y] == 'O':
                    self.board[i][y] = ' '
        return self.board 

    def go_first(self):
        """ Player decide wether to go first or not"""
        while True:
            try:
                conf = str(input('\nWould you like to go first: ')).lower().strip()
                self.msg = '\nYou are to enter "yes", "y", "no", "n"'
                self.validator(value=conf, item=self.valid_ans, character=True)
                break
            except ValueError as e:
                print(e)

        if conf == 'yes' or conf == 'y':
            print('Scores: \n', self.player_X, '\n', self.player_O, '\n')
        elif conf == 'no' or conf == 'n':
            self.computer_player()
            for line in self.draw_board():
                print(line)

    def convert_positions(self, index:list, keys=False, values=False)->list:
        """ Convert index to numbers and also numbers to index """
        if keys:
            key =[k for k, v in self.map_get_position.items() if v in index ]
            return key
        if values:
            value = [v for k, v in self.map_get_position.items() if k in index]
            return value

    def validator(self, value: str=None, position: list[int]=None, item: set=None,
                           character: bool = False, positions: bool=False):
        """ 
        Validates Players inputs must be "X" OR "O" 
        and to Validate position number and insert into table or board 
        """
        if character:
            if value not in item:
                raise ValueError(self.msg)
            else:
                pass
            
        if positions:
            key_find = self.convert_positions([position], keys=True)
            split_string = key_find[0].split()

            row, col = int(split_string[0]), int(split_string[1])
            if self.board[row][col] == ' ':
                self.board[row][col] = value
            else:
                raise ValueError(self.msg)
            return self.board

    def check_wins(self)-> tuple[str, str, str]:
        """ Check for wins in Coloums, Rows and Vertical """
        # row win
        for  row in self.board:
            if row[0] == row[1] == row[2]:
                if row[0] == 'X':
                    return ('win', f'Winner is "X"', 'X') 
                elif row[0] == 'O':
                    return ('win', f'Winner is "O"', 'O')
        # column win
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column]:
                if self.board[0][column] == 'X':
                    return ('win', f'Winner is "X"', 'X')
                if self.board[0][column] == 'O':
                    return ('win', f'Winner is "O"', 'O')
        
            # Check diagonals for victory
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == "X":
                return ('win', f'Winner is "X"', 'X')
            elif self.board[0][0] == "O":
                return ('win', f'Winner is "O"', 'O')

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == "X":
                return ('win', f'Winner is "X"', 'X')
            elif self.board[0][2] == "O":
                return ('win', f'Winner is "O"', 'O')
            
        elif self.fullBoard():
            return  ('tie', 'Tie game...', ' ')            
        else:
            return ('No match', ' ', ' ')
        
        return 0,0,0

    def game_type(self):
        """ To select gametype like Ai vs Ai, Player vs Player """
        gameType = ' '
        gameType = str(input(
                '\nWould you like Ai vs Ai, Player vs Player, none: ')).lower()
        
        if (gameType in ['ai vs ai', 'ai v ai', 'a vs a', 'a v a'] and 
            self.mode == 'Easy'):
            self.time = 2
            self.player_one = self.computer_player
            self.player_two = self.computer_player_mid
            return 1

        if (gameType in ['ai vs ai', 'ai v ai', 'a vs a', 'a v a'] and 
            self.mode in ['Meduim', 'Hard']):
            self.time = 2
            self.player_one = self.computer_player_mid
            self.player_two = self.computer_player_had
            return 1
        
        if gameType in ['player vs player', 'player v player', 'p vs p','p v p']:
            self.player_one = self.playerPvP_one
            self.player_two = self.playerPvP_two
            return 1
        elif gameType in [' ', 'none']:
            return 0
              
    def select_mode(self):
        """ To select which kind of ai you want easy, meduim hard """
        while True:
            mode = str(input('\nSelect Mode (easy, meduim, hard): '))
            self.msg = 'Select from (easy, meduim, hard) or (e, m, h)'
            try:
                self.validator(value=mode, item=self.valid_mode, character=True)
                break
            except ValueError as e:
                print(f'[bold red]{e}[/bold red]')
        if mode == 'easy' or mode == 'e':
            self.mode = 'Easy'
            self.player_two = self.computer_player

        elif mode == 'meduim' or mode == 'm':
            self.mode = 'Meduim'
            self.player_two = self.computer_player_mid
        
        elif mode == 'hard' or mode == 'h':
            self.mode = 'Hard'
            self.player_two = self.computer_player_had
        
        return self.mode
