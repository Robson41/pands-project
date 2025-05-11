# pands-project
Project Explanantion:
Project Summary

The project involves analysing the Iris dataset using Python. The main tasks include:

Data Loading: The project begins by importing necessary libraries—pandas for data manipulation, matplotlib.pyplot for plotting, and os for file handling. It then loads the Iris dataset from a CSV file.

Directory Creation: It checks for the existence of specific output directories and creates them if they do not already exist. These directories include:
        output/summary.txt for storing summary statistics,
        output/histograms/ for saving histogram plots,
        output/scatter_plots/ for saving scatter plots.

Data Summarisation: The project generates a summary of each variable in the dataset using the pandas .describe() function, capturing statistics like mean, standard deviation, minimum, and maximum values. This summary is saved to a text file.

Histogram Plots: For each numeric variable, the project creates histograms to visualise the distribution of values. Each histogram is saved as a PNG file in the specified directory.

Scatter Plots: It generates scatter plots for each unique pair of numeric variables, illustrating the relationships between them. Points are colour-coded based on the species of the iris flower, and these plots are saved as PNG files as well.


Completion Notification: Finally, the script prints or logs a message indicating that the analysis is complete.

Overall, this project aims to provide a comprehensive analysis and visualisation of the Iris dataset, facilitating insights into the relationships and distributions of the data.


Project Sources:
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data









