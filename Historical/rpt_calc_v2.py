"""
This file contains the classes, function and variables for
calculating the analytical report based on the configured statistics.
The file is meant to be imported into and called from a parent file for
deployment.
"""


def calc_region_data(country_avg_values):
    """
    sums country stat_type average for region and returns summary list
    """
    region_value = None
    return (region_value)


def calc_country_data(years, regions, stats_dict):
    """
    Using the report options, calculate the average statistic values
    for each region and type of statistic across the range of years.
    The calculations will support regional reporting and future
    country reporting.
        country_avg =
            sum_value (for range of years)/number of years
        region_avg =
            sum country_avg (for countries in region)/
                number of countries in region
    Return a list of lists: [region code, stat code, avg value]
    Assumes the stats_dict is sorted by country by region
    region_data =[region_code, sum_value, num_countries]
    country_avg_value = [country_code, country_avg, region_code]
    """
    country_avg_values = []
    num_years = float(int(years[1]) - int(years[0]))
    for country in stats_dict:
        if country['region_code'] in regions:
            sum_region = country['region_code']
            sum_country_value = 0.0
            for statistic in country['statistic']:
                sum_stat_code = statistic['stats_code']
                if statistic['year'] >= years[0] and \
                   statistic['year'] <= years[1]:
                    sum_country_value += float(statistic['value'])
            country_avg = sum_country_value / num_years
            country_avg_values.append([sum_region, sum_stat_code, country_avg])
    print(country_avg_values)
    calc_region_data(country_avg_values)
    return (country_avg_values)
#    region_data = calc_region_data(regions, country_avg_values)
#    return (region_data)
    
    def sum_report_data(years, regions, stats_dict):
    """
    Using the report options, calculate the average statistic values
    for each region and type of statistic across the range of years.
    The calculations will support regional reporting and future
    country reporting.
        country_avg =
            sum_value (for range of years)/number of years
        region_avg =
            sum country_avg (for countries in region)/
                number of countries in region
    Return a list of lists: [region code, stat code, avg value]
    Assumes the stats_dict is sorted by country by region
    region_data =[region_code, sum_value, num_countries]
    """
    num_years = float(int(years[1]) - int(years[0]))
    region_data = [['']]
    region_value = 0.0
    for country in stats_dict:
        if country['region_code'] in regions:
            sum_region = country['region_code']
            sum_country_value = 0.0
            for statistic in country['statistic']:
                sum_stat_code = statistic['stats_code']
                if statistic['year'] >= years[0] and \
                   statistic['year'] <= years[1]:
                    sum_country_value += float(statistic['value'])
            country_avg = sum_country_value / num_years
            region_value = calc_region(country_avg, sum_region, region_data,
                                       stats_dict)
            region_data.append([sum_region, sum_stat_code, region_value])
    return (region_data)


def calc_stats(report_options, stats_dict):
#    weights = report_options[0]
    years = report_options[1]
    regions = report_options[2]
    selection_results = sum_report_data(years, regions, stats_dict)
    return (selection_results)
