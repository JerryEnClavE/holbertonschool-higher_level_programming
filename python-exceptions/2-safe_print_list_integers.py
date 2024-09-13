#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            # Try to format and print the element as an integer
            print("{:d}".format(my_list[i]), end=" ")
            printed_count += 1
        except (ValueError, TypeError, IndexError):
            # Ignore non-integers and out-of-bounds index silently
            pass
    print()  # To ensure the output ends with a newline
    return printed_count
