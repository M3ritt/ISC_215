"""
      @Authors
        Josh Meritt : 805157393
    
    Midterm part 2: 
    
    Simple Linear Regression
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def get_file():
    cwd = os.getcwd()
    file = 'Salary_Education_Data.csv'
    path = cwd + "\\" + file
    while True:
        try:
            dataset = pd.read_csv(path)
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

  y_predictions = regressor.predict(x_test)
  print("[Y_prediction]:", y_predictions)
  print("[Y_test]:", y_test)
  
  create_training_set(x_train, y_train, regressor)
  plt.clf() #Need to clear current plot or will be combined when plotting test set
  create_test_set(x_test, y_test, x_train, regressor)


def create_training_set(x_train, y_train, regressor):
  plt.scatter(x_train, y_train, color = 'red')
  plt.plot(x_train, regressor.predict(x_train), color = 'blue')
  plt.xlabel('Years of Education (Training set)')
  plt.ylabel('Salary')
  plt.savefig('TrainingSet.png')
  plt.show()
  print('[Process complete] TrainingSet.png')
  

def create_test_set(x_test, y_test, x_train, regressor):
  plt.scatter(x_test, y_test, color = 'green')
  plt.plot(x_train, regressor.predict(x_train), color = 'blue')
  plt.xlabel('Years of Education (Test set)')
  plt.ylabel('Salary')
  plt.savefig('TestSet.png')
  plt.show()
  print('[Process complete] TestSet.png')


if __name__ == '__main__':
  get_file();
  print("[Exiting program]")
