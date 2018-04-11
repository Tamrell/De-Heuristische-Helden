from bokeh.plotting import figure, show

x_values = [1, 2, 3, 4, 5]
y_values = [6, 7, 2, 3, 6]
x1_values = [1, 2, 3, 4, 5]
y1_values = [3, 4, 1, 3, 4]

p = figure()
p.cross(x=x_values, y=y_values)
p.circle(x=x1_values, y=y1_values)
show(p)
