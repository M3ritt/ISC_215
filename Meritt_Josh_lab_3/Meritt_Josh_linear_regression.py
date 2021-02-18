"""
      @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab Three: 
    
    Linear Regression
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def get_file():
    file = 'Salary_Data.csv'
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
  creating_sets(x,y)
  
  
def creating_sets(x, y):
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)
  
  #print(x_train, x_test, y_train, y_test)
  regressor = LinearRegression()
  regressor.fit(x_train, y_train)

  #y_predictions = regressor.predict(x_test)
  #print(y_predictions)
  
  create_training_set(x_train, y_train, regressor)
  plt.clf() #Need to clear current plot or will be combined when plotting test set
  create_test_set(x_test, y_test, x_train, regressor)


def create_training_set(x_train, y_train, regressor):
  plt.scatter(x_train, y_train, color = 'red')
  plt.plot(x_train, regressor.predict(x_train), color = 'blue')
  plt.xlabel('Years Experience (Training set)')
  plt.ylabel('Salary')
  plt.savefig('TrainingSet.png')
  print('[Process complete] TrainingSet.png')
  

def create_test_set(x_test, y_test, x_train, regressor):
  plt.scatter(x_test, y_test, color = 'green')
  plt.plot(x_train, regressor.predict(x_train), color = 'blue')
  plt.xlabel('Years Experience (Test set)')
  plt.ylabel('Salary')
  plt.savefig('TestSet.png')
  print('[Process complete] TestSet.png')


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
