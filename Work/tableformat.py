# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
    
    
class TextTableFormatter(TableFormatter):
    '''
    Inheritance - Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
class CSVTableFormatter(TableFormatter):
    '''
    Inheritance - Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
        
        
class HTMLTableFormatter(TableFormatter):
    '''
    Inheritance - Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
        

    def row(self, rowdata):
        print('<tr>', end='')
        for rd in rowdata:
            print(f'<td>{rd}</td>', end='')
        print('</tr>')
        
        
class FormatErrorCustom (Exception):
    pass
        
        
def create_formatter(name):
    ''' allows a user to create a formatter given an output name such as 'txt', 'csv', or 'html'
    '''
    if name == 'txt':
        fmt = TextTableFormatter()
    elif name == 'csv':
        fmt = CSVTableFormatter()
    elif name == 'html':
        fmt = HTMLTableFormatter()
    else:
        raise FormatErrorCustom(f'Unknown table format {name}')
    
    return fmt
    
    
def print_table(objects, cols, formatter):
    ''' A generalized funct. - prints a table showing user-specified attributes of a list of arbitrary objects
    '''
    formatter.headings(cols)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in cols ] # list comprehension - getting attribute(s) of given object(cols given; interested in)
        formatter.row(rowdata)
        
    return