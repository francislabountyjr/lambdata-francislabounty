# lambdata-francislabounty
A repo that contains a collection of modules to expand on the pandas library. (https://pandas.pydata.org/pandas-docs)

Contains a helper_function module to define a DfHelper class (initialized with a pandas dataframe) which contains various functions to help streamline some pandas operations.

The DfHelper class contains a randomize(seed) function which takes a seed as input and returns a shuffled version of a dataframe.

The null_count() function from the DfHelper class takes in no input (uses dataframe already in class) and returns the sum of null values of each column.