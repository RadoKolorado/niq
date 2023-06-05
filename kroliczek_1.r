rm(list=ls())
library("dplyr")
library("ggplot2")
library("reshape")


samochody = read.csv("http://michal.ramsza.org/lectures/2_r_programming/data/data_2.csv",
                header=T, sep=",", dec=".")


samochody$NumOfOffers <- 1
dAggr <- aggregate(NumOfOffers~Brand+Engine_capacity, data=samochody, FUN=sum)

wykres1 <- (ggplot(dAggr, aes(x=Engine_capacity, y=Brand, size=NumOfOffers)) +
  geom_point(colour="blue", alpha = 0.2)
)
x11();print(wykres1)

mds <- reshape::cast(dAggr, Brand~Engine_capacity, fun.aggregate = "sum", value = "NumOfOffers")
tmpRownames <- mds[,1]
mds <- as.matrix(mds[,-1])

N <- length(tmpRownames)
M <- matrix( rep(0, N*N), ncol=N)

for(i in 1:N){
  for(j in 1:N){
    M[i,j] <- sqrt(sum((mds[i,] - mds[j,]) ^2))
  }
}

rownames(M) <- tmpRownames
colnames(M) <- tmpRownames

wyk <- as.data.frame(cmdscale(M))
colnames(wyk) <- c("X", "Y")
wyk$label <- rownames(wyk)

wykres2 <- (ggplot(wyk, aes(x=X, y=Y, label=label)) +
  geom_point(colour="blue") +
  geom_text(colour="blue")
)
x11();print(wykres2)