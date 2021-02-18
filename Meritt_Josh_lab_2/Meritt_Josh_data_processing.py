"""
    @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab Two: 
    
    Data processor
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def get_file():
    """
        Hard coded is the file given, but if file is not valid then it prompts user to enter correct file name. 
    """
    file = 'Data.csv'
    while True:
        try:
            dataset = pd.read_csv(file)
            read_data(dataset)
            return
        except FileNotFoundError:
            file = input("[Error] File was not found. Please enter a correct file: ")


def read_data(dataset):
    """
        Reads data from hard coded .csv file and returns x_train and x_test.
    """
    x = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values
    x[:,1:3] = missing_data(x)
    x = encoding_independent_variable(x)
    y = encoding_dependent_variable(y)
    x_train, x_test = split_and_scale(x,y)
    
    view_data(x_train, x_test)
    
    
def missing_data(x):
    """
        Takes care of the missing data.
    """
    imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
    imputer.fit(x[:,1:3])
    x[:,1:3] = imputer.transform(x[:,1:3])
    return x[:,1:3]
    
    
def encoding_independent_variable(x):
    """
        Encodes the independent variable.
    """
    ct = ColumnTransformer(transformers = [('encoder',OneHotEncoder(),[0])], remainder = 'passthrough')
    x = np.array(ct.fit_transform(x))
    return x
    
    
def encoding_dependent_variable(y):
    """
        Encodes the dependent variable.
    """
    le = LabelEncoder()
    y = le.fit_transform(y)
    return y
    
    
def split_and_scale(x,y):
    """
        Splits and scales the x and y variables by 20%
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
    sc = StandardScaler()
    x_train[:,4:] = sc.fit_transform(x_train[:,4:])
    x_test[:,4:] = sc.transform(x_test[:,4:])
    
    return x_train, x_test
    
    
def view_data(x_train, x_test):
    """
        Checks if the user would like to view the data. 
    """
    is_view = input("Would you like to view the data? (yes, y, or view to view data)")
    if is_view == 'yes' or is_view == 'y' or is_view == 'view':
        print("X train: \n", x_train, "\n\nX test: \n", x_test)
    
    
if __name__ == '__main__':
    print("""
     _____      _          _____                            _             
    |  _  \    | |        | ___ \                          (_)            
    | | | |__ _| |_ __ _  | |_/ / __ ___   ___ ___  ___ ___ _ _ __   __ _ 
    | | | / _` | __/ _` | |  __/ '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
    | |/ / (_| | || (_| | | |  | | | (_) | (_|  __/\__ \__ \ | | | | (_| |
    |___/ \__,_|\__\__,_| \_|  |_|  \___/ \___\___||___/___/_|_| |_|\__, |
                                                                     __/ |
                                                                    |___/ 
                                                                """)
    get_file()
    print("[Exiting program]")
    
    