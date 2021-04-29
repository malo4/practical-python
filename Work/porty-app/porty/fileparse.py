# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(iterObject, select=None, types=None, has_headers=True, delimiter_custom=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and has_headers == False:
        raise RuntimeError("select argument requires column headers")
    
    # by all means now, separate rows of the given object (separated with regards to delimiter)
    rows = csv.reader(iterObject, delimiter=delimiter_custom)
        
    # Read the file headers (if file contains headers)
    if has_headers:
        headers = next(rows)
    else:
        headers = []
        
    # If a column selector was given, find indices of the specified columns. Remember,  When you read a row of data from the file, you need the indices to filter it
    if select:
        indices = [headers.index(colname) for colname in select] # the indices are used to filter it
        headers = select
    else:
        indices = []
    
    records = []
    
    for i, row in enumerate(rows):
        if not row:    # Skip rows with no data
            continue
        
        # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]
            
        if types:            
        # Modify type of value if types given
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", i, row)
                    log.debug("Row %d: Reason %s", i, e)
                continue
            
        if has_headers:
            record = dict(zip(headers, row))
        else: # for fles without headers- create a list of tuples instead 
            record = tuple(row)
            
        records.append(record)

    return records