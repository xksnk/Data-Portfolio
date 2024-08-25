# Working with Files in Python

# Opening a file in Python
# To open a file, use the open() function along with a mode.
# The mode defines how the file should be opened:
# 'r' – read (default mode),
# 'w' – write (will overwrite the file if it exists, or create a new one if it doesn't),
# 'a' – append (will add content to the end of the file if it exists, or create a new one if it doesn't),
# '+' – create a new file (use with 'r', 'w', or 'a' to add read, write, or append permissions).
# Example usage:
with open('example_filepath/file', mode='r') as file:
    data = file.read()

# Importing Data from a CSV File using Pandas

# To load data from a CSV file into a Pandas DataFrame, use the read_csv() function.
# You need to specify the path to the file as a string argument.
# Example usage:
import pandas as pd
df = pd.read_csv('example_filepath/file')

# The data is now loaded into the 'df' DataFrame and can be manipulated using various Pandas methods.