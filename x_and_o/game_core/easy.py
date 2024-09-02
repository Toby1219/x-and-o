import random
from rich import print
from .functions import GameFunctions

class ComputerAi_Easy(GameFunctions):
    def __init__(self) -> None:
        super().__init__()
        self.__moves_easy: list = [x for x in range(1, 10)]
        

    def reset_moves(self):
        """ Reset moves """
        self.__moves_easy = [x for x in range(1, 10)]
        return self.__moves_easy

    def check_moves(self):
        board = self.board
        m_p =[]
        value_find = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    m_p.append(f'{i} {j}')
                    value_find =self.convert_positions(m_p, values=True)
        for v in value_find:
            self.__moves_easy.append(v)
        return self.__moves_easy

    #Computer Function
    def computer_player(self):
        """
        Computer player (Easy mode just selecting random number)
        """
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        elif self.char == 'O':
            self.comp_char = 'X'
        else:
            self.comp_char = 'O'

        #generating random moves
        def gen_randomNumber(value: list) -> int:
            try:
                self.comp_pos = random.choice(value)
                return self.comp_pos
            except:
                if self.fullBoard():
                    pass
                else:
                    self.check_moves()
                
        self.comp_pos = gen_randomNumber(self.__moves_easy)

        self.__moves_easy = self.__moves_easy

        if self.comp_pos == self.pos:
            self.comp_pos = gen_randomNumber(self.__moves_easy)
            
        try:
            self.validator(value=self.comp_char, position=self.comp_pos, positions=True)    
        except ValueError as e:
            print(f"[bold red]{e}[/bold red]")
        
        # Delete current player position from computer moves
        try:
            self.__moves_easy.remove(self.comp_pos)
            if self.pos in self.__moves_easy:
                self.__moves_easy.remove(self.pos)
        except Exception as e:
            print(f"[bold red]{e}[/bold red]")



