# ---------- R Environment Setup ----------
import os
os.environ['R_HOME'] = r'C:/Program Files/R/R-4.5.0'

# ---------- Python Visualization Libraries ----------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from bokeh.plotting import figure, output_file, save
import altair as alt

# ---------- R Libraries via rpy2 ----------
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects.lib import ggplot2

# Core R packages
grdevices = importr('grDevices')
graphics = importr('graphics')
ggplot2_r = importr('ggplot2')
plotly_r = importr('plotly')
rgl = importr('rgl')
