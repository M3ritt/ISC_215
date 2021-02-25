#Multiple Linear Regression
#ISC 215
#Joshua Meritt

#Ran on first time to install the package
#install.packages("caTools", repos = "http://cran.us.r-project.org")
library(caTools)

dataset = read.csv('Startup_Co_Data_Set.csv')

dataset$State = factor(dataset$State, 
                       levels = c ("New York", "Washington", "Connecticut"), 
                       labels = c (1,2,3))

set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 2/3)

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fit the model to the linear regressor
regressor = lm(formula = Profit ~ ., data = training_set)
#regressor = lm(formula = Profit ~ TechnologyBudget + HumanResources + Advertising + State, data = training_set)
regressor = lm(formula = Profit ~ TechnologyBudget + Advertising, data = training_set)

summary(regressor)
