dataset = read.csv('data.csv')

dataset$age = ifelse(is.na(dataset$age),
                           avg(dataset$Age, FUN = function(x)mean(x,na.rm=TRUE))
                           ,dataset$age)