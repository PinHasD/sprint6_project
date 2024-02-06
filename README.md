Vehicle Analysis Dashboard
This dashboard provides an interactive exploration of a dataset containing information about vehicles in the US. It utilizes the Streamlit framework along with Plotly Express for data visualization.

Dataset
The dataset used in this dashboard (vehicles_us_clean.csv) contains cleaned data about vehicles, including the following information:
 year of manufacture, condition, number of cylinders, type of fuel, odometer reading, type of tramsmission, body type, paint color, is or isn't 4WD,  date posted, days listed, and manufacturer.

To run the dashboard click the link:

https://vehicles-us-nsix.onrender.com 



Features


Data Viewer

Displays the dataset with an option to view all data.


Vehicle Types by Manufacturer

Presents a histogram showing the distribution of vehicle types by manufacturer.


Distribution of condition by year

Allows users to select a condition and view its distribution across different years.


Color Popularity

Shows a barchart of the popularity of different colors among vehicles.


Scatterplot of condition VS odometer

Provides a scatterplot allowing users to explore the relationship between vehicle condition and odometer readings.


Compare Condition Distribution Between Manufacturers

Enables users to compare the distribution of vehicle conditions between two manufacturers.


Libraries used:


pandas == 2.2.0

scipy == 1.12.0

streamlit == 1.30.0

plotly.express == 0.4.1

altair == 5.2.0