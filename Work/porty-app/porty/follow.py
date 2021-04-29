# follow.py
import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    Implication ... follow a log file
    '''
    f = open(filename)
    f.seek(0, os.SEEK_END)   # seek to the end - Move file pointer 0 bytes from end of file
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)    # Sleep briefly to avoid busy wait
            continue
        yield line   # Remember, any generator funct. uses 'yield' to emit values 
    
if __name__ == '__main__':
    import report
    
    portfolio = report.read_portfolio('Data/portfolio.csv')
    
    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')