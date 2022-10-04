#python 3.10

import random
import logging
import json

logging.basicConfig(filename='log_ModuleJJ.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'This log message appears in log_ModuleJJ.txt.')

def compileroster():
    roster = json.loads(open('Projects\HobbyBot\jjbaasbr_roster.json').read())
    return roster

def generate(teamsize, assist_on = bool) -> list:
    n = 0
    slot = 1
    jjteam = []
    roster = compileroster()
    rosterselect = roster
    while teamsize != n:
        character = random.choice(rosterselect)
        rosterselect.remove(character)
        if assist_on and n % 2:
            jjteam = jjteam + [f'A{slot}: {character}']
            logging.debug(f'{slot}: {character}\n')
            n = n+1
            slot = slot+1
            continue
        else:
            jjteam += [f'**{slot}: {character}**']
            logging.debug(f'{slot}: {character}\n')
            n = n+1
            if assist_on is False:
                slot = slot+1
            continue
    else:
        logging.debug(f'Generated team\n{jjteam}')
        return list(jjteam)

def main():
    generate(6, True)