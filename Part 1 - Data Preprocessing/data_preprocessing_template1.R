dataset = read.csv('data.csv')

dataset$Age = ifelse(is.na(dataset$Age),
                           ave(dataset$Age, FUN = function(x)mean(x,na.rm=TRUE))
                           ,dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x)mean(x,na.rm=TRUE))
                     ,dataset$Salary)

dataset$Country = factor(dataset$Country,levels=c('France','Spain','Germany'),label=c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,levels=c('No','Yes'),label=c(0,1))

install.packages('caTools')
library(caTools)

split = sample.split(dataset$Purchased,SplitRatio=0.8)