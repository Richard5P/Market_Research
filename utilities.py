"""
This package contains general utility functions
for import into other packages
"""
import os
import getch


# copied from Tomislav Dukez https://github.com/tomdu3
# import os
# import getch
def clear_screen():
    '''
    Clears the terminal screen
    '''

    # detects if the script is run on MS Windows system
    # and uses the corresponding command
    if os.name == 'nt':
        os.system('cls')

    # for Linux/MacOs different clear command
    else:
        os.system('clear')


def key_press():
    """
    Pause flow and allow user to clear screen before next feature
    """
    print('\nPlease, press any key to clear the screen and continue...')
    key = getch.getch()
    return True


def clear_screen():
    '''
    Clears the terminal screen
    '''
    # detects if the script is run on MS Windows system
    # and uses the corresponding command
    if os.name == 'nt':
        os.system('cls')
    # for Linux/MacOs different clear command
    else:
        os.system('clear')

# end of copy


def lists_intersection(lst1,  lst2):
    intersect_lst = list(set(lst1) & set(lst2))
    if len(intersect_lst) > 0:
        return (intersect_lst)
    else:
        return False