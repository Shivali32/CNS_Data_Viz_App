# CNS-SRES Data Visualization Web App
### Shivali Mate

## Overview

This project is a web application for executing and rendering **data visualizations** using both **Python** and **R** scripts. It enables users to run code snippets from either language and view the resulting static, interactive, or 3D plots directly on a web page.

- **Frontend**: Built using **Angular**, styled with **Bootstrap**.
- **Backend**: Built using **Flask** in Python, with separate execution logic for Python and R.
- **Integration**: Angular communicates with Flask using HTTP requests to send code and receive visualization results.
- **Plot Rendering**: 
  - Python interactive plots are rendered as **HTML**.
  - R static plots are rendered as **PNG**.

---

##  Tools & Libraries

### Frontend:
- Angular
- Bootstrap

### Backend:
- Flask
- rpy2 (for R execution)
- Python visualization libraries: Matplotlib, Seaborn, Plotly, Bokeh, Altair
- R visualization libraries: ggplot2, lattice, rgl, plotly, vioplot

---

## Folder Structure

```bash
cns_sres/
│
├── back_sres/
│   ├── app.py                  
│   ├── executor/
│   │   ├── __init__.py
│   │   ├── run_python.py       
│   │   └── run_r.py            
│   ├── static/                 
│   ├── requirements.txt
│   └── README.md
│
├── front_sres/
│   ├── src/
│   │   ├── app/
│   │   │   ├── code-editor/
│   │   │   │   ├── code-editor.component.ts
│   │   │   │   └── ...
│   │   │   ├── app.component.ts
│   │   │   └── ...
│   ├── angular.json
│   ├── package.json
│   └── README.md
│
└── recording.mp4                    
```
---
## Known Issues & Resolutions

### Issues Encountered:

1. **Saving and displaying plots**:  
   - Challenge: Generated plots were not appearing in the frontend.
   - Solution: Saved the files in the `/static` folder and rendered them based on their extension:
     - Python renders `.html` (for interactive/3D).
     - R renders `.png`.

2. **Submission doesn't refresh output**:  
   - Issue: Submitting the same language's code twice sometimes renders the old output.
   - Cause: Cached or non-overwritten file.
   - Temporary Fix: Ensured each request saves output under a unique name.
   - To Do: Implement better state and cache clearing mechanism.

---

## Demo & Recording

> A short screen recording (`recording.mp4`) showcases the following visualizations:

<video width="600" controls>
  <source src="recording.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Demo Visualizations

### Plot 1 – Python 3D Scatter Plot
- Created using `matplotlib` with `Axes3D` projection.
- Random data points visualized in a 3D space with color mapping (`viridis` colormap).

### Plot 2 – R Violin Plot
- Made using base R and the `vioplot` package.
- Shows mpg distribution across different cylinder categories in `mtcars`.

### Plot 3 – Python Interactive Bar Chart
- Built using `plotly.express`.
- Displays population by continent using the Gapminder dataset.

### Plot 4 – R Histogram
- A basic histogram of 100 random normal values.
- Styled with color and borders for clarity.

### Plot 5 – Python Plotly Scatter Plot
- Random x and y values shown with `plotly.graph_objects`.
- Includes titles and labeled axes.

### Plot 6 – R ggplot2 Scatter Plot
- Uses `ggplot2` to create a clean scatter plot with custom styling.
- Includes axis titles and plot title.

### Plot 7 – Python Altair Bar Chart
- Simple and interactive bar chart created with `altair`.
- Encodes category and value data.

### Plot 8 – Python Bokeh Line Plot
- Interactive line plot with legends using `bokeh.plotting.figure`.
- Includes labeled axes and a styled line.


---
##  How to Run the Project

Follow the steps below to run both the backend and frontend of the application:

### 1. Start the Flask Backend

```bash
cd cns_sres
vcns\Scripts\activate
cd back_sres
flask run
```

### 2. Start the Angular Frontend

```bash
cd front_sres
npm install
ng serve
```
