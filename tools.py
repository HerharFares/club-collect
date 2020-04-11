from config import REPLACE_ITEMS

def replacing(string):
    """To convert the name of the universities from 
    French to English.
    """
    for temp in REPLACE_ITEMS:
        string = string.replace(temp[0], temp[1])
    return string