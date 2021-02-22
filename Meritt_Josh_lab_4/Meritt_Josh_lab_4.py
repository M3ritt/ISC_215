"""
    @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab Four: 
    
    Multi Linear Regressor
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

from sklearn.compose import ColumnTransformer as col_trans
from sklearn.preprocessing import OneHotEncoder as OHE
from sklearn.model_selection import train_test_split as tst
from sklearn.linear_model import LinearRegression as lr


def get_file():
    file = 'Startup_Co_Data_Set.csv'
    while True:
        try:
            dataset = pd.read_csv(file)
            read_data(dataset)
            return
        except FileNotFoundError:
            file = input("[Error] File was not found. Please enter a correct file: ")
            
            
def read_data(dataset):
    x = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values

    ct = col_trans(transformers = [('encoder', OHE(), [3])], remainder = "passthrough")
    x = np.array(ct.fit_transform(x))
    x = check_dummy_variable(x)
    train_data(x,y)
    
    
def train_data(x, y):
    x_train, x_test, y_train, y_test = tst(x, y, test_size = 0.2, random_state = 1)
    #print("\n===============================================================================\n" + 
    #"[x_train]:\n",x_train)
    
    #print("\n===============================================================================\n" + 
    #"[x_test]:\n",x_test)
    
    #print("\n===============================================================================\n" + 
    #"[y_train]:\n",y_train)
    
    #print("\n===============================================================================\n" + 
    #"[y_test]:\n",y_test)

    regressor = lr()
    regressor.fit(x_train, y_train)
    create_predictions(x_test, y_test, regressor, x, y)


def create_predictions(x_test, y_test, regressor, x, y):
    profit_predictions = regressor.predict(x_test)
    #print("\n===============================================================================\n" + 
    #"[profit_predictions]:\n",profit_predictions)
    
    np.set_printoptions(precision = 2)
    #print("\n===============================================================================\n" + 
    #"[np]:\n",
    #np.concatenate((profit_predictions.reshape(len(profit_predictions), 1), y_test.reshape(len(y_test), 1)), 1))
    

    x = np.append(arr = np.ones((50,1)).astype(int), values = x, axis = 1)
    x_optimal = x[:,[0,1,2,3,4,5]]
    x_optimal = x_optimal.astype(np.float64)

    regressor_Opt = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_Opt.summary()
    #print("\n===============================================================================\n" + 
    #"[Regressor opt summary]:\n" ,regressor_Opt.summary())

    x_optimal = x[:,[0,1,4,5]]
    x_optimal = x_optimal.astype(np.float64)
    #print("\n===============================================================================\n" + 
    #"[x_optimal]:\n",x_optimal)

    regressor_Opt = sm.OLS(endog = y, exog = x_optimal).fit()
    regressor_Opt.summary()
    #print("\n===============================================================================\n" + 
    #"[Regressor opt summary]:\n" ,regressor_Opt.summary())


def check_dummy_variable(x):
    x = x[:,1:]
    return x

    
    
if __name__ == '__main__':
  print("""
   _     _                        ______                             _             
  | |   (_)                       | ___ \                           (_)            
  | |    _ _ __   ___  __ _ _ __  | |_/ /___  __ _ _ __ ___  ___ ___ _  ___  _ __  
  | |   | | '_ \ / _ \/ _` | '__| |    // _ \/ _` | '__/ _ \/ __/ __| |/ _ \| '_ \ 
  | |___| | | | |  __/ (_| | |    | |\ \  __/ (_| | | |  __/\__ \__ \ | (_) | | | |
  \_____/_|_| |_|\___|\__,_|_|    \_| \_\___|\__, |_|  \___||___/___/_|\___/|_| |_|
                                              __/ |                                
                                             |___/                                 """)
  get_file();
  print("[Exiting program]")
