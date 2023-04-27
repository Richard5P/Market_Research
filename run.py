from loadcsv import import_csv2dict


def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
    # variables to be passed to reports
    weights = None
    years = None
    regions = None
    stats_dict = import_csv2dict('population')
    print(stats_dict)
#    rpt_options = input_rpt_options(weights, years, regions, stats_dict)
#    print(rpt_options)

main()