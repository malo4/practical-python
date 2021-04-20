# ticker.py

from follow import follow
import csv

# generator funct. - to select specific columns
def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

# generator funct. - to convert data types (yields item using list comprehension)        
def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)] # remember, key/value pairs using zip()

# generator funct. - to build dict.
def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row)) # remember, common use of zip() -> constructing dicts.

def parse_stock_data(lines):
    '''
    Package a series of pipeline stages (into a single function call)
    '''
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

# generator funct. - filters data (yield specific items only)        
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row    
    
if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
        
def ticker(portfile, logfile, fmt):
    '''
    Creates a real-time stock ticker from a given portfolio, logfile, and table format.
    '''
    from report import read_portfolio
    import tableformat
    portfolio = read_portfolio(portfile)
    pricelive = parse_stock_data(follow(logfile))
    rows = filter_symbols(pricelive, portfolio)
    # print it out:
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )

    return