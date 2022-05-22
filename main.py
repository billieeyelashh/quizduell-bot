from pickle import TRUE
from utils import *
import coloredlogs, logging
import keyboard as kb


if __name__ == '__main__':
    
    start = True
    DEBUG = False
    if DEBUG == True:
        logging.basicConfig(level=logging.DEBUG)

    while start:
        # Checking for Buttons (highly inefficient)
        if locate_image('buttons/newGame.PNG'):
            print('[INFO] New Game found')
            Location = locate_image('buttons/newGame.PNG')
            click_on_coordinates(Location[0], Location[1])
            time.sleep(1)
        elif locate_image('buttons/next.PNG'):
            print('[INFO] Next Button found')
            Location = locate_image('buttons/next.PNG')
            click_on_coordinates(Location[0], Location[1])
            next += 1
            time.sleep(1)
            play()
        elif locate_image('buttons/play.PNG'):
            print('[INFO] Play Button found')
            Location = locate_image('buttons/play.PNG')
            click_on_coordinates(Location[0], Location[1])
            time.sleep(1)
            play()

        elif locate_image('buttons/randomPlayer.PNG'):
            print('[INFO] Random Player found')
            Location = locate_image('buttons/randomPlayer.PNG')
            click_on_coordinates(Location[0], Location[1])
            time.sleep(1)

        
