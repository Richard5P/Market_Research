"""
This file contains the functions and variables for
importing statistical data from a csv into a 
dictionary for reporting
"""

from datetime import datetime
import csv

# Contstants
# Initialise statics dictionary with keys


class UnknownStatsType(Exception):
    """
    Raise when stat_type is not found
    """
    pass


def load_country_stats(stats_dict, stats_code, data_row, header_row):
    """
    appends countries to STATS for each data row in CSV
    calls load_statistics to append statics for each country
    """
    stats_dict.append({
        'country_name': data_row[1],
        'region_code': data_row[2],
        'region_name': data_row[3],
        'statistic': load_statistics(stats_dict, stats_code,
                      data_row, header_row)
    }
    )


def load_statistics(stats_dict, stats_code, data_row, header_row):
    """
    loads annual statistical data for each country from stats_code.csv into
    a list of annual statistics and returns that to the load_country_stats
    function to load with the other country statistics
    uses header row for year value and data rows for values
    """
    annual_stats = []
    value_row = data_row
    year_row = header_row
    for i in range(4, len(year_row)):
        print(f'\n')
        annual_stats.append({
            'stats_code': stats_code,
            'year': year_row[i],
            'value': value_row[i]})
    return (annual_stats)


def import_csv2dict():
    """
    Imports data from csv file to python dictionary
    Assumes the csv file has headings in the first row for statistics keys
    Calls function to load remaining rows into STATS
    """
# create that stats_dict skeleton
    stats_dict = [
        {'country_code': None,
         'country_name': None,
         'region_code':  None,
         'region_name':  None,
         'statistic': [{
            'stats_code': None,
            'year': None,
            'value': None
            }]
        }
    ]
# loop through the various statistitics to load
    for stats_name in ['income', 'population', 'urban']:
        stats_code = stats_name[:4].upper()
        file_name = stats_name + '.csv'
        header_row = []
        try:
            with open(file_name, 'r', encoding='utf-8-sig', newline='')\
              as csv_file:
                csv_data = csv.reader(csv_file, dialect='excel')
                first_row = True
                for row in csv_data:
                    if first_row:
                        header_row = row
                        first_row = False
                        continue
                    else:
                        load_country_stats(stats_dict, stats_code, row,
                                           header_row)
                        continue

        except OSError as e:
            print(f'Unable to open CSV file. Please contact system'
                  f'manager with error:\n  >>  {e.args[1]}  <<')
            return False

    return (stats_dict)
