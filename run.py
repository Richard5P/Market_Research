"""
The app is a Market Research sample tool to demonstrate how Python can be used
to prepare and present a typical market reseach report for business analysis.
There are two primary services: 
    1) Import statistical demographical data from an external file
        Note: input files were created from XLXS spreadsheet and saved in CSV UTF-8(Comma delimited) format
    2) Prepare and present an ad-hoc market analysis report
The functions for each of those 2 services are contained in separate .py files.
    1)loadcsv.py
    2)report.py
This run.py contains the functions to:
   - initiate the app
   - initiate the error and results logging
        + functions for OS file operations
   - select the service to run
   - call the selected service
   - return a validation of the service run
   - allow the user to select another service or exit the app
"""

from loadcsv import import_csv2dict
from report import *
from datetime import datetime
import os
import getch 

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

# copied from Tomislav Dukez https://github.com/tomdu3
import os
import getch

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

def log_event(event_msg):
    """
    Opens or creates a log file to record errors and operation results 
    for session.
    """
    try:
        with open('logfile.txt','+a') as log:
            now = datetime.now()
            rundate = now.strftime('%m/%d/%Y %H:%M:%S%f')
            log.write('\n' + rundate + '\t'+ event_msg)
    except OSError as e:
        print(f'Unable to open log file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False    
    return True

def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
    # variables to be passed to reports
    weights = None
    years = None
    regions = None
    user_name = input('Please enter your name:\n')
    log_event('Application Start: '+user_name)
    print(f'\nHello {user_name}')
    stats_dict = import_csv2dict('population')
    if key_press():
        clear_screen()
    rpt_options = run_report(weights, years, regions, stats_dict)
    print(rpt_options)

main()