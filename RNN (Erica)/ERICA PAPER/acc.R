rawdata <- read.csv("compare.csv", header = T)
head(rawdata)

fifth <- c()
for (i in 1:nrow(rawdata)) {
  if (i %% 5 == 0) {
    fifth <- rbind(fifth,rawdata[i,-1])
  }
}

fifth
confusion <- table(fifth)
accuracy <- (confusion[1,1] + confusion[2,2])/sum(confusion)
accuracy