import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as print:
    print('Playing with simplified syntax.', fmt='header')
    df = pd.DataFrame(np.random.randn(500,2), columns=list('AB'))
    print('Hello world.', 123, 'abc', df)
    print('This is an alert.', fmt='alert')
    print(df.describe())
    print('And here is some info.')
    print(df, fmt='info')

    # smoothness = 100

    # out.data(df.describe())
    # df = pd.DataFrame({
    #     'A': np.convolve([1.0 / smoothness] * smoothness, df.A),
    #     'B': np.convolve([1.0 / smoothness] * smoothness, df.B)
    # })
    # out.data(df.describe())
    # out.data(df[:20])
    #
    # fig = plotting.Figure(width=500)
    # fig.line(df.index, df.A, line_color='red')
    # fig.line(df.index, df.B, line_color='blue')
    # out.plot(fig)
    # out.text('All done!')

    # print('Playing with multiindices.', fmt='header')
    # smoothness = 100
    # df = pd.DataFrame(np.random.randn(500,2), columns=list('AB'))
    # print(df.describe())
    # df = pd.DataFrame({
    #     'A': np.convolve([1.0 / smoothness] * smoothness, df.A),
    #     'B': np.convolve([1.0 / smoothness] * smoothness, df.B)
    # })
    # print(df.describe())
    # print(df[:20])
    #
    # fig = plotting.Figure(width=500)
    # fig.line(df.index, df.A, line_color='red')
    # fig.line(df.index, df.B, line_color='blue')
    # print(fig)

    # dates = pd.date_range('12/30/2017', periods=8)
    # df = pd.DataFrame(np.random.randn(8, 4), index=dates)
    # sa = pd.Series([1,2,3], index=list('abc'))
    # df.columns = list('ABCD')
    # out.data(df)
    # out.data(df.A)
    # out.data(df.B)
    # out.data(sa)
    # out.text(f'sa.a = {sa.a}')
    # out.text(f'sa.b = {sa.b}')
    # out.text(f'sa.c = {sa.c}')
    # sa.a = 5
    # out.data(sa)
    # df.A = range(len(df.index))
    # out.data(df)

    # out.data(sa[:2])
