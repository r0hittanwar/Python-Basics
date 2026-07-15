from typing import list, Tuple, Dict, Union

n : int = 5

name : str = "Rohit"

numbers: list[int] = [1, 2, 3, 4, 5]   #list of integers

person : Tuple[str, int] = ("Alice", 2)   #Tuple of a string and an integer

scores : Dict[str, int] = {"Harry" : 1, "Bob" : 25}    #Dictionary with strings keys and integer values

identifier : Union[str, int] = "ID123"    #Union type for variables that can hold multiple types
 


# in functions
def sum(a : int, b : int) -> int:
    return a + b
