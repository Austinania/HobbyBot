#python 3.10

import bot
import logging

logging.basicConfig(filename='log_HobbyBot.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This log message appears in log_HobbyBot.txt.')

if __name__ == '__main__':
    bot.run_discord_bot()