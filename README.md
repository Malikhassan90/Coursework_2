# Coursework_2

# Visualization Design
This is a Dash app that displays an Energy Prices Dashboard, which allows the user to view the prices of oil and natural gas over time. The visualisations included in the dashboard are a line graph, a histogram, a boxplot, and a scatterplot.
The target audience for this dashboard is likely energy industry professionals or analysts, who are interested in exploring and understanding the trends in energy prices over time. The questions that the visualisations are intended to address include: what is the overall trend of energy prices over time, what is the distribution of energy prices, what is the spread of energy prices and what is the relationship between the date and energy prices.
The design of the dashboard and the visualisations are appropriate for the target audience and questions. The line graph is appropriate for showing the overall trend of energy prices over time and the histogram is appropriate for showing the distribution of energy prices. The boxplot is appropriate for showing the spread of energy prices, and the scatterplot is appropriate for showing the relationship between the date and energy prices. The choice of colours, style, and titles are appropriate and help to clearly communicate the information.
However, there are some limitations in the current design. For example, the visualisations only show the prices of oil and natural gas, and do not allow the user to compare them. Additionally, the visualisations do not show the prices of other energy sources, which would be helpful in understanding the overall energy market. Furthermore, there are no interactive elements in the visualisations, such as the ability to zoom in or select specific data points, which would be useful for exploring the data in more detail.
Overall, the Energy Prices Dashboard is a good start for visualising energy prices, but there is room for improvement. To enhance the effectiveness of the visualisations, additional data sources and interactive elements could be added to provide a more comprehensive view of the energy market. Additionally, using appropriate literature and references could help to support the design decisions and further improve the visualisation.

The line graph is the primary visualization used to visualize the prices of the selected energy type over time. The line graph provides a clear overview of the trends and fluctuations in the prices over time, and it is easy for the user to compare the prices between different dates.
The histogram is used to visualize the distribution of the prices of the selected energy type. It provides an insight into the frequency of occurrence of different prices, which can be used to identify outliers or identify the most common prices. This can be especially useful for identifying trends in prices or for detecting unusual or unexpected spikes in prices.
The boxplot is used to visualize the quartiles of the prices of the selected energy type. It provides a compact representation of the distribution of prices, showing the minimum, first quartile, median, third quartile, and maximum prices. This can be useful for identifying outliers or for comparing the prices between different energy types.
The scatterplot is used to visualize the relationship between the prices and the dates of the selected energy type. The scatterplot provides a way to visualize the trend of the prices over time, and it can also help to identify any correlations between the prices and the dates. This visualization can be especially useful for detecting correlations between prices and specific events or for identifying unusual spikes or dips in prices.
In conclusion, the Energy Prices Dashboard provides an effective and intuitive way to visualize the prices of oil and natural gas over time. The visualizations are appropriate for the target audience and the questions they are intended to address, and they are designed to be easily interpreted and useful for the user.

Screenshots attached

# Dash App
# Energy Prices Dashboard
This is a dashboard application built using Dash, a web-based framework for building analytical web applications, to display the prices of energy commodities such as oil and natural gas.

# Data Loading
The data used in this dashboard is loaded using the Dask library, a flexible parallel computing library in Python, to handle large datasets efficiently. The data is loaded from two datasets available on DataHub.io, one for oil prices and the other for natural gas prices. The load_prices_dask function takes the data package URL and the required columns as arguments and returns a pandas DataFrame with the required data.

# Application Layout
The layout of the application is built using the Dash HTML Components and Dash Core Components libraries. The application consists of:
A dropdown to select the type of energy commodity to display the prices for.
A submit button to trigger the update of the graphs.
Four graphs to display the prices of the selected energy commodity in various forms: line graph, histogram, boxplot, and scatterplot.
# Functionality
The application consists of two callbacks, one to update the n_clicks state of the submit button and the other to update the graphs based on the selected energy commodity and the submit button clicks.
# Limitations
This application is only capable of displaying the prices of oil and natural gas as of the data cutoff date. Future updates to the data are not reflected in the application.

# Tools & Techniques
#Source code control:
https://github.com/Malikhassan90/Coursework_2.git

#Set-up instructions:
The code is written in Python and makes use of several libraries such as Dash, Pandas, and Dask to create a dashboard to visualize energy prices. To set up the program, you need to perform the following steps:
Install the required libraries by running the following command:
pip install dash pandas datapackage dask
Run the app using python app2.python
Go to broswer and enter 'http://127.0.0.1:8050/' and wait for the Visualization to display.