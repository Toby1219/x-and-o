from .functions import GameFunctions
import random
from rich import print




class ComputerAiMedium(GameFunctions):
    """ This class contains every function and controls of the manager """
    def __init__(self) -> None:
        super().__init__()
        self.__moves_mid: list = self.get_wining_path()
    
    
    def reset_moves(self):
        """ Reset moves """
        self.__moves_mid.clear()
        self.__moves_mid = self.get_wining_path(self.maps_win)
        return self.__moves_mid
    
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
    
    def move_manager_med(self)->list[int]:
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
    def computer_player_mid(self):
        """
        Computer player (medium mode it has learned the game)
        """
        self.comp_char = 'X'
       
        # Select computer character
        if self.char == 'X':
            self.comp_char = 'O'
        elif self.char == 'O':
            self.comp_char = 'X'
        else:
            self.comp_char = self.comp_char
     
            
    
        #Delete player position from computer to avoid conflit
        if self.pos in self.__moves_mid:
            self.__moves_mid.remove(self.pos)      
        
        if len(self.__moves_mid) == 0:
            self.__moves_mid = self.move_manager_med()
            self.comp_pos = random.choice(self.__moves_mid)
            try:
                self.validator(value=self.comp_char, position=self.comp_pos, 
                                    item=self.valid_str, positions=True, character=True)
            except ValueError as e:
                print(f'[bold red]{e}[/bold red]')

            self.__moves_mid.remove(self.comp_pos)
        else:
            self.comp_pos = random.choice(self.__moves_mid)
            try:
                self.validator(value=self.comp_char, position=self.comp_pos, 
                                item=self.valid_str, positions=True, character=True)
            except ValueError as e:
                print(f'[bold red]{e}[/bold red]')
            self.__moves_mid.remove(self.comp_pos)