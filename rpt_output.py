"""
This file contains the classes, function and variables for
the user processes for output presentation of the report calculations. 
The file is meant to be imported into and called from a parent file 
for deployment.
"""

from datetime import datetime
import csv


def output_results(calc_results):
    if export_rpt2csv(calc_results) and display_report(calc_results)
    return True
    else:
        return False


def export_rpt2csv(calc_results):
    