import logging
from rich.logging import RichHandler

def logger_func(file, path, console=False)-> logging:
    log = logging.getLogger(f'{file}')
    log.setLevel(level=logging.DEBUG)

    handler = logging.FileHandler(f'x_and_o/game_core/Logs/{path}.logs', mode='w')
    formarts = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formarts)

    log.addHandler(handler)

    if console:
        terminal = RichHandler()
        formartTwo = logging.Formatter('%(levelname)s | %(message)s')
        terminal.setFormatter(formartTwo)
        log.addHandler(terminal)
    
    return log
