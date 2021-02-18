"""
    @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab One: 
    
    Temperature converter
"""
import Meritt_Josh_converter as converter


def convert():
    """
        Main loop for program. 
         - Finds new temperature for each iteration.
    """
    is_exiting = False
    while is_exiting == False:
        print("The new temperature is: " + str(converter.convert(converter.check_int())))
        is_exiting = is_exit()
    print("[Exiting]")
    
    
def is_exit():
    """
        Checks if the user would like to exit the program. 
    """
    command = input("Run again? ")
    print("")
    if command == "no" or command =="n" or command == "false":
        return True
    return False
    

if __name__ == '__main__':
    print(""" 
  _______                                  _                                                  _            
 |__   __|                                | |                                                | |           
    | | ___ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ ___    ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
    | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _ \  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
    | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | |  __/ | (_| (_) | | | \ V /  __/ |  | ||  __/ |   
    |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \___|  \___\___/|_| |_|\_/ \___|_|   \__\___|_|   
                     | |                                                                                   
                     |_|                                                                                       """)
    convert()