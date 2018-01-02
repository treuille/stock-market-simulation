import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as print:
    print('Playing with timeseries', fmt='header')
    dates = pd.date_range('1/1/2018', periods=365)
    df = pd.DataFrame(np.random.randn(365), index=dates, columns=['deltas'])
    df['cumsum'] = df.cumsum()
    print(df)

    fig = plotting.Figure()
    fig.line(np.arange(10), np.arange(10), color='blue')
    # fig.line(df.index.values, df['deltas'].values)
    print('the figure:', fig)
