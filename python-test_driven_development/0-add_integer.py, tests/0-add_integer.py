#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if 'a' is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if 'b' is an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both 'a' and 'b' to integers
    a = int(a)
    b = int(b)
    
    # Return the sum
    return a + b
