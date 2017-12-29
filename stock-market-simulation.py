import notebook

with notebook.Notebook() as out:
    import numpy as np
    from bokeh import plotting

    # import figure, output_file, show

    out.header('A Test plot...')

    out.text('Creating some random data...')

    # prepare some data
    N = 4000
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    radii = np.random.random(size=N) * 1.5
    colors = [
        "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
    ]

    out.text('Creating the plot random data...')

    # create a new plot with the tools above, and explicit ranges
    TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    p = plotting.figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))
    p.circle(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

    out.text('Showing the plot...')
    out.plot(p)
    out.text('The plot has been shown.')
