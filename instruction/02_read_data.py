# Pandas DataFrame Overview

# head()
# The head() method will display the first n rows of the dataframe.
# In the argument field, input the number of rows you want displayed in a Python notebook.
# The default is 5 rows.
# Example usage:
df.head(10)

# info()
# The info() method will display a summary of the dataframe, including the range index, dtypes, column headers, and memory usage.
# Leaving the argument field blank will return a full summary.
# Optionally, you can use the show_counts=True argument to display the count of non-null values for each column.
# Example usage:
df.info(show_counts=True)

# describe()
# The describe() method will return descriptive statistics of the entire dataset, including total count, mean, minimum, maximum, dispersion, and distribution.
# Leaving the argument field blank will default to returning a summary of the data frame’s statistics.
# Optionally, you can use “include=[X]” and “exclude=[X]” to limit the results to specific data types, depending on what you input in the brackets.
# Example usage:
df.describe()

# shape
# shape is an attribute that returns a tuple representing the dimensions of the dataframe by number of rows and columns.
# Remember that attributes are not followed by parentheses.
# Example usage:
df.shape

# Key takeaways:
# head(), info(), describe(), and shape are pandas tools that data scientists can use to understand a dataset at a high level.
# The information learned from using these tools will serve to inform the remainder of your Exploratory Data Analysis (EDA) work
# when you use pandas to analyze data throughout your career.