# A/B testing for test the effect of new company's website based on user info.
Data Science Take-Home Task


This Python script performs AB hypothesis testing to determine if the effect of new website is significant or not.


## Installation

This script is compatible with Python 3.7 and above.

1 - Create and activate a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate # for Linux/Mac
env\Scripts\activate # for Windows


2- Install the required packages (already presented as a requirements.txt in the package directory):

pip install -r requirements.txt


## Usage

To run the script, first modify the working parameters and execute.

### Parameters

The script accepts the following parameters:

- --working_path (str): Working directory, contains the input files
- --countries_fname (float): the countries where the user is from
- --verbose (boolean): if True, return more reports on screen [Default: False]
- --ab_data (str): filename of CSV file of user info
- --random_state (int): seed to generate the random number [Default: 2023]


## Version

- Version: 0.0.1


## Author

- Author: Saeideh Kamgarsangari [saeideh.kamgar@gmail.com]


## Why Script Format?

This code is implemented as a script instead of a class-based structure for simplicity and ease of modification. This is in fact suitable for quick prototyping. However, to integrate this algorithm into a larger codebase or build a reusable library, I would refactor the script into a modular and extensible class-based structure.
