# Zadanie 1.1

rm(list=ls())
library(lattice)
library(latticeExtra)

wig=read.csv("wig.csv", 
             header=T, sep=",", dec=".")

wig$Data = as.Date(wig$Data)

plot_1 = xyplot(
  Otwarcie+Najwyzszy+Najnizszy+Zamkniecie~Data,
  data=wig,
  type="s",
  col.line=c("Blue","Pink","Green","Red"),
  pch=3,
  lwd=1,
  lty=1,
  xlab="Data",
  ylab="PLN",
  main="Ceny",
  auto.key=list(columns=4, rectangles=!F)
)

plot_2 = xyplot(
  Wolumen~Data,
  data=wig,
  type="s",
  col.line=c("Blue"),
  pch=3,
  lwd=1,
  lty=1,
  xlab="Data",
  ylab="Wolumen",
  main="Wolumen"
)

x11(width=10);
plot(plot_1, split=c(1,1,1,2), more=T)
print(plot_2, split=c(1,2,1,2), more=F)

# Zadanie 1.2

rm(list=ls())
library(lattice)
library(latticeExtra)

wig=read.csv("wig.csv", header=T, sep=",", dec=".")

wig$Data = as.Date(wig$Data)

wyk <- histogram(
  ~Zamkniecie-Otwarcie,
  data=wig,
  col="green",
  breaks=10,
  #type="percent"
  type="count"
)

x11()
print(wyk)

# Zadanie 1.3

rm(list=ls())
library(lattice)
library(latticeExtra)

wig=read.csv("wig.csv", header=T, sep=",", dec=".")
wig$Data = as.Date(wig$Data)
wig$Dni <- weekdays(wig$Data)


wig$roznica1=(wig$Najwyzszy-wig$Najnizszy)

wyk <- bwplot(
  wig$roznica1~wig$Dni,
  data=wig,
  fill="green",
  col=F,
  horizontal=F)
x11()
print(wyk)


