import datetime

"""
This file contains the classes, function and variables for
the user processes for configuring the report calculations.
The file is meant to be imported into and called from a parent file
for deployment.
"""


class InvalidPercents(Exception):
    """
    Raise when percents don't add up to 100
    """
    pass


class InvalidDateRange(Exception):
    """
    Raise when years are out of range
    """
    pass


class InvalidRegion(Exception):
    """
    Raise when region(s) entered are not in list
    """
    pass


def years_loaded(stat_dict):
    """
    Returns the earliest and lastest statistic years in the dictionary
    Assumes all other report options have same years loaded
    """
    years_loaded = set()
    for code in stat_dict:
        if code['stats_code'] == 'popu':
            for country in code['country_stats']:
                for stat in country['statistics']:
                    years_loaded.add(stat['year'])
        else:
            continue
    first_year = min(years_loaded)
    last_year = max(years_loaded)
    print(first_year, last_year)
    return ([first_year, last_year])


def input_years(stat_dict):
    """
    Prompts user for date range report configuration
    """
    range_of_years = years_loaded(stat_dict)
    print(f'\nNow choose the range of years:')
    print(f'The range of years studies available for your report are '
          f'from: {range_of_years[0]} to: {range_of_years[1]}')
    print(f'\nPlease enter a start year and an end year within that '
          f'range (inclusive)')
    years_unset = True
    while years_unset:
        try:
            start_year = input('Report start year:\n')
            end_year = input('Report end year:\n')
            if not (start_year >= range_of_years[0] and
               end_year <= range_of_years[1]):
                raise InvalidDateRange
            else:
                return ([start_year, end_year])
        except InvalidDateRange:
            print(f'\nYears must be between {range_of_years[0]} and )'
                  f'{range_of_years[1]}, please try again')


def regions_loaded(stat_dict):
    """
    Returns a list of regions
    Assumes all other report options have same years loaded
    """
    regions_loaded = set()
    for code in stat_dict:
        if code['stats_code'] == 'popu':
            for country in code['country_stats']:
                regions_loaded.add(country['region_code'])
        else:
            continue
    return (sorted(regions_loaded))


def input_regions(stat_dict):
    """
    Prompts user to select region(s) for report configuration
    """
    region_list = (regions_loaded(stat_dict))
    print(f'\nNow choose the region or regions to report on.')
    print(f'The following is a list of available regions.')
    print(f'Please use the exactly the same region code as in the list.')
    print(f'If you would like to report on more than one region, then'
          f'please separate them with commas similarly to the list.')
    regions_unset = True
    while regions_unset:
        try:
            report_regions = input('Report region(s):\n')
            if (all(regions in report_regions for regions in region_list)):
                raise InvalidRegion
            else:
                return (report_regions)
        except InvalidRegion:
            print(f'\nRegions must be from the list and in the same format, '
                  f'please try again')


def input_weights():
    """
    Prompts user for study weight report configuration
    """
    print(f'There are 3 report studies available for your report:'
          f'\t Disposable Income, Population, Urbanisation\n')
    print(f'Please enter 3 numbers which total to 100 for weighting the'
          f' percent of each study')
    pct_unset = True
    while pct_unset:
        try:
            disp_pct = int(input('Disposable Income %:\n'))
            popu_pct = int(input('Population %:\n'))
            urba_pct = int(input('Urbanisation %:\n'))
            if ((disp_pct + popu_pct + urba_pct) != 100):
                raise InvalidPercents
            else:
                return ([disp_pct, popu_pct, urba_pct])
        except InvalidPercents:
            print('\nAmounts entered do not sum to 100, please try again')
        except ValueError:
            print('\nNumbers only, please try again')


def input_rpt_options(weights, years, regions, stat_dict):
    """
    Collect report options from user
    option functions return a list of values
    """
    print('Next step is to configure your report\n')
    weights = input_weights()
    years = input_years(stat_dict)
#    regions = input_regions()
    return ([weights, years])
