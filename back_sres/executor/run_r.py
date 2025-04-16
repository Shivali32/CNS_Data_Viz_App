import subprocess
import os
os.environ['R_HOME'] = r'C:/Program Files/R/R-4.5.0'

def run_r_code(code, output_filename):
    try:
        script = f"""
library(ggplot2)
library(rgl)
library(grDevices)
library(vioplot)

# User-provided code
png(file="static/{output_filename}", width=600, height=600)
{code}
dev.off()

# Check if plot exists and is a valid ggplot object
tryCatch({{
    if (inherits(plot, "gg")) {{
        ggsave("static/{output_filename}", plot = plot, width = 6, height = 6)
        print("2D Plot saved as PNG.")
    }} else {{
        print("No valid ggplot object found or plot is NA/NaN.")
    }}
}}, error = function(e) {{
    print(paste("Error in saving 2D plot:", e$message))
}})

# Check and save 3D plot if exists
tryCatch({{
    if (exists("plot")){{
        rgl.snapshot("static/{output_filename}")
        print("3D Plot saved as PNG.")
    }} else {{
        print("No valid rgl plot found.")
    }}
}}, error = function(e) {{
    print(paste("Error in saving 3D plot:", e$message))
}})
"""
        with open("temp_script.R", "w") as f:
            f.write(script)

        subprocess.run(["Rscript", "temp_script.R"], check=True)
        plot_url = f"/static/{output_filename}"
        return True, {"plot_url": plot_url}
    except subprocess.CalledProcessError as e:
        return False, str(e)

