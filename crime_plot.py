import itertools as it
import datetime as dt
import csv
import pylab as pl
import pandas as pd

conv_date = lambda d, f: dt.datetime.strptime(d, f).date()


years = [(conv_date('1/1/%s' % yr, '%m/%d/%Y'),
          conv_date('12/31/%s' % yr, '%m/%d/%Y'))
            for yr in range(2000, 2013)]

weeks = [(conv_date('%s/%s' % (dy, yr), '%j/%Y'),
          conv_date('%s/%s' % (dy+7, yr), '%j/%Y'))
            for yr in xrange(2000, 2013) for dy in range(1, 360, 7)]

with open('data/CRIME_ALL.csv', 'rb') as crimefile:
    global crime
    cread = csv.reader(crimefile, delimiter=',').__iter__()
    header = cread.next()

    dateset = []
    typeset = []
    geoset = []
    for row in cread:
        dateset.append(conv_date(row[0], '%m/%d/%Y'))
        typeset.append(row[2])
        geoset.append((float(row[3]), float(row[4])))

    crime = pd.Series([1]*len(typeset), dateset)

geoset = pl.array(geoset)
types = list(set(typeset))

yearstarts = [yr[0] for yr in years]
weekstarts = [wk[0] for wk in weeks]
yearsums = [sum(crime[yr[0]:yr[1]]) for yr in years]
weeksums = [sum(crime[wk[0]:wk[1]]) for wk in weeks]

year_crime = pd.Series(yearsums, yearstarts)
week_crime = pd.Series(weeksums, weekstarts)

pl.figure(1)
geo_type_slice = {}
for tp in types:
    geo_type_slice[tp] = pl.array([(geoset[i])
        for i in xrange(len(geoset)) if typeset[i] == tp])

type_sig = [
    'o', 'o', 'o', 'o', 'o', 'o',
    'x', 'x', 'x', 'x', 'x', 'x',
    '*', '*', '*', '*', '*', '*',
    'D', 'D', 'D', 'D', 'D', 'D',
    ]
for i,tp in enumerate(types):
    data = geo_type_slice[tp]
    pl.plot(data[:, 0], data[:, 1], type_sig[i])
pl.legend(types)
pl.show()
