import streamlit as st
import pandas as pd
import plotly_express as px

# Read the dataset and create a new column 'manufacturer'
df = pd.read_csv('vehicles_us_clean.csv')
df['manufacturer'] = df['model'].apply(lambda model: model.split()[0])

# Section: Data Viewer
# Display a header and the DataFrame
st.header('Data viewer')
st.dataframe(df)

# Section: Vehicle Types by Manufacturer
# Display a header
st.header('Vehicle types by manufacturer')
# Create a histogram figure showing the distribution of vehicle types by manufacturer
fig = px.histogram(df, x='manufacturer', color='type')
# Update y-axis label
fig.update_yaxes(title_text='Qantity')
# display the figure with streamlit
st.write(fig)

# Section: Histogram of `condition` vs `year`
# Display a header
st.header('Distribution of `condition` by `year`')
# Radio button to select conditions
selected_condition = st.radio(
    'Select condition', df['condition'].unique(), index=0)
# Filter the DataFrame based on selected conditions
filtered_df = df[df['condition'] == selected_condition]
# Create a histogram figure showing the distribution of condition by year using filtered data

# Add checkbox to allow users to normalize the histogram
normalize = st.checkbox('Normalize histogram',
                        value=True, key='normalize_checkbox')
if normalize:
    histnorm = 'percent'
    y_axis_label = 'percentage'
else:
    histnorm = None
    y_axis_label = 'quantity'

fig = px.histogram(filtered_df, x='model_year',
                   color='condition',
                   histnorm=histnorm)
fig.update_yaxes(title_text=y_axis_label)
st.write(fig)

# Section: Barchart of `color` popularity
st.header('`Color` popularity')
# Create a color map to correspond to color names
color_counts = df['paint_color'].value_counts()
total_count = color_counts.sum()
color_percentages = (color_counts / total_count) * 100

# Create a DataFrame from the calculated percentages
df_percentages = pd.DataFrame(
    {'paint_color': color_percentages.index, 'percentage': color_percentages.values})

color_map = {
    'red': 'red', 'black': 'black', 'white': 'antiquewhite', 'grey': 'grey',
    'silver': 'silver', 'custom': 'cyan', 'orange': 'orange', 'yellow': 'yellow',
    'blue': 'blue', 'brown': 'brown', 'green': 'green', 'purple': 'purple',
    'unknown': 'crimson'
}

# Create the histogram using the calculated percentages
fig = px.bar(df_percentages, x='paint_color', y='percentage',
             color='paint_color', color_discrete_map=color_map)
st.write(fig)

# Section: Scatterplot of `condition` VS `odometer`
st.header('Scatterplot of `condition` VS `odometer`')
# create color map
color_map = {'like new': 'blue', 'excellent': 'green',
             'good': 'orange', 'fair': 'yellow', 'salvage': 'red', 'new': 'purple'}
# Checkbox to select conditions
selected_conditions = st.multiselect(
    'Select conditions', df['condition'].unique(), default=df['condition'].unique())

# Filter the DataFrame based on selected conditions
filtered_df = df[df['condition'].isin(selected_conditions)]
fig = px.scatter(filtered_df, x='odometer', y='price', color='condition',
                 size='model_year', color_discrete_map=color_map)
st.write(fig)

# Section: Compare condition distribution between manufacturers
st.header('Compare condition distribution between manufacturers')
# Get a sorted list of unique manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# Dropdown menu for selecting the 1st manufacturer
manufacturer_1 = st.selectbox(
    label='Select manufacturer 1',  # title of the select box
    options=manufac_list,  # options listed in the select box
    index=manufac_list.index('chevrolet')  # default pre-selected option
)
# Dropdown menu for selecting the 2nd manufacturer
manufacturer_2 = st.selectbox(
    label='Select manufacturer 2',
    options=manufac_list,
    index=manufac_list.index('hyundai')
)
# Filter the DataFrame based on the selected manufacturers
mask_filter = (df['manufacturer'] == manufacturer_1) | (
    df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# Add checkbox to allow users to normalize the histogram
normalize = st.checkbox('Normalize histogram',
                        value=True, key='normalize_checkbox1')
if normalize:
    histnorm = 'percent'
    y_axis_label = 'percentage'
else:
    histnorm = None
    y_axis_label = 'quantity'

# Create a histogram comparing the distribution of conditions between the selected manufacturers
fig = px.histogram(df_filtered,
                   x='condition',
                   # y='price',
                   #                   nbins=30,
                   color='manufacturer',
                   histnorm=histnorm,
                   barmode='group')
fig.update_yaxes(title_text=y_axis_label)
# display the figure with streamlit
st.write(fig)
