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

import pandas as pd, matplotlib.pyplot, os, requests, json
# Importing the requisite libraries necessary for dataset loading, manipulation, and plotting as well as the api and file handling liraries required to access the url and save it to a file. Also imported the json file for serialisation and deserialisation for when data is being transferred over the network

#Define the URL of the dataset:
iris_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Retrieving the iris dataset and assigning it to a response object
response = requests.get(iris_url) 

if response.status_code == 200: # Error handling
    #Save dataset in to a csv file
    with open('iris_dataset.csv', 'w') as f: # Creating the iris_url.csv file locally
        f.write(response.text) # Saving the content from the iris dataset url(as raw text) to the iris_dataset.csv file
        print("Iris dataset successfully saved to iris_url.csv file")
else:
    print("Failed to retrieve Iris dataset", "HTTP Response: ", response.status_code)

# Load the dataset into a pandas DataFrame
    iris_ds = pd.read_csv('iris_dataset.csv', header = None)
#Adding columns for enhanced readability
    iris_ds.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']






