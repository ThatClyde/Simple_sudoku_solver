import os 
from models import Table
        
def clearscreen():
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.system('cls')

