import time
import random
from colorama import Fore, Style, init

init(autoreset=True)  

TOWER_HEIGHT = 10  
COLUMNS = 10 

COLORS = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA]  

try:
    while True:
        for _ in range(TOWER_HEIGHT):  
            row = ''
            for _ in range(COLUMNS):  
                char = random.choice(['|', '#', '*', '-'])  
                color = random.choice(COLORS)  
                row += color + char + ' ' if random.random() > 0.3 else '  '  
            print(row)
        print()  
        time.sleep(0.2)  

except KeyboardInterrupt:
    print('\nVertical Struts - Modified by Dev Srivastava, based on Al Sweigart’s work (2024)')
