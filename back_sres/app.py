# from flask import Flask, request, jsonify, send_from_directory
# import os
# from executor.run_python import run_python_code
# from executor.run_r import run_r_code
# import uuid
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app, resources={r"/run": {"origins": "http://localhost:4200"}})  

# OUTPUT_DIR = 'static'
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# import viz_libs  
# # import matplotlib
# # matplotlib.use('Agg')  
# # import matplotlib.pyplot as plt


# # import os
# # os.environ['R_HOME'] = 'C:/Program Files/R/R-4.5.0'

# # import rpy2.robjects as ro

# # @app.route("/run", methods=["POST", "OPTIONS"])
# # def run_code():
# #     if request.method == "OPTIONS":
# #         return '', 204

# #     data = request.get_json()
# #     code = data.get("code")
# #     language = data.get("language")

# #     if language == "python":
# #         # Python code execution logic
# #         try:
# #             success, filename = run_python_code(code, 'plot.png')
# #             if success:
# #                 print(filename)
# #                 return jsonify({"url": f"/static/{filename}"}), 200
# #             else:
# #                 return jsonify({"error": filename}), 500
# #         except Exception as e:
# #             return jsonify({"error": str(e)}), 500

# #     elif language == "r":
# #         # R code execution logic
# #         try:
# #             success, filename = run_r_code(code)
# #             if success:
# #                 return jsonify({"url": f"/static/{filename}"}), 200
# #             else:
# #                 return jsonify({"error": filename}), 500
# #         except Exception as e:
# #             return jsonify({"error": str(e)}), 500

# #     return jsonify({"error": "Invalid language"}), 400


# @app.route("/run", methods=["POST", "OPTIONS"])
# def run_code():
#     if request.method == "OPTIONS":
#         return '', 204

#     data = request.get_json()
#     code = data.get("code")
#     language = data.get("language")

#     if language == "python":
#         try:
#             exec(code) 
#             plt.savefig('static/plot.png')  # Save the plot to the static folder
#             plt.close()  
#             return jsonify({"url": "/static/plot.png"})
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     elif language == "r":
#         try:            
#             ro.r(code) 
#             return jsonify({"url": "/static/r_plot.png"})
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     return jsonify({"error": "Invalid language"}), 400

# @app.route("/static/<filename>")
# def serve_output(filename):
#     return send_from_directory(OUTPUT_DIR, filename)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, request, jsonify, send_from_directory
import os, subprocess
from executor.run_python import run_python_code
from executor.run_r import run_r_code
import uuid
from flask_cors import CORS

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app, resources={r"/run": {"origins": "http://localhost:4200"}})  # Allow only Angular frontend

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

    # if language == "python":
    #     # Safely execute the Python code and save the plot
    #     try:
    #         exec(code)  # Execute the Python code
    #         plt.savefig('static/plot.png')  # Save the plot to the static folder
    #         plt.close()  # Close the plot to release memory
    #         return jsonify({"url": "/static/plot.png"})
    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500

    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500

    # elif language == "r":
    #     # Handle R code execution (you can add your R code execution logic here)
    #     try:
    #         # import rpy2.robjects as ro
    #         ro.r(code)  # Run the R code
    #         return jsonify({"url": "/static/r_plot.png"})
    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500

    # return jsonify({"error": "Invalid language"}), 400

    # if language == "python":
    #     # Call the function from `run_python.py` to execute the code
    #     try:
    #         output_filename = 'plot.png'  # You can also use uuid to make the filename unique
    #         success, error = run_python_code(code, output_filename)  # Run the Python code and save the plot
    #         if success:
    #             return jsonify({"url": f"/static/{output_filename}"})
    #         else:
    #             return jsonify({"error": error}), 500
    #     except Exception as e:
    #         return jsonify({"error": str(e)}), 500

    if language == "python":
        # Call the function from `run_python.py` to execute the code
        try:
            # Run the Python code and save the plot as plot.png and plot.html
            success, result = run_python_code(code)  # No need to pass output_filename since it's handled inside run_python_code
            
            if success:
                # Return the URLs for the generated plot(s)
                return jsonify({
                    # "plot_url": result["plot_url"],  # Matplotlib plot (image)
                    "plot_html_url": result["plot_html_url"]  # Plotly/Bokeh/Altair (HTML)
                })
            else:
                return jsonify({"error": result}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    elif language == "r":
        # Call the function from `run_r.py` to execute the R code
        try:
            output_filename = 'plot.png'  # You can also use uuid here for uniqueness
            success, result = run_r_code(code, output_filename)  # Run the R code and save the plot
            if success:
                # return jsonify({"url": f"/static/{output_filename}"})
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