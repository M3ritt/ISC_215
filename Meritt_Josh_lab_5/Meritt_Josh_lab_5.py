"""
    @Authors
        Josh Meritt : 805157393
    
    ISC 215 Lab Five: 
    
    Polynomial Regression
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures



def get_file():
    file = 'Warranty_Data_Set.csv'
    while True:
        try:
            dataset = pd.read_csv(file)
            read_data(dataset)
            return
        except FileNotFoundError:
            file = input("[Error] File was not found. Please enter a correct file: ")


def read_data(dataset):
    x = dataset.iloc[:,1:-1].values
    y = dataset.iloc[:,-1].values
    train_linear_model(x, y)
    plt.clf()
    train_polynomial_model(x, y)


def train_linear_model(x, y):
    Linear_Regression = LinearRegression()
    Linear_Regression.fit(x, y)
    visualize_linear_model(x, y, Linear_Regression)
    
    
def visualize_linear_model(x, y, Linear_Regression):
    plt.scatter(x, y, color = 'red')
    plt.plot(x, Linear_Regression.predict(x), color = 'blue')
    plt.title('Linear Model')
    plt.xlabel('Item Covered')
    plt.ylabel('Cost')
    plt.savefig('linear_model.png')
    plt.show()
    print('[Process complete] linear_model.png')
    

def train_polynomial_model(x, y):
    Polynomial_Regressor = PolynomialFeatures(degree = 4)
    x_Polynomial = Polynomial_Regressor.fit_transform(x)
    line_reg_2 = LinearRegression()
    line_reg_2.fit(x_Polynomial, y)
    visualize_polynomial_model(x, y, line_reg_2, Polynomial_Regressor)
    
    
def visualize_polynomial_model(x, y, line_reg_2, Polynomial_Regressor):
    plt.scatter(x, y, color = 'green')
    plt.plot(x, line_reg_2.predict(Polynomial_Regressor.fit_transform(x)), color = 'orange')
    plt.title('Polynomial Model')
    plt.xlabel('Item Covered')
    plt.ylabel('Cost')
    plt.savefig('polynomial_model.png')
    plt.show()
    print('[Process complete] polynomial_model.png')


if __name__ == '__main__':
  print(""" 
             _                             _       _                                    _             
            | |                           (_)     | |                                  (_)            
 _ __   ___ | |_   _ _ __   ___  _ __ ___  _  __ _| |  _ __ ___  __ _ _ __ ___  ___ ___ _  ___  _ __  
| '_ \ / _ \| | | | | '_ \ / _ \| '_ ` _ \| |/ _` | | | '__/ _ \/ _` | '__/ _ \/ __/ __| |/ _ \| '_ \ 
| |_) | (_) | | |_| | | | | (_) | | | | | | | (_| | | | | |  __/ (_| | | |  __/\__ \__ \ | (_) | | | |
| .__/ \___/|_|\__, |_| |_|\___/|_| |_| |_|_|\__,_|_| |_|  \___|\__, |_|  \___||___/___/_|\___/|_| |_|
| |             __/ |                                            __/ |                                
|_|            |___/                                            |___/                                 """)
  get_file();
  print("[Exiting program]")
