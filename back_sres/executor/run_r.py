# import subprocess  # Make sure subprocess is imported
# import uuid

# def run_r_code(code):
#     try:
#         # Generate a unique filename for the plot
#         unique_filename = str(uuid.uuid4()) + '.png'

#         # Create the R script with the unique filename
#         script = f"""
# {code}
# library(ggplot2)
# ggsave("static/{unique_filename}")
# """
#         # Write the script to a temporary R file
#         with open("temp_script.R", "w") as f:
#             f.write(script)

#         # Run the R script
#         subprocess.run(["Rscript", "temp_script.R"], check=True)

#         # Return the unique filename
#         return True, unique_filename

#     except subprocess.CalledProcessError as e:
#         # Return False and error message if there is an issue
#         return False, str(e)



import subprocess

def run_r_code(code, output_filename):
    try:
        script = f"""
library(ggplot2)
{code}
ggsave("static/{output_filename}")
"""
        with open("temp_script.R", "w") as f:
            f.write(script)

        subprocess.run(["Rscript", "temp_script.R"], check=True)
        plot_url = "/static/plot.png"
        return True, {"plot_url": plot_url}
    except subprocess.CalledProcessError as e:
        return False, str(e)


# import os
# os.environ['R_HOME'] = r'C:/Program Files/R/R-4.5.0'
# import subprocess
# import rpy2.robjects as ro
# from rpy2.robjects.packages import importr
# from rpy2.robjects.lib import ggplot2, rgl, graphics, grdevices

# # Import plotly manually as it is not part of rpy2.robjects.lib
# plotly = importr('plotly')

# def run_r_code_with_libraries(code, output_filename, plot_type="ggplot"):
#     try:
#         # Core R libraries
#         ggplot2_r = importr('ggplot2')
#         plotly_r = importr('plotly')
#         rgl_r = importr('rgl')
#         graphics_r = importr('graphics')
#         grdevices_r = importr('grDevices')
        
#         # Always save output as PNG
#         script = None

#         if plot_type == "ggplot":
#             script = f"""
# library(ggplot2)
# {code}
# ggsave("static/{output_filename}.png", width = 6, height = 6)
# """
#         elif plot_type == "plotly":
#             script = f"""
# library(plotly)
# {code}
# png("static/{output_filename}.png", width = 800, height = 600)
# plotly::plotly_IMAGE(p, format = "png", out_file = "static/{output_filename}.png")
# dev.off()
# """
#         elif plot_type == "rgl":
#             script = f"""
# library(rgl)
# {code}
# rgl.postscript("static/{output_filename}.png", fmt = "png")
# """
#         elif plot_type == "graphics":
#             script = f"""
# library(graphics)
# {code}
# dev.copy(png, file = "static/{output_filename}.png")
# dev.off()
# """
#         else:
#             return False, "Unsupported plot type"

#         # Write the R code to a temporary script file
#         with open("temp_script.R", "w") as f:
#             f.write(script)

#         # Execute the R script using subprocess
#         subprocess.run(["Rscript", "temp_script.R"], check=True)

#         # Return the plot URL
#         plot_url = f"/static/{output_filename}.png"
#         return True, {"plot_url": plot_url}

#     except subprocess.CalledProcessError as e:
#         return False, str(e)




# import os
# os.environ['R_HOME'] = r'C:/Program Files/R/R-4.5.0'
# import rpy2.robjects as ro
# from rpy2.robjects.packages import importr

# def run_r_code(code, output_filename):
#     try:
#         # Import necessary R libraries via rpy2
#         grdevices = importr('grDevices')
#         graphics = importr('graphics')
#         ggplot2_r = importr('ggplot2')
#         plotly_r = importr('plotly')
#         rgl = importr('rgl')

#         # Prepare the R code that loads libraries, runs user code, and saves the plot
#         r_code = f"""
# # Load R libraries
# library(ggplot2)
# library(plotly)
# library(rgl)

# # User-provided code
# {code}

# # If the plot is ggplot2-based, convert to Plotly and save as HTML
# if (exists("plot")) {{
#   plotly_plot <- ggplotly(plot)
#   htmlwidgets::saveWidget(plotly_plot, 'static/{output_filename}')
#   print("Plot saved as HTML.")
# }}

# # If the plot is a 3D rgl plot, save it as an HTML file
# if (exists("rgl_plot")) {{
#   rgl::rgl.postscript('static/{output_filename}', fmt = 'html')
#   print("3D Plot saved as HTML.")
# }}
# """

#         # Execute the R code using rpy2
#         ro.r(r_code)

#         return True, None
#     except Exception as e:
#         return False, str(e)

