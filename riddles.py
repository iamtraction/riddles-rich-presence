"""
Riddles is a simple text-based riddles game.
It implements Discord's rich presence using the discoIPC Python package.
"""

from discoIPC import ipc
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'details': 'Playing a game of riddles, and showing you all off!',
    'timestamps': {},
    'assets': {
        'small_image': 'riddles_icon',
        'small_text': 'Riddles',
    }
}


def main():
    """Riddles. A small text-based riddle game with Discord Rich Presence."""
    client = ipc.DiscordIPC(config['CLIENT']['client_id'])
    # Connect to Discord Client
    client.connect()

    print('\nStarting Riddles...\n')
    time.sleep(5)

    # Level 1.
    client.update_activity(set_activity(1))  # Update Activity

    while True:
        print('A merchant can place 8 large boxes or 10 small boxes into a ' +
              'carton for shipping. In one shipment, he sent a total of 96 ' +
              'boxes. If there are more large boxes than small boxes, how ' +
              'many cartons did he ship?\n')
        answer = input('Answer: ')

        # Answer is 11:
        # 7 large boxes (7 * 8 = 56 boxes)
        # 4 small boxes (4 10 = 40 boxes
        # 11 total cartons and 96 boxes

        if answer == '11':
            print('\nCorrect! Let\'s move on to the next riddle.\n')
            break
        else:
            print('\nWrong answer! Let\'s try again.\n')

    # Level 2.
    client.update_activity(set_activity(2))  # Update Activity

    while True:
        print('If 9999 = 4, 8888 = 8, 1816 = 6, 1212 = 0, then 1919 =\n')
        answer = input('Answer: ')

        # Answer is 4:
        # Look at how many closed areas are there.
        #  -  9999 has 4 closed areas (the top of the '9')
        #  -  8888 has 8 closed areas, the top and bottom parts of the 8 and
        #         there are no other digits
        #  -  1816 has 3 closed areas, (top and bottom of 8 and bottom of 6,
        #         and it has 2 other digits ( 3*2=6)
        #  -  1212 has 0 closed areas,(0*4=0)

        if answer == '4':
            print('\nCorrect! That\'s the end, thanks for playing.\n')
            break
        else:
            print('\nWrong answer! Let\'s try again.\n')

    # The End!
    client.disconnect()


def set_activity(level):
    """Set acitivty for the player."""
    activity = base_activity
    activity['state'] = 'Playing Level {0}'.format(level)
    activity['timestamps']['start'] = time.time()
    activity['assets']['large_image'] = 'level_{0}'.format(level)
    activity['assets']['large_text'] = 'Level {0}'.format(level)
    return activity


if __name__ == '__main__':
    main()
