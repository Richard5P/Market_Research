"""
This file contains the classes, function and variables for
calculating the analytical report based on the configured statistics.
The file is meant to be imported into and called from a parent file for
deployment.
"""


def sum_report_data(years, regions, stats_dict):
    """
    Using the report options, sum the statistic values for each region and
    type of statistic across the range of years.
    Return a list of lists: [region code, stat code, value sum]
    """
    sum_data = []
    sum_value = 0
    for country in stats_dict:
        if country['region_code'] in regions:
            sum_region = country['region_code']
            for statistic in country['statistic']:
                sum_stat_code = statistic['stats_code']
                if statistic['year'] >= years[0] and statistic['year'] <= years[1]:
                    sum_value += int(statistic['value'])
            sum_data.append([sum_region, sum_stat_code, sum_value])
    print(sum_data)
    return (sum_data)


def calc_stats(report_options, stats_dict):
    weights = report_options[0]
    years = report_options[1]
    regions = report_options[2]
    selection_results = sum_report_data(years, regions, stats_dict)
    print(selection_results)

