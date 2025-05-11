# pands-project
Project Explanantion:
'''BEGIN analysis.py

1. IMPORT necessary libraries:
    - pandas for data manipulation
    - matplotlib.pyplot for plotting
    - os for file handling

2. LOAD the Iris dataset:
    - Use pandas to read the dataset from a CSV file

3. CREATE a directory (if not already exists) to store output files:
    - "output/summary.txt"
    - "output/histograms/"
    - "output/scatter_plots/"

4. GENERATE a summary of each variable:
    - Use pandas .describe() function to get mean, std, min, max, etc.
    - Save this summary to a text file

5. FOR each numeric variable in the dataset:
    - Plot a histogram using matplotlib/seaborn
    - Save each histogram as a PNG in "output/histograms/"

6. FOR each unique pair of numeric variables:
    - Create a scatter plot showing the relationship between the pair
    - Colour-code the points by species (target class)
    - Save each scatter plot as a PNG in "output/scatter_plots/"

7. (Optional but recommended) DO any additional analysis:
    - Example: compute correlation matrix and save as heatmap
    - Example: group data by species and calculate group statistics

8. PRINT or log a message indicating that all analysis is complete

END analysis.py'''


Project Sources:
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data









