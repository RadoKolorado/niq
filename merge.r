library(readxl)
library(readr)

rm(list = ls())


schedule_stop_3 <- read_csv("schedule_stop_3.csv", 
                            col_types = cols(station_id = col_number()))

stationid <- read_excel("stationid.xlsx", 
                        col_types = c("numeric", "text"))

schedule3=merge(schedule_stop_3, stationid, by.x = "station_id", by.y = "station_id", all.x = TRUE)
schedule3 <- na.omit(schedule3)

write.csv(schedule3, "schedule3.csv")

# SPACJA

rm(list = ls())


schedule_stop_4 <- read_csv("schedule_stop_4.csv", 
                            col_types = cols(station_id = col_number()))

stationid <- read_excel("stationid.xlsx", 
                        col_types = c("numeric", "text"))

schedule4=merge(schedule_stop_4, stationid, by.x = "station_id", by.y = "station_id", all.x = TRUE)
schedule4 <- na.omit(schedule4)

write.csv(schedule4, "schedule4.csv")

# SPACJA

rm(list = ls())


schedule_stop_5 <- read_csv("schedule_stop_5.csv", 
                            col_types = cols(station_id = col_number()))

stationid <- read_excel("stationid.xlsx", 
                        col_types = c("numeric", "text"))

schedule5=merge(schedule_stop_5, stationid, by.x = "station_id", by.y = "station_id", all.x = TRUE)
schedule5 <- na.omit(schedule5)

write.csv(schedule5, "schedule5.csv")

# SPACJA

rm(list = ls())


schedule_stop_6 <- read_csv("schedule_stop_6.csv", 
                            col_types = cols(station_id = col_number()))

stationid <- read_excel("stationid.xlsx", 
                        col_types = c("numeric", "text"))

schedule6=merge(schedule_stop_6, stationid, by.x = "station_id", by.y = "station_id", all.x = TRUE)
schedule6 <- na.omit(schedule6)

write.csv(schedule6, "schedule6.csv")