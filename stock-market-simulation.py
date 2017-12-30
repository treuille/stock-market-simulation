import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as out:
    out.header('Playing with multiindices.')
    dates = pd.date_range('12/30/2017', periods=8)
    df = pd.DataFrame(np.random.randn(8, 4), index=dates)
    df.columns = list('ABCDE'[:4])
    out.data(df)
