"""
    @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab One: 
    
    Temperature converter
        - helper method
"""


def convert(temp):
    """
        Converts the temperature based on user input of what scale.
        
        @param:
            temp : int of the temperature to be converted
            
        @return:
            the new temperature.
    """
    while True:
        scale = input("Enter 'f' to convert to Fahrenheit or 'c' to convert to Celsius: ")
        if scale == 'c':
            return (temp - 32) * (5.0 / 9.0)
        elif scale == 'f':
            return temp * (9.0 / 5.0) + 32
        else :
            print("[Error] Incorrect scale. Try c or f.\n")
        
        
def check_int():
    """
        Checks if the number entered is an int. This finds the temperature to be converted.
        
        @return: 
            the temperature to be converted.
    """
    while True:
        try:
            temp = int(input("Enter a temperature to convert: "))
            return temp
        except ValueError or TypeError:
            print("[Error]Incorrect Type. Try an integer.\n")