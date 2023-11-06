"""
A/B testing 

Description:
This script runs an A/B testing for company website. 

Author: Saeideh Kamgar [saeideh.kamgar@gmail.com]
Date: 01 Nov 2023
"""
from pathlib import Path
import pandas as pd
import statsmodels.stats.api as sms
from scipy.stats import shapiro, levene, mannwhitneyu

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm



# ----------------------------------------------------------------------------------------

def AB_testing(
    working_path,
    countries_fname,
    ab_data_fname, 
    verbose=False,
    random_state=random_state,
):
    """
    Purpose:
    
    
    Args::
        working_path (str): Working directory, contains the input files
        countries_fname (float): the countries where the user is from
        ab_data_fname (str): filename of csv file of user info
        verbose (boolean): if True, return more reports on screen [Default: False]
        random_state (int): seed to generate the random number [Default: 2023]

    Example:
    Modify the working parameters and run the main script

    """

    # Taking care of inputs/outputs
    # ------------------------------------------------------------------------------------

    # check if working_path exists
    assert Path(working_path).is_dir(), f'No {working_path} directory exists!'

    # Define paths for data, models, and figures
    data_path = Path(working_path) / "data"
    Path(data_path).mkdir(parents=True, exist_ok=True)

    model_path = Path(working_path) / "model"
    Path(model_path).mkdir(parents=True, exist_ok=True)

    fig_path = Path(working_path) / "figures"
    Path(fig_path).mkdir(parents=True, exist_ok=True)



    # Loading data into pandas DF
    countries_file = data_path / countries_fname
    assert Path(countries_file).is_file(), f'No transactions file named {countries_file} found in {data_path}'
    ab_data_file = data_path / ab_data_fname
    assert Path(ab_data_file).is_file(), f'No labels file named {ab_data_file} found in {data_path}'
    countries_data = pd.read_csv(countries_file)
    ab_data = pd.read_csv(ab_data_file)


    if verbose:
        # Display trans dataset information
        #print(countries_data.info())
        #print(countries_data.shape)
        #print(countries_data.head(20))
        #print(countries_data.apply(lambda x: x.nunique()))

        # Display label dataset information
        print(ab_data.info())
        print(ab_data.head(20))
        print(ab_data.apply(lambda x: x.nunique()))
        print(ab_data.isnull().sum())
  

    # Data pre-processing: [part I]
        print(ab_data.shape)
        #remove rows which are duplicate values in the 'user_id' column.
        df2 = ab_data.drop_duplicates(subset= 'user_id', keep= False)
        print(df2.shape)
        print(df2.groupby(['group','landing_page']).agg({'landing_page': lambda x: x.value_counts()}))
        print(df2.groupby(['group','landing_page']).agg({'converted': 'mean'}))
        print(pd.DataFrame(df2.loc[:,'landing_page'].value_counts(normalize = True) * 100))
        df2[((df2['group'] == 'control') & (df2['landing_page'] == 'new_page')) |((df2['group'] == 'treatment') & (df2['landing_page'] == 'old_page')) ]
      

    # AB Test¶
    #Checking Normality Assumption¶
        test_stat, pvalue = shapiro(df2.loc[df2["landing_page"] == "old_page", "converted"])
        print("p-value:",pvalue)
        print("test_stat:",test_stat)

        test_stat, pvalue = shapiro(df2.loc[df2["landing_page"] == "new_page", "converted"])
        print("p-value:",pvalue)
        print("test_stat:",test_stat)

    # if p-value < 0.05, so assumption of normality is not provided and we use non-parametric test(mannwhitneyu test)
    #Cheking Variance Homogeneity
        test_stat, pvalue = levene(df2.loc[df2["landing_page"] == "new_page", "converted"],
                           df2.loc[df2["landing_page"] == "old_page", "converted"])
        print("p-value:",pvalue)  
        print("test_stat:",test_stat)
    # Hypothesis Testing¶
    test_stat, pvalue = mannwhitneyu(df2.loc[df2["landing_page"] == "new_page", "converted"],
                                 df2.loc[df2["landing_page"] == "old_page", "converted"])

    print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
    if pvalue > 0.05:
        print("There is no statistically significant difference between the new page and the old page")
    else:
        print("The new page brings profit")   
    # ------------------------------------------------------------------------------------

if __name__ == "__main__":
    # Set the input parameters (Refer to the README file for the description of each parameter)
    # -------------------------------------------------------------------------------------------------------------
    working_path = "/Users/your_directory"
    countries_fname = "countries.csv"
    ab_data_fname = "ab_data.csv"
    verbose = True
    random_state = 2023

    # Call the process_data function with the argument values
    AB_testing(
        working_path,
        countries_fname,
        ab_data_fname,
        verbose=verbose,
        random_state=random_state
    )


