"""
This file contains the classes, function and variables for
the user processes for output presentation of the report calculations. 
The file is meant to be imported into and called from a parent file 
for deployment.
"""

from datetime import datetime
import csv
from colorama import Fore, Back, Style


def output_results(calc_results, rpt_options, user_name):
    """
    Calls functions to write report to:
       csv file - formatted as a spreadsheet
       display to the terminal for user to review
    """
    if export_rpt2csv(calc_results, user_name) and\
       display_report(calc_results):
        return True
    else:
        return False


def display_report(calc_results):
    return True


def export_rpt2csv(calc_results, user_name):
    """
    Writes report summary data to csv file
    formated for spreadsheet
    """
    now = datetime.now()
    rundate = now.strftime('%d%m%Y_%H%M:%f')
    exp_file_name = rundate + '_' + user_name
    try:
        with open(exp_file_name, 'w') as rpt_ouput:
            write_row = csv.writer(rpt_ouput)
            write_row.writerow(list(calc_results.keys()))
            for region in calc_results:
                for stat_type in calc_results[region]:
                    print(stat_type, calc_results[region][stat_type])
#                print(list(calc_results[region].values()))
#                for stat_type in region.values()
#                   write_row(stat_type, region[stat_type])
        return True

    except OSError as e:
        print(Fore.RED + f'Unable to open CSV file: {exp_file_name}\n'
              f' Please contact system'
              f' manager with error:\n  >>  {e.args[1]}  <<')
        print(Fore.BLACK)
        return False
