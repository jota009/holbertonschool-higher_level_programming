#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    #     except IndexError:
    #         break
    print()
    return counter
