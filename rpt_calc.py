"""
This file contains the classes, function and variables for
calculating the analytical report based on the configured statistics.
The file is meant to be imported into and called from a parent file for
deployment.
"""


def calc_region(sum_region, region_data, stats_dict):
    """
    Checks if region has sum_value and returns it for
    use in summing region values for report
    """
    for i in range(0, len(region_data)):
        if sum_region in region_data[i].values():
            sum_value = region_data[i]['sum_value']
        else:
            sum_value = 0
    return (sum_value)


def avg_report_data(years, regions, stats_dict):
    """
    Using the report options, calculate the average statistic values
    for each region and type of statistic across the range of years.
    The calculations will support regional reporting and future
    country reporting.
        country_avg =
            sum_value (for range of years)/number of years
        region_avg =
            sum country_annual_avg (for countries in regaion)/
                number of countries in region
    Return a list of lists: [region code, stat code, avg value]
    Assumes the stats_dict is sorted by country by region
    """
    num_years = int(years[1]) - int(years[0])
    region_data = [{'region': None, 'sum_value': None, 'num_countries': 0}]
    region_value = 0
    for country in stats_dict:
        if country['region_code'] in regions:
            sum_region = country['region_code']
            region_value = calc_region(sum_region, region_data, stats_dict)
            for statistic in country['statistic']:
                sum_stat_code = statistic['stats_code']
                if statistic['year'] >= years[0] and \
                   statistic['year'] <= years[1]:
                    sum_value += float(statistic['value'])
                country_avg = sum_value / num_years
            avg_value = sum_value / num_countries
            sum_data.append([sum_region, sum_stat_code, avg_value])
    return (sum_data)


def calc_stats(report_options, stats_dict):
#    weights = report_options[0]
    years = report_options[1]
    regions = report_options[2]
    selection_results = sum_report_data(years, regions, stats_dict)
    return (selection_results)
