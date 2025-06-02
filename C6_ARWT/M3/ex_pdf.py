from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

table_data = []
for k, v in fruit.items():
  table_data.append([k, v])
#print(table_data)

report = SimpleDocTemplate("/tmp/report.pdf")
styles = getSampleStyleSheet()
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]


report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
empty_line = Spacer(1,20)       

report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

#print(report_pie.data)
# output: [2, 5, 8, 3, 1, 1, 13]
#print(report_pie.labels)
# output: ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, empty_line, report_table, empty_line, report_chart])
print("PDF report created successfully at /tmp/report.pdf")
