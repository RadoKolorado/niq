library(dplyr)
library(readr)
library(tidyverse)

scheduleall2 <- list.files(path = '~/Magisterka/Dane historyczne/Dane do modelu/Przerobione') %>%
  lapply(read_csv) %>%
  bind_rows



            