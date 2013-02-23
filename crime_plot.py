import datetime as dt
import csv
import pylab as pl
import pandas as pd

conv_date = lambda d: dt.datetime.strptime(d, '%m/%d/%Y').date()

years = [(conv_date('1/1/%s' % yr), conv_date('12/31/%s' % yr))
            for yr in range(2000, 2013)]

with open('data/CRIME_ALL.csv', 'rb') as crimefile:
    global crime
    cread = csv.reader(crimefile, delimiter=',').__iter__()
    header = cread.next()

    dateset = []
    typeset = []
    for row in cread:
        dateset.append(conv_date(row[0]))
        typeset.append(1)

    crime = pd.Series(typeset, dateset)

yearstarts = [yr[0] for yr in years]
yearsums = [sum(crime[yr[0]:yr[1]]) for yr in years]
