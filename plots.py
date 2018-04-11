from bokeh.plotting import figure, show

def plot(grid):
    color_to_plot = {'on_green':'#2ca02c', 'on_blue':'#1f77b4', 'on_red':'#ff7f0e',
                     'on_cyan':'#e377c2', 'on_yellow':'#e7ba52',
                     'on_magenta':'#d62728', 'on_white':'#636363'}
    p = figure()
    for cord, b in grid.batteries.items():
        x_h = [h.cord[0] for h in b.links]
        y_h = [h.cord[1] for h in b.links]
        x_b = [b.cord[0]]
        y_b = [b.cord[1]]
        p.diamond(x=x_h, y=y_h, size=10, color=color_to_plot[b.color])
        p.circle_x(x=x_b, y=y_b, size=13, color=color_to_plot[b.color], alpha=0.5)
    show(p)
