# About this App
Implementing the code from David Beazley's course (@dabeaz); with my notes, custom code, implementation.
# My code structure - Files overview:
porty-app/
    README.txt
    portfolio.csv
    prices.csv
    print_report.py # top-level script to run our code
    setup.py        # for distribution
    MANIFEST.in     # for distribution
    porty/
        __init__.py
        fileparse.py     # CSV Parsing
        follow.py        # Follow a log file
        pcost.py         # computes portfolio cost
        portfolio.py     # Portfolio class
        report.py        # Makes a report
        stock.py         # Stock class
        tableformat.py   # Formatted tables
        ticker.py        # Produce a real-time stock ticker
        typedproperty.py # Typed Class properties