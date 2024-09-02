import math
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
        self.moves: list = []
        
        self.player_X = 0
        self.player_O = 0
        self.total_point = 0
        self.winner = ''

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

    def cleanBoard(self):
        """ Reset Board """
        for i in range(len(self.board)):
            for y in range(len(self.board[i])):
                if self.board[i][y] == 'X' or self.board[i][y] == 'O':
                    self.board[i][y] = ' '
        return self.board 
    
    def calculate_score(self):
        """ Calculates scores or point """
        if self.player_X > self.player_O:
            self.total_point = self.player_X
            print(f'\n\n Highest Point = [bold green]{self.total_point}[/bold green] \n [bold green]{self.winner}[/bold green] wins this round :smile: \n\n Sad to see you go :cry: \n\n')       

        elif self.player_O > self.player_X:
            self.total_point = self.player_O
            print(f'\n\n Highest Point = [bold green] {self.total_point}[/bold green] \n [bold green]{self.winner}[/bold green] wins this round :smile: \n\n Sad to see you go :cry: \n\n')       

        elif self.player_O == self.player_X:
            self.total_point = f'"X": {self.player_X} "O": {self.player_O}'
            print(f'\n\n Tie Game [bold green]{self.total_point}[/bold green] \n\n Sad to see you go :cry: \n\n')       
   
    def reset_moves(self):
        """ Reset moves """
        self.moves.clear()
        #self.moves = [1,2,3,4,5,6,7,8,9]
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
            self.main(replay = True)
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


    def fullBoard(self):
        return all(self.board[rows][col] != ' ' for rows in range(3) for col in range(3)) 

    def check_wins(self)-> str:
        """ Check for wins in Coloums, Rows and Vertical """
        # row win
        for  row in self.board:
            if row[0] == row[1] == row[2]:
                if row[0] == 'X':
                    return ['win', f'Winner is "X"', 'X'] 
                elif row[0] == 'O':
                    return ['win', f'Winner is "O"', 'O']
        # column win
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column]:
                if self.board[0][column] == 'X':
                    return ['win', f'Winner is "X"', 'X']
                if self.board[0][column] == 'O':
                    return ['win', f'Winner is "O"', 'O']
        
            # Check diagonals for victory
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == "X":
                return ['win', f'Winner is "X"', 'X']
            elif self.board[0][0] == "O":
                return ['win', f'Winner is "O"', 'O']

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == "X":
                return ['win', f'Winner is "X"', 'X']
            elif self.board[0][2] == "O":
                return ['win', f'Winner is "O"', 'O']
            
        elif self.fullBoard():
            return  ['tie', 'Tie game...', ' ']            
        else:
            return ['No match', ' ', ' ']
        
        return 0,0,0
        

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
                        print(f"\nError line 239: [bold red]{e}[/bold red]")
                        continue
                except:
                    print(f"Error line 242: [bold red]Invalid Number:[/bold red] [bold yellow]enter number (1-9)[/bold yellow]")

class ComputerAiSmart(GameFuctions):
    """ This class contains every function and controls of the computerAi
    using minimax and Alpha-beta pruning algo you can beat me hahahaha..... """

    def __init__(self) -> None:
        super().__init__()
    
    def check_wins_computer(self):
        """" checking wins for minimax algorithm """
        winning_positions = [
            [(0, 0), (0, 1), (0, 2)],  # Top row
            [(1, 0), (1, 1), (1, 2)],  # Middle row
            [(2, 0), (2, 1), (2, 2)],  # Bottom row

            [(0, 0), (1, 0), (2, 0)],  # Left column
            [(0, 1), (1, 1), (2, 1)],  # Middle column
            [(0, 2), (1, 2), (2, 2)],  # Right column
            
            [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)],  # Diagonal from top-right to bottom-left
        ]
        for positions in winning_positions:
            lines = [self.board[x][y] for x, y in positions]
            if lines == [self.comp_char, self.comp_char, self.comp_char]:
                return 1
            elif lines == [self.char, self.char, self.char]:
                return -1
            
        if self.fullBoard():
            return 0
        
        return None
            
    def move_manager(self, depth: int, alpha, beta, PlayerAi: bool):
        """ Using minimax and Alpha-beta pruning algorithim"""
        score = self.check_wins_computer()
        if score is not None:
            return score
        
        if PlayerAi:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = self.comp_char

                        value = self.move_manager(depth +1, alpha, beta, False)
                        
                        self.board[row][col] = ' '

                        best_score = max(value, best_score)

                        # Alpha-beta pruning
                        alpha = max(alpha, value)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = self.char

                        value = self.move_manager(depth +1, alpha, beta, True)

                        self.board[row][col] = ' '

                        best_score = min(value, best_score)

                        # Alpha-beta pruning
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
            return best_score

    def fetch_move(self):
        """ get best move for ai"""
        best_move = -math.inf
        move = (-1, -1)
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = self.comp_char

                    value = self.move_manager(0, -math.inf, math.inf, False)

                    self.board[row][col] = ' '
                    if value > best_move:
                        best_move = value
                        move = (f'{row} {col}')
        convert = [v for k, v in self.map_get_position.items() if move == k]
        return convert

    
    #Computer Function
    def computer_player(self):
        """
        Computer player AI (HARD mode it has played the game before you played)
        """
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        else:
            self.comp_char = 'X'


        self.moves = self.fetch_move()
        if not self.fullBoard():
            self.comp_pos = self.moves[0]    
            self.validator(value=self.comp_char, position=self.comp_pos, 
                                item=self.valid_str, positions=True, character=True)
            self.moves.clear() 

class GameBuild(Player, ComputerAiSmart):
    """ This is the builder for the entire game """
    def __init__(self) -> None:
        super().__init__()

        self.main()

    def main(self, replay=False):
        """ Runs the Game """
        if not replay:
            self.player()  

        self.go_first()
        
        while True:
            result, message, winner = self.check_wins()
            if result == 'win':
                self.winner = winner
                if winner == 'X':
                    self.player_X += 1
                elif winner == 'O':
                    self.player_O += 1
                print(f'\n\n [bold blue]{message} [/bold blue] \n\n Player X = [bold blue]{self.player_X}[/bold blue] \n Player O = [bold blue]{self.player_O}[/bold blue]')
                break
            
            if result == 'tie':
                print(f'\n\n [bold blue]{message}[/bold blue] \n\n')
                break

            if result == 'No Match':
                continue

            self.player(user_char=False, user_position=True)
            self.computer_player()
            for line in self.draw_board():
                print(line)
        
        self.replay() 


if __name__ == '__main__':
   GameBuild()



