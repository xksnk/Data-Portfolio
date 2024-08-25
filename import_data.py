#mode, you use one of the following options:
#'r' – read, 'w' – write, 'a' – append, '+' – create new file
with open('example_filepath/file', mode='r') as file:
	data = file.read()

#Importing a CSV file using pandas /// load the data into a dataframe
import pandas as pd
df = pd.read_csv('example_filepath/file')