from rich import print

class Board:
    def __init__(self) -> None:
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

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
