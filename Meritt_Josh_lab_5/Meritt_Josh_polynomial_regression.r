#Polynomial Regression
#ISC 215
#Joshua Meritt

#install.packages("ggplot2", repos = "http://cran.us.r-project.org")
library(ggplot2)

dataset = read.csv('Warranty_Data_Set.csv')
#Remove the unwanted column
dataset = dataset[2:3]

#Training the Linear model
Linear_Regression = lm(formula = Cost ~ Level, data = dataset)

#Training the Polynomial model
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

#Moving cost location using temp variable and removing old cost and temp variable
dataset$Cost_Temp = dataset$Cost
dataset$Cost = NULL
dataset$Cost = dataset$Cost_Temp
dataset$Cost_Temp = NULL

Polynomial_Regression = lm(formula = Cost ~ ., data = dataset)
summary(Polynomial_Regression)

#Visualize linear result - Results are not close at all and Polynomial model gets closer the more levels
# ggplot() +
#   geom_point(aes(x = dataset$Level, y = dataset$Cost),
#              colour = 'red') +
#   geom_line(aes(x = dataset$Level, y = predict(Linear_Regression, newdata = dataset)),
#             colour = 'blue') +
#   ggtitle('Linear Model') +
#   xlab('Level') + ylab('Cost')

#Visualize the Polynomial result
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Cost), 
             colour = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(Polynomial_Regression, newdata = dataset)),
            colour = 'blue') + 
  ggtitle('Polynomial Model 4') + 
  xlab('Level') + ylab('Cost')

