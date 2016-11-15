from nvd3 import pieChart

#Open File to write the D3 Graph
output_file = open('test-nvd3.html', 'w')

type = 'pieChart'
chart = pieChart(name=type, color_category='category20c', height=450, width=450)
chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

#Create the keys
xdata = ['vlsi', 'image', 'micro', 'wireless']
ydata = [58301, 87518, 41236, 466680]

#Add the serie
extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
chart.buildhtml()
output_file.write(chart.htmlcontent)

#close Html file
output_file.close()