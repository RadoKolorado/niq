rm(list=ls())
library("ggplot2")

getNBPRates <- function(year=2021){

d <- readLines(paste0("https://www.nbp.pl/kursy/Archiwum/archiwum_tab_a_",year,".csv"))
d <- d[-2]
d <- d[-((length(d)-3) : length(d))]
x <- read.table(textConnection(d,encoding="UTF-8"),sep=";",dec=",",header=T)
x <- x[,-c((ncol(x)-2):ncol(x))]

x <- x[,grep("data|USD|EUR", colnames(x))]
colnames(x) <- gsub("X1","", colnames(x))
x$data <- as.Date(as.character(x$data),format="%Y%m%d")

return(x)

}

d_1 <- getNBPRates("2013")
d_2 <- getNBPRates("2014")
d_3 <- getNBPRates("2015")
d_4 <- getNBPRates("2016")
d_5 <- getNBPRates("2017")
d_6 <- getNBPRates("2018")
d_7 <- getNBPRates("2019")
d_8 <- getNBPRates("2020")

alldata <- rbind(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8)

#print(alldata)
print(head(alldata))
print(tail(alldata))

wykres <- ggplot(alldata, aes(x=data)) +
  geom_line( aes(y=USD), colour="blue", size=1) +
  geom_line( aes(y=EUR), colour="red", size=1) +
  ggtitle("Wykres kursow srednich NBP dla EUR i USD")

x11(width=15);
plot(wykres)