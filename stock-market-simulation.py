import notebook
import numpy as np
import pandas as pd
from bokeh import plotting

with notebook.Notebook() as out:
    N = 4000
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    y[0] = 55.0
    radii = np.random.random(size=N) * 1.5
    colors = ["#%02x%02x%02x" % (int(r), int(g), 150)
        for r, g in zip(50+2*x, 30+2*y)][:N]

    out.header('Displaying the arrays:')
    df = pd.DataFrame(np.array([x, y, radii]).T, columns=['X', 'Y', 'radii'])
    df['colors'] = colors
    out.data_frame(df)

    out.header('Summarizing some data:')
    out.data_frame(df.describe())

    # create a new plot with the tools above, and explicit ranges
    out.header('Lets make a plot:')

    p = plotting.figure(tools='crosshair,pan,box_zoom,reset',
        x_range=(0,100), y_range=(0,100))
    p.circle(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

    out.text('Showing the plot...')
    out.plot(p)
    out.text('The plot has been shown.')

#     # out.header('Combining Pandas and Bokeh')
#     # out.text('Now to learn how to write tables using pandas...')
#     #
#     # periods, columns = 3, 6
#     # dates = pd.date_range('20130101', periods=periods)
#     # from string import ascii_lowercase as lowercase
#     # df = pd.DataFrame(np.random.randn(periods, columns),
#     #     index=dates, columns=list(lowercase[:columns]))
#     #
#     # # display the dataframe
#     # out.data_frame(df)
#     #
#     # out.text('Describing the data')
#     # out.data_frame(df.describe())
#     #
#     # out.text('Here is a figure.')
#

#     # fig = plotting.figure(x_axis_type='datetime')
#     # fig.line
#
#     # out.text('Creating some random data...')
#     #
#     # # prepare some data


#
#     #
#     # out.text('Creating the plot random data...')
#     #
