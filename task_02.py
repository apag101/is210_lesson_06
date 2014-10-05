#!usr/bin/env python#
# -*- coding: utf-8 -*-
"""Even and Odds Function."""


import data
import task_01

def get_average(D):
     
    """Returns Average of a list.

    Args:
    numbers(numeric).

    Returns:
    Number: Returns average as a float.

    Examples:
   
    """
    global TOTAL_AVG
    L = len(D)
    A= 0
    for x in D:
        A = A + x
    TOTAL_AVG = float(A / L)
    return TOTAL_AVG

def REPORT(D):

    """Returns Average of even and odd list.

    Args:
    numbers(numeric).

    Returns:
    Number: Returns report of average numbers.

    Examples:
   
    """

    EVEN_AVG = get_average(task_01.evens_and_odds(D))
    ODD_AVG = get_average(task_01.evens_and_odds(D, False))
    TOTAL_AVG = get_average(D)
        
    REPORT = '''    Task 02 Report
    -----------------------------
    Total AVG:      {T:,.2f}
    EVEN_AVG:       {E:,.2f}
    ODD_AVG:        {O:,.2f}'''.format(T=TOTAL_AVG, E=EVEN_AVG, O=ODD_AVG)
    print REPORT
