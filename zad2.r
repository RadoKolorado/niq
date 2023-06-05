# Zadanie 2.1

rm(list=ls())
library(ggplot2)
library(gridExtra)
library(ggimage)

wig=read.csv("wig.csv", header=T, sep=",", dec=".")

img <- "logo.jpg"

wig$Data = as.Date(wig$Data)

plot_1 = xyplot(
  Otwarcie+Najwyzszy+Najnizszy+Zamkniecie~Data,
  data=wig,
  type="s",
  col.line=c("Blue","Pink","Green","Red"),
  ylab="",
  xlab="",
  pch=3,
  lwd=1,
  lty=1,
  main="Notowania WIG",
)


plot_2 = xyplot(
  Wolumen~Data,
  data=wig,
  type="s",
  col.line=c("Black"),
  pch=3,
  lwd=1,
  lty=1,
  xlab="",
  ylab="",
  main="Wolumen"
)

x11(width=10);
plot(plot_1, split=c(1,1,1,2), more=T)
print(plot_2, split=c(1,2,1,2), more=F)


#Zadanie 2.2
rm(list=ls())
library(ggplot2)
library(gridExtra)
library(ggimage)

img <- "logo.jpg"
wig=read.csv("wig.csv", header=T, sep=",", dec=".")

wig$Data = as.Date(wig$Data)

wig$roznice1=(wig$Zamkniecie-wig$Otwarcie)

Roznica1 <- qplot(
  wig$roznice1,
  geom="histogram",
  binwidth=100,
  main="xyz",
  xlab="Roznice kurosw",
  fill=I("green"),
  col=I("red"),
  type="count"
  )

wyk <- ggbackground(Roznica1, img)
x11();print(wyk)

#Zadanie 2.3

rm(list=ls())
library(ggplot2)
library(gridExtra)
library(ggimage)

wig=read.csv("wig.csv", header=T, sep=",", dec=".")

wig$Data = as.Date(wig$Data)
wig$Dni <- weekdays(wig$Data)
img <- "logo.jpg"

dane <- ggplot(wig, aes(x="", y = Wolumen, fill = Dni)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  ggtitle("Wykres kolowy") +
  scale_fill_brewer(palette = "Spectral")+
  xlab("")

wyk <- ggbackground(dane, img)
x11();print(wyk)
