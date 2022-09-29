#python 3.10

import random
import logging

logging.basicConfig(filename='log_ModuleJJ.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'This log message appears in log_ModuleJJ.txt.')

def compileroster():
    part1 = ['Jonathan Joestar','Will A. Zeppeli','Robert E. O. Speedwagon','Dio Brando',]
    part2 = ['Joseph Joestar','Caesar Anthonio Zeppeli','Lisa Lisa (Elizabeth)','Wamuu','Esidisi','Kars',]
    part3 = ['Jotaro Kujo & Star Platinum','Old Joseph Joestar & Hermit Purple','Muhammad Avdol & Magician\'s Red','Noriaki Kakyoin & Hierophant Green','Jean Pierre Polnareff & Silver Chariot','Iggy & The Fool','Hol Horse & Emperor','Mariah & Bastet','Pet Shop & Horus','Vanilla Ice & Cream','DIO & The World',]
    part4 = ['Josuke Higashikata 4 & Crazy Diamond','Koichi Hirose & Echoes','Okuyasu Nijimura & The Hand','Rohan Kishibe & Heaven\'s Door','Jotaro Kujo 4 & Star Platinum','Yukako Yamagishi','Shigekiyo Yangu & Harvest','Akira Otoishi & Red Hot Chili Pepper','Yoshikage Kira & Killer Queen','Kosaku Kawajiri & Killer Queen',]
    part5 = ['Giorno Giovanna & Gold Experience','Bruno Bucciarati & Sticky Fingers','Guido Mista & Sex Pistols','Narancia Ghirga & Aerosmith','Pannacotta Fugo & Purple Haze','Trish Una & Spice Girl','Prosciutto & Pesci with Beach Boy','Ghiaccio & White Album','Diavolo & King Crimson',]
    part6 = ['Jolyne Cujoh & Stone Free','Ermes Costello & Kiss','Narciso Anasui & Diver Down','Foo Fighters','Enrico Pucci & Whitesnake',]
    part7 = ['Johnny Joestar & Tusk','Gyro Zeppeli','Diego Brando','Funny Valentine & D4C',]
    part8 = ['Josuke Higashikata 8 & Soft & Wet',]
    other = ['Ikuro Hashizawa']
    roster = []
    roster.extend(part1)
    roster.extend(part2)
    roster.extend(part3)
    roster.extend(part4)
    roster.extend(part5)
    roster.extend(part6)
    roster.extend(part7)
    roster.extend(part8)
    roster.extend(other)
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