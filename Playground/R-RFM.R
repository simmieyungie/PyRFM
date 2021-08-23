#rfm in R sampe
#install.packages("rfm")

#library
library(rfm)
library(tidyverse)

#data
df <- read.csv("C:\\Users\\SIMIYOUNG\\Documents\\Python-Projects\\RFM\\PyRFM\\Playground\\Retail_Data_Transactions.csv")


#preview
head(df)


#todays date
lubridate::date()

#reference date
analysis_date <- lubridate::as_date("2015-03-17")

#convert date column to date dtype
df$trans_date <- lubridate::dmy(df$trans_date)


#table
rfm_table_order(data = df,
                  customer_id = customer_id,
                  order_date = trans_date,
                  revenue = tran_amount,
                  analysis_date = analysis_date)

#rfm_table_order()
