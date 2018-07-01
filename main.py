import math
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

if __name__ == '__main__':

	print(__doc__)

	#Ascii art 
	init(strip=not sys.stdout.isatty())
	cprint(figlet_format('G D S!', font='starwars'), 'green', 'on_red', attrs=['bold'])
	print("Gender Detection System !")


