
library(ggplot2)
library(rgl)
library(grDevices)
library(vioplot)

# User-provided code
png(file="static/plot.png", width=600, height=600)
data <- data.frame(
x = c(324,432,354,350,234,453,876,523,456), 
y = c(765,673,768,876,584,464,654,364,453))
plot <- ggplot(data, aes(x=x, y=y)) +
    geom_point(size = 5, shape = 21, color = "blue", fill = "lightblue", alpha = 0.7) +
    ggtitle("ggplot2 Scatter Plot") +
    xlab("X Axis") +
    ylab("Y Axis")


dev.off()

# Check if plot exists and is a valid ggplot object
tryCatch({
    if (inherits(plot, "gg")) {
        ggsave("static/plot.png", plot = plot, width = 6, height = 6)
        print("2D Plot saved as PNG.")
    } else {
        print("No valid ggplot object found or plot is NA/NaN.")
    }
}, error = function(e) {
    print(paste("Error in saving 2D plot:", e$message))
})

# Check and save 3D plot if exists
tryCatch({
    if (exists("plot")){
        rgl.snapshot("static/plot.png")
        print("3D Plot saved as PNG.")
    } else {
        print("No valid rgl plot found.")
    }
}, error = function(e) {
    print(paste("Error in saving 3D plot:", e$message))
})
