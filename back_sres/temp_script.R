
library(ggplot2)

data <- data.frame(x = c(1, 2, 3, 4), y = c(10, 11, 12, 13))
ggplot(data, aes(x=x, y=y)) +
    geom_point() +
    ggtitle("ggplot2 Scatter Plot") +
    xlab("X Axis") +
    ylab("Y Axis")
ggsave("static/plot.png")
