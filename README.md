# Covid19-Data-Analysis
This is Data Analysis Project attempts to find a relation between the spread of the the virus in a country and how happy people are, living in that country through GDP per capita, Healthy life expectancy, Social support etc.
The time period is from Jan'20 to April'20. This project was done under the guidance provided by Cousera. 

Consists of two data sets:
    
		- Covid19 dataset published by John Hopkins University which contains total number of confirmed cases in different countries.
		- World Happiness report which is an annual publication by united nations
		
## Structure
### Python Modules Used

	-Pandas
	-Numpy
	-Matplotlib
	-Seaborn

### Cleaning of Datasets
Both the datasets had many columns that werent required for the analysis hence they were removed by using drop feature in DataFrames in Pandas library. Apart from this maximum value from first derivative was calculated to obtain the rate of infection of the virus country wise.

### Merging Datasets
The datasets were merged to obtain a final dataset that had maximum infection rate, GDP per capita, Healthy Life Expectancy, Social Support, Happiness score etc. And a correlaation was obtained which turned out to be positive.

### Visualisation 
The result was then shown usind seaborn and matlpotlib in the form of scatterplot and curve fitting was done and shown on the same that visually represented the positive correlation.

### Conclusion 
Countries with higher happiness score had more infection rate

### Scope of Improvement 
The following conclusion can be further dwelled upoun and further correlations can be calculated between maximum infection rate and death rate. Also dataset can be expanded from April'20 to July'20 to get better results.
