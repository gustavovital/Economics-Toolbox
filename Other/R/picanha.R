install.packages("sidrar")
library(sidrar)
library(tidyverse)

data <- get_sidra(api = "/t/7060/n1/all/v/63/p/all/c315/7169,7170,7445,7486,7558,7625,7660,7712,7766,7786,47621/d/v63%202")
data_2 <- get_sidra(api = "/t/7060/n1/all/v/63/p/last%2023/c315/7169,7170,7445,7486,7558,7625,7660,7712,7766,7786,47621/d/v63%202")
data<-data[, -c(1,2,3,4,6,7,8,9,11,12)]
data_2<-data_2[, -c(1,2,3,4,6,7,8,9,11,12)]

data$mes_data <- as.Date(paste0(data$`Mês (Código)`, "01"), format = "%Y%m%d")
data_2$mes_data <- as.Date(paste0(data_2$`Mês (Código)`, "01"), format = "%Y%m%d")

data<-data[, -2]
data_2<-data_2[, -2]

data_wide <- data %>%
  pivot_wider(
    names_from = `Geral, grupo, subgrupo, item e subitem`, # Coluna cujos valores se tornarão nomes das colunas
    values_from = Valor # Coluna cujos valores preencherão as novas colunas
  )

data_wide_2 <- data_2 %>%
  pivot_wider(
    names_from = `Geral, grupo, subgrupo, item e subitem`, # Coluna cujos valores se tornarão nomes das colunas
    values_from = Valor # Coluna cujos valores preencherão as novas colunas
  )


cols_to_accumulate <- names(data_wide)[2:ncol(data_wide)] # Todas as colunas, exceto a primeira (mes_data)
cols_to_accumulate_2 <- names(data_wide_2)[2:ncol(data_wide_2)] # Todas as colunas, exceto a primeira (mes_data)

# Aplicar cumsum para cada coluna selecionada
data_wide[cols_to_accumulate] <- lapply(data_wide[cols_to_accumulate], cumsum)
data_wide_2[cols_to_accumulate_2] <- lapply(data_wide_2[cols_to_accumulate_2], cumsum)

colnames(data_wide) <- gsub("^\\d+\\.", "", colnames(data_wide)) # Remove números seguidos de ponto no início
colnames(data_wide) <- gsub("\\.", "", colnames(data_wide))      # Remove todos os pontos restantes
colnames(data_wide_2) <- gsub("^\\d+\\.", "", colnames(data_wide_2)) # Remove números seguidos de ponto no início
colnames(data_wide_2) <- gsub("\\.", "", colnames(data_wide_2))      # Remove todos os pontos restantes

data_wide_2 %>% 
  ggplot(aes(x=mes_data)) +
  geom_line(aes(y=`Picanha`)) +
  geom_line(aes(y=`Índice geral`)) + 
  geom_line(aes(y=`Alimentação e bebidas`)) 
  #geom_line(aes(y=`Habitação`)) + 
  geom_line(aes(y=`Picanha`)) + 
  geom_line(aes(y=`Picanha`)) 
