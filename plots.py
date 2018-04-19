from bokeh.plotting import figure, show
from bokeh.models import HoverTool
import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

# plot with dict as subset

def plot(grid):
    color_to_plot = {'on_green':'#2ca02c', 'on_blue':'#1f77b4', 'on_red':'#ff7f0e',
                     'on_cyan':'#e377c2', 'on_yellow':'#e7ba52',
                     'on_magenta':'#d62728', 'on_white':'#636363'}
    p = figure()
    no = 1
    for cord, b in grid.batteries.items():
        x_h = [h.cord[0] for h in b.links]
        y_h = [h.cord[1] for h in b.links]
        x_b = [b.cord[0]]
        y_b = [b.cord[1]]
        p.diamond(x=x_h, y=y_h, size=10, color=color_to_plot[b.color], legend='battery'+str(no))
        p.circle_x(x=x_b, y=y_b, size=13, color=color_to_plot[b.color], alpha=0.5)
        no += 1
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    #p.add_tools(HoverTool(tooltips=None, renderers=[p], mode='hline'))
    show(p)

def hover_plot(grid):
    color_to_plot = {'on_green':'#2ca02c', 'on_blue':'#1f77b4', 'on_red':'#ff7f0e',
                     'on_cyan':'#e377c2', 'on_yellow':'#e7ba52',
                     'on_magenta':'#d62728', 'on_white':'#636363'}
    p = figure()
    bats = []
    no = 1
    for cord, b in grid.batteries.items():
        b_name = 'battery'+str(no)
        bats.append(b_name)
        x_h = [h.cord[0] for h in b.links]
        y_h = [h.cord[1] for h in b.links]
        x_b = [b.cord[0]]
        y_b = [b.cord[1]]
        p.diamond(x=x_h, y=y_h, size=10, name=b_name, color=color_to_plot[b.color], hover_fill_color="black", legend=b_name)
        p.circle_x(x=x_b, y=y_b, size=13, name=b_name, color=color_to_plot[b.color], alpha=0.5)
        no += 1
    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    hover = HoverTool(names=bats)
    hover.tooltips = [("Battery", "$color[hex, swatch]:fill_color")]
    #p.add_tools(hover)
    show(p)

def line_plot(data):
    p = figure(title="distribution", plot_width=300, plot_height=300)
    data = sorted([(d, data[d]) for d in data])
    p.line(x=[d[0] for d in data], y=[d[1] for d in data])
    show(p)
