
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from bokeh.plotting import figure, output_file, save, show
import altair as alt
import os
import base64
from io import BytesIO

os.makedirs('static', exist_ok=True)

# USER CODE
fig = figure(title="Bokeh Line Plot", x_axis_label='X', y_axis_label='Y', width=400, height=400)
fig.line([1, 2, 3], [4, 5, 6], legend_label="Line 1", line_width=2)


# Try saving with matplotlib (PNG) as plot.png
try:
    if 'plt' in locals():  # Check if plt exists for Matplotlib/Seaborn
        # Save the Matplotlib plot to a file (e.g., plot.png)
        plot_path = 'static/plot.png'
        plt.savefig(plot_path, format='png')
        print(f"Saved Matplotlib plot")

        # Create HTML content that references the saved PNG image directly
        html_content = f""" 
<html>
<head><title>Matplotlib Plot</title></head>
<body>    
    <img src="http://localhost:5000/static/plot.png" alt="Matplotlib Plot" width="400"/>
</body>
</html>
"""

        # Save the HTML file
        with open('static/plot.html', 'w') as f:
            f.write(html_content)
        print("Saved as Matplotlib HTML (plot.html).")
except Exception:
    pass

# Try saving Seaborn plot as an HTML file (without base64 encoding)
try:
    if 'plt' in locals():  # Seaborn plots use Matplotlib's Axes
        # Save the Seaborn plot to a file (e.g., plot.png)
        plot_path = 'static/plot.png'
        plt.savefig(plot_path, format='png')
        print(f"Saved Seaborn plot")

        # Create HTML content that references the saved PNG image directly
        html_content = f""" 
<html>
<head><title>Seaborn Plot</title></head>
<body>    
    <img src="http://localhost:5000/static/plot.png" alt="Seaborn Plot"/>
</body>
</html>
"""

        # Save the HTML file
        with open('static/plot.html', 'w') as f:
            f.write(html_content)
        print("Saved as Seaborn HTML (plot.html).")
except Exception:
    pass

# Try saving Plotly figure (HTML) as plot.html
try:
    if 'fig' in locals():
        fig.write_html('static/plot.html')
        print("Saved as Plotly HTML (plot.html).")
except Exception:
    pass

# Try saving Bokeh (HTML) as plot.html
try:
    if 'fig' in locals():
        output_file('static/plot.html')
        save(fig)
        print("Saved as Bokeh HTML (plot.html).")
except Exception:
    pass

# Try saving Altair (HTML) as plot.html
try:
    if 'chart' in locals():
        chart.save('static/plot.html')
        print("Saved as Altair HTML (plot.html).")
except Exception:
    pass
