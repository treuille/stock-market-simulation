import notebook
import numpy as np
import pandas as pd
from bokeh import plotting as bk_plot

with notebook.Notebook() as out:
    out.header('Combining Pandas and Bokeh')
    out.text('Now to learn how to write tables using pandas...')

    periods, columns = 50, 6
    dates = pd.date_range('20130101', periods=periods)
    from string import ascii_lowercase as lowercase
    df = pd.DataFrame(np.random.randn(periods, columns),
        index=dates, columns=list(lowercase[:columns]))

    # display the dataframe
    out.text('Here is a dataframe.')
    out.data_frame(df)

    out.text('Describing the data')
    out.data_frame(df.describe())

    out.text('Here is a figure.')
    # colors = ["#%02x%02x%02x" % (int(r), int(g), 150)
    #     for r, g in zip(50+2*x, 30+2*y)]
    # fig = plotting.figure(x_axis_type='datetime')
    # fig.line

    # out.text('Creating some random data...')
    #
    # # prepare some data
    # N = 4000
    # x = np.random.random(size=N) * 100
    # y = np.random.random(size=N) * 100
    # radii = np.random.random(size=N) * 1.5

    #
    # out.text('Creating the plot random data...')
    #
    # # create a new plot with the tools above, and explicit ranges
    # TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    # p = plotting.figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))
    # p.circle(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
    #
    # out.text('Showing the plot...')
    # out.plot(p)
    # out.text('The plot has been shown.')
