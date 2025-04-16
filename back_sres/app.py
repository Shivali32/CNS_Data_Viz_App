from flask import Flask, request, jsonify, send_from_directory
import os, subprocess
from executor.run_python import run_python_code
from executor.run_r import run_r_code
import uuid
from flask_cors import CORS

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app, resources={r"/run": {"origins": "http://localhost:4200"}})  

OUTPUT_DIR = 'static'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# import viz_libs 

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



@app.route("/run", methods=["POST", "OPTIONS"])
def run_code():
    if request.method == "OPTIONS":
        return '', 204

    data = request.get_json()
    code = data.get("code")
    language = data.get("language")


    if language == "python":
        try:
            success, result = run_python_code(code)  
            
            if success:
                return jsonify({
                    "plot_html_url": result["plot_html_url"]  
                })
            else:
                return jsonify({"error": result}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    elif language == "r":
        try:
            output_filename = 'plot.png'  
            success, result = run_r_code(code, output_filename)  
            if success:
                return jsonify({
                    "plot_url": result["plot_url"]
                })
            else:
                return jsonify({"error": result}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid language"}), 400



@app.route("/static/<filename>")
def serve_output(filename):
    return send_from_directory(OUTPUT_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)