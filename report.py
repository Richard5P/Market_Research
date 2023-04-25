from rpt_config import input_rpt_options
#from rpt_calc import *
#from rpt_output import *

"""
This file contains the classes, function and variables for
the production of statistical reports. The file is meant to be
imported into a main file for deployment. 
The features included in this file include:
    - User processes for configuring, running and outputting each report
        rpt_config.py
    - Calculations for reporting on the configured statistics
        rpt_calc.py
    - Outputing the results
        rpt_output.py
"""


def run_report(weights, years, regions, stats_dict):
    rpt_options = input_rpt_options(weights, years, regions, stats_dict)
    return (rpt_options)
