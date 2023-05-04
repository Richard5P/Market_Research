"""
This file contains the classes, function and variables for
calculating the analytical report based on the configured statistics.
The file is meant to be imported into and called from a parent file for
deployment.
"""


def calc_region(country_avg, sum_region, region_data, stats_dict):
    """
    Checks if region has a sum_value. 
    If it does then add the country avg to it.
    Otherwise, set it
    returns it for
    use in summing region values for report
    """
    region_value = 0.0
    for i in range(0, len(region_data)):
        print(region_data[i], country_avg)
        if sum_region in region_data[i]:
            sum_value = region_data[i][2] + country_avg
        else:
            sum_value = country_avg
        region_data[i]['num_countries'] += 1
        region_value = sum_value / region_data[i]['num_countries']
    return (region_value)


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
    """
    num_years = float(int(years[1]) - int(years[0]))
    reg_stat_data = []
#   region_data = []
#   region_value = 0.0
    for country in stats_dict:
        sum_value = 0.0
        if country['region_code'] in regions:
            sum_region = country['region_code']
            for statistic in country['statistic']:
                sum_stat_code = statistic['stats_code']
                if statistic['year'] >= years[0] and \
                   statistic['year'] <= years[1]:
                    print(statistic['value'], sum_value)
                    sum_value = sum_value + float(statistic['value'])
                country_avg = sum_value / num_years
            reg_stat_data.append([sum_region, sum_stat_code, country_avg])
#            region_value = calc_region(country_avg, sum_region, region_data,
#                                       stats_dict)
#            region_data.append([sum_region, sum_stat_code, region_value])
    return (reg_stat_data)


def calc_stats(report_options, stats_dict):
#    weights = report_options[0]
    years = report_options[1]
    regions = report_options[2]
    selection_results = sum_report_data(years, regions, stats_dict)
    return (selection_results)
