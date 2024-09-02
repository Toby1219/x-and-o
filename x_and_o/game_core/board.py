from rich import print
from .Logs import logger_func

log = logger_func('board.py', 'board')

class Board:
    def __init__(self) -> None:
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        
        log.info(f'Board initialization {self.board}')

    def draw_board(self):
        """ Draws Board"""
        log.info('Drawing board')
        line_through = '___'
        v = [line_through for _ in range(3)]
        count = 0
        for row in self.board:
            yield ' | '.join(row)
            
            if count != 2:
                st2 = ''.join(v)
                yield st2
            count += 1 
        log.info('Done drawing board') 
