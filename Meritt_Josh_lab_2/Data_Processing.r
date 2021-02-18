#Data preprocessing

#ISC 215

#Joshua Meritt

#This was needed first time running to install caTools
#install.packages("caTools", repos = "http://cran.us.r-project.org")

dataset = read.csv('Data.csv')

#missing age
dataset$Age = ifelse(is.na(dataset$Age),
                    ave(dataset$Age, FUN = function(x)mean(x,na.rm = TRUE)),
                    dataset$Age)

#missing salary    
dataset$Salary = ifelse(is.na(dataset$Salary),
                       ave(dataset$Salary, FUN = function(x)mean(x,na.rm = TRUE)),
                       dataset$Salary)
                          
#encode categorical data
#encode city
dataset$City = factor(dataset$City,
                      levels = c('syracuse', 'oswego', 'Buffalo', 'Albany'),
                      labels = c(1,2,3,4))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(1,2))

library(caTools)
set.seed(123)

split = sample.split(dataset$Purchased, SplitRatio = 0.8)
#print(split)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature scaling
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
print(training_set)
