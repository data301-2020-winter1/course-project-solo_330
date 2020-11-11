# analysis

This directory holds all jupyter notebooks used in the project.

## milestone1.ipynb

Contains the three raw data sets loaded into dataframes in Python.

## milestone2.ipynb

Loads and processes the raw data set from 'lolchallengertotal.csv' into a dataframe called 'loldata' in Python.

The data is loaded using the load_and_process function from 'scripts/python_functions.py' in order to:
   - Combine mutually exclusive (binary) columns into a single more informative column.
       - For example, the binary columns 'blueWin' and 'redWin' can be condensed into a single more informative categorical column.
       - As only a single team can win, it makes more sense to have a column called 'winner' with the value being 'blue' or 'red'. 
   - Drop the original binary columns which are no longer needed. 
   - Rename columns to be more consistent and clear, and to fix spelling and capitalization mistakes. 
   - Order columns in a more appropriate, intuitive, and useful way.
