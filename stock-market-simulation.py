import notebook

with notebook.Notebook() as out:
    print('Created notebook.')
    print('Sleeping 10 seconds.')
    import time
    out.header('Interations:')
    for x in range(5):
        time.sleep(1)
        out.text('iteration:', x)
    out.header('Finished iterations:')
    out.text('final_iteration\nwhat about this?\n...and this?')

# from bokeh import plotting
# import numpy as np
# from numpy import random
# import math
#
# # prepare some data
# N = 4000
# width = 1000
# xs = np.arange(0, 10, 0.25)
# y1 = np.sin(xs)
# y2 = np.cos(xs)
#
# # output to static HTML file
# plotting.output_file("lines.html")
#
# # create a new plot with a title and axis labels
# tools = 'crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select'
# fig1 = plotting.figure(
#     tools=tools,
#     title=None,
#     x_axis_label='x',
#     y_axis_label='y')
# fig1.triangle(xs, y1,
#     size=10,
#     fill_color='blue',
#     fill_alpha=0.6,
#     line_color=None)
#
# # create a new plot with a title and axis labels
# tools = 'crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select'
# fig2 = plotting.figure(
#     tools=tools,
#     title=None,
#     x_axis_label='x',
#     y_axis_label='y')
# fig2.square(xs, y2,
#     size=10,
#     fill_color='red',
#     fill_alpha=0.6,
#     line_color=None)
#
# p = plotting.gridplot([[fig1], [fig2]])
#
# # show the results
# plotting.show(p)
