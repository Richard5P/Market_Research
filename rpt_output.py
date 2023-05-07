"""
This file contains the classes, function and variables for
the user processes for output presentation of the report calculations. 
The file is meant to be imported into and called from a parent file 
for deployment.
"""

from datetime import datetime
import csv
from colorama import Fore, Back, Style
from utilities import key_press


def format_value_by_type(num, type):
    """
    Formats float values to display format
    according to the type of statistic
    INCO $00,000
    POPU 000,000
    URBA %
    """
    out_num = 0.0
    if type == 'INCO':
        out_num = '${:,.2f}'.format(num)
    elif type == 'POPU':
        out_num = '{:,f}'.format(num)
    elif type == "URBA":
        out_num = '{:0.2%}'.format(num/100)
    return out_num


def display_report(calc_results):
    for region in calc_results:
        print(f'\n{region}\n')
        for stat_type in calc_results[region]:
            raw_value = calc_results[region][stat_type]
            display_value = format_value_by_type(raw_value, stat_type)
            print(f'{stat_type}: {display_value}')
    key_press()
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
            writer = csv.writer(rpt_ouput, dialect='excel')
            writer.writerow(list(calc_results.keys()))
            for region in calc_results:
                for stat_type in calc_results[region]:
                    out_row = [stat_type,
                               calc_results[region][stat_type]]
                    writer.writerow(out_row)
        return True

    except OSError as e:
        print(Fore.RED + f'Unable to open CSV file: {exp_file_name}\n'
              f' Please contact system'
              f' manager with error:\n  >>  {e.args[1]}  <<')
        print(Fore.BLACK)
        return False


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
