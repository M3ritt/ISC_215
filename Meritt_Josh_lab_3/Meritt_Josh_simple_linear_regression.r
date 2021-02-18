#Simple Linear Regression
#ISC 215
#Joshua Meritt

#install.packages("caTools", repos = "http://cran.us.r-project.org")
install.packages("ggplot2", repos = "http://cran.us.r-project.org")

dataset = read.csv('Salary_Data.csv')

library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Linear regression
regressor = lm(formula = Salary ~ YearsExperienceInField, data = training_set)
library(ggplot2)

y_predictions = predict(regressor, newdata = test_set)

#Visualize the training set
ggplot()+
  geom_point(aes(x = training_set$YearsExperienceInField, y = training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperienceInField, y = predict
              (regressor, newdata = training_set)), 
              colour = 'blue') + 
  ggtitle('Salary vs Years Experience(Training set)') +
    xlab('Years Experience') + 
    ylab('Salary')

ggplot()+
  geom_point(aes(x = test_set$YearsExperienceInField, y = test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperienceInField, y = predict
                (regressor, newdata = training_set)), 
            colour = 'green') + 
  ggtitle('Salary vs Years Experience(Test set)') +
  xlab('Years Experience') + 
  ylab('Salary')
