'''
PSEUDOCODE
1. IMPORT required libraries
    pandas for data handling
    matplotlib.pyplot for plotting
    os for file/directory handling
    requests for downloading data from the internet
    combinations from itertools for generating variable pairs

2. DEFINE the URL to the Iris dataset.

3. SEND HTTP GET request to download the dataset.

4. IF the download is successful:
    Save the dataset to a local CSV file.
    PRINT confirmation message.
    ELSE
    PRINT an error message with the HTTP status code.

5. LOAD the dataset into a DataFrame using pandas.

6. ASSIGN column names to the dataset for clarity.

7. CREATE output directories if they don’t already exist:
    /output/
    /output/histograms/
    /output/scatter_plots/

8. GENERATE a summary of each numeric variable:
    Use .describe() to calculate statistics.
    SAVE the summary to output/summary.txt.


9. FOR each numeric column in the dataset:
    PLOT a histogram using matplotlib.
    LABEL the axes and title.
    SAVE each histogram to output/histograms/.
    CLEAR the figure before the next plot.

10. GET all numeric columns.

11. FOR every unique pair of numeric columns:
    FOR each species in the dataset:
    Filter the dataset by species.
    PLOT a scatter plot with different colors per species.
    LABEL axes and title.
    DISPLAY legend.
    SAVE the scatter plot to output/scatter_plots/.
    CLEAR the figure before the next plot.

12. COMPUTE correlation matrix using .corr() on numeric columns only.
    PLOT the matrix as a heatmap.
    LABEL the axes and add a color bar.
    SAVE heatmap as output/iris_correlation_heatmap.png.
    CLEAR the figure.

13. GROUP dataset by species using .groupby() and .describe().
    SAVE the grouped summary stats to output/grouped_statistics.txt.
'''

import pandas as pd, matplotlib.pyplot as plt, os, requests
# Importing the requisite libraries necessary for dataset loading, manipulation, and plotting as well as the api and file handling liraries required to access the url and save it to a file. Also imported the json file for serialisation and deserialisation for when data is being transferred over the network
from itertools import combinations  # Import combinations to get unique pairs

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

# Create a directory to store output files
output_dir = os.makedirs("output", exist_ok = True)
histograms_dir = os.makedirs("output/histograms/", exist_ok = True)
scatter_plots_dir = os.makedirs("output/scatter_plots/", exist_ok = True)

# GENERATE a summary of each variable:
# Use pandas .describe() function to get mean, std, min, max, etc.
# Save this summary to a text file
# Generate a summary of each variable in the dataset
summary_var = iris_ds.describe()

# Save this summary to a text file
with open("output/summary.txt", "w") as summary_file:
    summary_file.write(summary_var.to_string())

# FOR each numeric variable in the dataset:
# Plot a histogram using matplotlib
# Save each histogram as a PNG in "output/histograms/"
for column in iris_ds.select_dtypes(include=['float64', 'int64']).columns:# Iterating over columns and filtering columns based on their datatypes, and then retrieving relevant column names
    plt.hist(iris_ds[column], bins=10, color='blue', align="mid")# Plot a blue histogram with 10 bins aligned to bin midpoints for the current numeric column
    plt.title(f'Histogram of {column}')# Set the plot title using the current column name
    plt.xlabel(column)# Label the x-axis with the column name
    plt.ylabel('Frequency')# Label the y-axis as 'Frequency'
    plt.savefig(f'output/histograms/{column}_histogram.png')# Save the histogram plot as a PNG file in the output/histograms directory
    plt.clf()# Clear the figure for the next plot

    
#FOR each unique pair of numeric variables:
#Create a scatter plot showing the relationship between the pair
#Colour-code the points by species (target class)
#Save each scatter plot as a PNG in "output/scatter_plots/"  
# Select all numeric columns from the dataset (float64 and int64 types)
numeric_columns = iris_ds.select_dtypes(include=['float64', 'int64']).columns

# Generate all unique pairs of numeric columns for scatter plot comparisons
for col_x, col_y in combinations(numeric_columns, 2):
    # Loop through each species to plot them with different colors
    for species in iris_ds['species'].unique():
        # Filter the dataset for the current species
        subset = iris_ds[iris_ds['species'] == species]
        # Plot a scatter plot for the current pair of numeric columns, color-coded by species
        plt.scatter(subset[col_x], subset[col_y], label=species)

    # Set the title of the scatter plot to show which columns are being compared
    plt.title(f'{col_x} vs {col_y}')
    # Label the x-axis and y-axis with the corresponding column names
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    # Display the legend to distinguish between species
    plt.legend()
    # Save the scatter plot to the "output/scatter_plots" directory with an appropriate filename
    plt.savefig(f'output/scatter_plots/{col_x}_vs_{col_y}.png')
    # Clear the current figure to avoid overlap with the next plot
    plt.clf()


#Compute correlation matrix and save as heatmap
plt.figure(figsize=(8, 6))  # Set the size of the heatmap figure
correlation_matrix = iris_ds.select_dtypes(include=['float64', 'int64']).corr()  # Calculate correlation matrix for numeric columns only
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')  # Display matrix as an image (heatmap) using the 'coolwarm' color map
plt.colorbar()  # Add a color bar to show the scale of correlation values
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)  # Label x-axis with column names
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)  # Label y-axis with column names
plt.title("Correlation Heatmap of Iris Dataset")  # Add title to the heatmap
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.savefig("output/iris_correlation_heatmap.png")  # Save the heatmap as a PNG image
plt.clf()  # Clear the figure so it doesn't interfere with the next plot

#Group data by species and save group statistics
grouped_stats = iris_ds.groupby('species').describe()  # Group the data by species and get summary statistics (count, mean, std, etc.)
with open("output/grouped_statistics.txt", "w") as f:  # Create and open a text file for writing
    f.write(grouped_stats.to_string())  # Write the grouped stats to the file as plain text






