# import uuid
# import subprocess

# def run_python_code(code, output_filename):
#     try:
#         unique_filename = str(uuid.uuid4()) + '.png'  # Unique filename using UUID
#         script = f"""
# import matplotlib.pyplot as plt
# {code}
# plt.savefig('static/{unique_filename}')
# """
#         with open("temp_script.py", "w") as f:
#             f.write(script)

#         subprocess.run(["python", "temp_script.py"], check=True)
#         return True, unique_filename  # Return the unique filename
#     except subprocess.CalledProcessError as e:
#         return False, str(e)




# import subprocess
# import os

# def run_python_code(code, output_filename):
#     try:
#         print("python")
#         script = f"""
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.graph_objects as go
# import plotly.express as px
# from bokeh.plotting import figure, output_file, save
# import altair as alt
# {code}
# plt.savefig('static/{output_filename}')
# """
#         with open("temp_script.py", "w") as f:
#             f.write(script)

#         subprocess.run(["python", "temp_script.py"], check=True)
#         return True, None
#     except subprocess.CalledProcessError as e:
#         return False, str(e)


# import subprocess
# import os

# def run_python_code(code, output_filename):
#     try:
#         print("Running Python visualization script...")

#         script = f"""
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.graph_objects as go
# import plotly.express as px
# from bokeh.plotting import figure, output_file, save, show
# import altair as alt
# import os

# os.makedirs('static', exist_ok=True)

# # USER CODE
# {code}

# # AUTO-SAVE SECTION
# try:
#     # Try saving with matplotlib
#     plt.savefig('static/{output_filename}.png')
#     print("Saved as Matplotlib image.")
# except Exception:
#     pass

# try:
#     # Try saving Plotly figure
#     if 'fig' in locals():
#         fig.write_html('static/{output_filename}.html')
#         print("Saved as Plotly HTML.")
# except Exception:
#     pass

# try:
#     # Try saving Bokeh
#     output_file('static/{output_filename}.html')
#     save(fig)
#     print("Saved as Bokeh HTML.")
# except Exception:
#     pass

# try:
#     # Try saving Altair
#     if 'chart' in locals():
#         chart.save('static/{output_filename}.html')
#         print("Saved as Altair HTML.")
# except Exception:
#     pass
# """

#         with open("temp_script.py", "w") as f:
#             f.write(script)

#         subprocess.run(["python", "temp_script.py"], check=True)
#         return True, None
#     except subprocess.CalledProcessError as e:
#         return False, str(e)


# import subprocess
# import os

# def run_python_code(code, output_filename="plot"):  # Default output filename
#     try:
#         print("Running Python visualization script...")

#         script = f"""
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.graph_objects as go
# import plotly.express as px
# from bokeh.plotting import figure, output_file, save, show
# import altair as alt
# import os

# os.makedirs('static', exist_ok=True)

# # USER CODE
# {code}

# # Try saving with matplotlib (PNG) as plot.png
# try:
#     plt.savefig('static/plot.png')
#     print("Saved as Matplotlib image (plot.png).")
# except Exception:
#     pass

# # Try saving Plotly figure (HTML) as plot.html
# try:
#     if 'fig' in locals():
#         fig.write_html('static/plot.html')
#         print("Saved as Plotly HTML (plot.html).")
# except Exception:
#     pass

# # Try saving Bokeh (HTML) as plot.html
# try:
#     if 'fig' in locals():
#         output_file('static/plot.html')
#         save(fig)
#         print("Saved as Bokeh HTML (plot.html).")
# except Exception:
#     pass

# # Try saving Altair (HTML) as plot.html
# try:
#     if 'chart' in locals():
#         chart.save('static/plot.html')
#         print("Saved as Altair HTML (plot.html).")
# except Exception:
#     pass
# """

#         # Write the dynamically created script to a temporary file
#         with open("temp_script.py", "w") as f:
#             f.write(script)

#         # Run the temporary Python script to generate the plots
#         subprocess.run(["python", "temp_script.py"], check=True)

#         # Return the URL of the generated plot(s)
#         plot_url = "/static/plot.png"  # Always Matplotlib plot (image)
#         plot_html_url = "/static/plot.html"  # For Plotly, Bokeh, Altair (HTML)

#         # Return both URLs so the frontend can decide which one to use
#         return True, {"plot_url": plot_url, "plot_html_url": plot_html_url}

#     except subprocess.CalledProcessError as e:
#         return False, str(e)



import subprocess
import os

def run_python_code(code, output_filename="plot"):  # Default output filename
    try:
        print("Running Python visualization script...")

        script = f"""
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
{code}

# Try saving with matplotlib (PNG) as plot.png
try:
    if 'plt' in locals():  # Check if plt exists for Matplotlib/Seaborn
        # Save the Matplotlib plot to a file (e.g., plot.png)
        plot_path = 'static/plot.png'
        plt.savefig(plot_path, format='png')
        print(f"Saved Matplotlib plot")

        # Create HTML content that references the saved PNG image directly
        html_content = f\"\"\" 
<html>
<head><title>Matplotlib Plot</title></head>
<body>    
    <img src="http://localhost:5000/static/plot.png" alt="Matplotlib Plot"/>
</body>
</html>
\"\"\"

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
        html_content = f\"\"\" 
<html>
<head><title>Seaborn Plot</title></head>
<body>    
    <img src="http://localhost:5000/static/plot.png" alt="Seaborn Plot"/>
</body>
</html>
\"\"\"

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
"""

        # Write the dynamically created script to a temporary file
        with open("temp_script.py", "w") as f:
            f.write(script)

        # Run the temporary Python script to generate the plots
        subprocess.run(["python", "temp_script.py"], check=True)

        # Return the URL of the generated plot(s)
        # plot_url = "/static/plot.png"  # Always Matplotlib plot (image)
        plot_html_url = "/static/plot.html"  # For Plotly, Bokeh, Altair (HTML)

        # Return both URLs so the frontend can decide which one to use
        return True, { "plot_html_url": plot_html_url}
        # return True, {"plot_url": plot_url, "plot_html_url": plot_html_url}

    except subprocess.CalledProcessError as e:
        return False, str(e)
