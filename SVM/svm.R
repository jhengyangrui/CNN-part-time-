install.packages("e1071", dep = TRUE)
require(e1071)

train <- read.csv("train_SMOTE_ALL.csv")
test <- read.csv("test_SMOTE_ALL.csv")
head(train)
str(train)

svmall <- svm(Y ~ ., data = train)
summary(svmall)

train.pred = predict(svmall, train)
test.pred = predict(svmall, test)

table(real=test$Y, predict=test.pred)

confus.matrix = table(real=test$Y, predict=test.pred)
sum(diag(confus.matrix))/sum(confus.matrix)
acc = sum(diag(confus.matrix))/sum(confus.matrix)

#-----------------------------------------------
trainBICP <- read.csv("trainBICP.csv")
testBICP <- read.csv("testBICP.csv")

svmBICP <- svm(Y ~ ., data = trainBICP)
summary(svmBICP)

trainBICP.pred = predict(svmBICP, trainBICP)
testBICP.pred = predict(svmBICP, testBICP)
#testBICP.pred
table(real=testBICP$Y, predict=testBICP.pred)

confus.matrix = table(real=testBICP$Y, predict=testBICP.pred)
sum(diag(confus.matrix))/sum(confus.matrix)

#----------------------------------------------------
trainRFM <- read.csv("trainRFM.csv")
testRFM <- read.csv("testRFM.csv")

svmRFM <- svm(Y ~ ., data = trainRFM)
summary(svmRFM)

trainRFM.pred = predict(svmRFM, trainRFM)
testRFM.pred = predict(svmRFM, testRFM)

table(real=testRFM$Y, predict=testRFM.pred)

confus.matrix = table(real=testRFM$Y, predict=testRFM.pred)
sum(diag(confus.matrix))/sum(confus.matrix)








