
library(readxl)
library(tidyverse)
library(fpp2)
library(forecast)
library(astsa)

EA_stock_price <- read_csv("Documents/EA_stock_price.csv")
data_prep <- EA_stock_price 
data_prep$Date <- as.Date(data_prep$Date)
data_prep$Year <- format(data_prep$Date, "%Y")
data_prep <- subset(data_prep, !(Year %in% c("1999", "2024")))
data_prep <- data_prep %>% select(-Year)
data_close <- ts(data_prep$`Close Price`, start = 2000,  frequency = 252)
tsplot(data_close, ylab="Close Price", main="Daily EA stock closing prices, 03/01/2000 - 29/12/2023")

# install.packages('quantmod')
install.packages(c("fpp2","forecast","astsa"),repos=c(CRAN = "http://cran.rstudio.com"))
# 
# library(quantmod)
# 
# ea_df <- getSymbols('EA.VI', src='yahoo', auto.assign=FALSE)
# autoplot(ea_df)
# chartSeries(ea_df, theme = chartTheme("white")) # função boa demais

install.packages("BETS")
# Load the BETS package
library(BETS)

# Retrieve the Brazilian GDP series (code 7326)
gdp <- BETSget(24363)
gdp_ts <- ts(gdp[,-1],start = c(2003,1), frequency = 12)

# graphs
ggmonthplot(gdp_ts) + 
  theme_minimal()

autoplot(gdp_ts)

ggseasonplot(gdp_ts)
ggsubseriesplot(gdp_ts)


par(mfrow=c(2,1))

autoplot((gdp_ts)) 
autoplot(log(gdp_ts))


gdp_ts.lambda=BoxCox.lambda(gdp_ts)
gdp_ts.lambda

gdp_ts.BC=BoxCox(gdp_ts,lambda=gdp_ts.lambda)
autoplot(gdp_ts.BC)

lag1.plot(gdp_ts,12)
fit <- lm(gdp_ts ~ time(gdp_ts))

summary(fit) # regress price on time

par(mfrow=c(2,1))
tsplot(gdp_ts, ylab="Brazilian GDP", col=4, lwd=2)
abline(fit)           # add the fitted regression line to the plot
tsplot(resid(fit), main="detrended")

# residuos<-resid(fit)
# summary(lm(residuos ~ time(residuos)))

lag1.plot(residuos,12)

