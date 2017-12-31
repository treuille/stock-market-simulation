import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as print:
    print('Learning about indices', fmt='header')
    dates = pd.date_range('12/31/2017', periods=8)
    df = pd.DataFrame(np.random.randn(8,4), index=dates, columns=list('ABCD'))
    print('dates:', dates)
    print('dataframe:', df)
    print('df.A and df.B', df[['A', 'B']])

    print('Reset first column.', fmt='header')
    df.A = range(len(df.index))
    print(df)
    print(df, fmt='info')

    print('Slicing some ranges...', fmt='header')
    print(df.B > 0, 'Only where B is positive:', df[df.B > 0])

    print('Getting a value directly', fmt='header')
    print(df.loc['1/4/2018', 'C'], type(df.loc['1/4/2018', 'C']))

    print('Looking at a row.', fmt='header')
    print(df.loc['1/4/2018'])

    print("Let's do some sampling...", fmt='header')
    print('n=3', df.sample(n=3))
    print('frac=0.5', df.sample(frac=0.5, replace=True))
