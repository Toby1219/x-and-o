import math
from .functions import GameFunctions

class ComputerAiSmart(GameFunctions):
    """ This class contains every function and controls of the computerAi
    using minimax and Alpha-beta pruning algo you can beat me hahahaha..... """

    def __init__(self) -> None:
        super().__init__()
        self.__move_hard: list = []
    
    def reset_moves(self):
        """ Reset moves """
        self.__move_hard.clear()
        return self.__move_hard
    
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
    def computer_player_had(self):
        """
        Computer player AI (HARD mode it has played the game before you played)
        """
        self.comp_char = 'O'
   
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        elif self.char == 'O':
            self.comp_char = 'X'
        else:
            self.comp_char = self.comp_char


        self.__move_hard = self.fetch_move()
        if not self.fullBoard():
            self.comp_pos = self.__move_hard[0]
            try:    
                self.validator(value=self.comp_char, position=self.comp_pos, 
                                item=self.valid_str, positions=True, character=True)
            except ValueError as e:
                print(f'[bold red]{e}[/bold red]')
            self.__move_hard.clear() 