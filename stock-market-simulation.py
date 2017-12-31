import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as print:
    print.header('Playing with multiindices.')
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
    # import io
    # stream = io.StringIO()
    # df.info(buf=stream)
    # out.text(stream.getvalue())
    # out.data(sa[:2])
